#!/usr/bin/env python3
"""Generate a dynamic food-image inventory dashboard.

Folders are the source of truth for category placement:
  Vegetables/ -> vegetables
  Fruits/     -> fruits
  Grains/     -> grains

Filename grammar:
  <item>_<specification>_<count>
  <item>_<count>

Examples:
  grapes_red_1.jpg
  grapes_red_2.jpg
  grapes_green_1.jpg

The dashboard creates a dynamic parent item and nested specification rows.
No fixed product catalog is required for discovering new names.
"""
from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".bmp", ".avif"}
CATALOG_TARGETS = {"Vegetables": 254}

ALIASES = {
    "eggplant": "brinjal", "aubergine": "brinjal", "jalepeno": "jalapeno",
    "green bell pepper": "green capsicum", "bell pepper": "capsicum",
    "lady finger": "okra", "ladyfinger": "okra", "bhindi": "okra",
    "drumstick": "moringa drumstick", "moringa": "moringa drumstick",
    "arbi": "colocasia arbi", "taro": "colocasia arbi",
    "suran": "elephant foot yam", "jimikand": "elephant foot yam",
    "karela": "bitter gourd", "lauki": "bottle gourd",
    "tori": "ridge gourd", "turai": "ridge gourd", "parwal": "pointed gourd",
    "kundru": "ivy gourd", "tinda": "round gourd", "chukandar": "beetroot",
    "gajar": "carrot", "mooli": "radish", "aloo": "potato",
    "adrak": "ginger", "lehsun": "garlic", "pyaz": "onion",
}


def clean_token(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "_", value).strip("_")
    return value


def display_name(value: str) -> str:
    return value.replace("_", " ").strip().title()


def normalize_name(value: str) -> str:
    value = clean_token(value).replace("_", " ")
    return ALIASES.get(value, value)


def parse_filename(stem: str):
    """Return (parent, specification, count) from the requested grammar.

    The final numeric token is always the image sequence number. Everything
    before it is split into parent/specification. If there are >=2 tokens,
    the first token is the parent and the remaining tokens are specification.
    This intentionally keeps the grammar simple and predictable.
    """
    s = clean_token(stem)
    match = re.match(r"^(?P<body>.+?)(?:_(?P<count>\d+))$", s)
    if match:
        body = match.group("body")
        count = int(match.group("count"))
    else:
        body = s
        count = None

    parts = body.split("_") if body else []
    if len(parts) >= 2:
        parent = normalize_name(parts[0])
        spec = normalize_name("_".join(parts[1:]))
    else:
        parent = normalize_name(body)
        spec = ""
    return parent, spec, count


def scan_folder(folder: Path):
    files = [p for p in folder.rglob("*") if p.is_file() and p.suffix.lower() in IMAGE_EXTENSIONS]
    products = defaultdict(lambda: {"base": [], "specs": defaultdict(list)})
    for path in files:
        parent, spec, count = parse_filename(path.stem)
        if not parent:
            continue
        if spec:
            products[parent]["specs"][spec].append(path)
        else:
            products[parent]["base"].append(path)
    return files, products


def load_catalog_counts():
    result = dict(CATALOG_TARGETS)
    for category in ("Vegetables", "Fruits", "Grains"):
        csv_path = ROOT / "data" / f"{category.lower()}.csv"
        if csv_path.exists():
            with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
                rows = list(csv.DictReader(f))
            if rows:
                result[category] = len(rows)
    return result


def pct(a: int, b: int) -> float:
    return a / b * 100 if b else 0.0


def progress(value: float, width: int = 20) -> str:
    filled = max(0, min(width, round(width * value / 100)))
    return "█" * filled + "░" * (width - filled)


def item_total(data) -> int:
    return len(data["base"]) + sum(len(v) for v in data["specs"].values())


def status(photo_count: int) -> str:
    if photo_count == 0:
        return "⚪ Missing"
    if photo_count >= 3:
        return "🟦 Rich"
    return "🟨 Covered"


def category_block(category: str, files, products, target: int | None):
    photos = len(files)
    covered = len(products)
    denominator = target or covered
    coverage = pct(covered, denominator)
    zero = max(denominator - covered, 0) if target else 0
    emoji = "🥬" if category == "Vegetables" else "🍎" if category == "Fruits" else "🌾"

    # Every discovered parent is a valid dynamic item. Specifications are
    # nested under their parent so names such as grapes_red and grapes_green
    # do not become unrelated top-level products.
    rows = []
    for parent in sorted(products):
        data = products[parent]
        total = item_total(data)
        rows.append((parent, total, data))

    table = [
        f"## {emoji} {category}", "",
        f"**{covered} detected items** · **{photos} photos** · **{coverage:.1f}% coverage**", "",
        f"`{progress(coverage)}` **{covered}/{denominator}**", "",
        "<details>",
        f"<summary>📋 View all {category.lower()} image statuses ({covered} items)</summary>",
        "",
        "| Item | Photos | Status |", "|---|---:|---|",
    ]

    for parent, total, data in rows:
        table.append(f"| **{display_name(parent)}** | **{total}** | **{status(total)}** |")
        if data["specs"]:
            table.extend(["", "<details>", f"<summary>↳ View {display_name(parent)} specifications</summary>", "", "| Specification | Photos | Status |", "|---|---:|---|"])
            for spec in sorted(data["specs"]):
                n = len(data["specs"][spec])
                table.append(f"| ↳ {display_name(parent)}_{display_name(spec).lower().replace(' ', '_')} | {n} | {status(n)} |")
            table.extend(["", "</details>", ""])

    table.extend(["", "</details>"])
    if zero:
        table.extend(["", f"> ⚪ **{zero} catalog target items still need at least one image.**"])
    table.extend(["", "---", ""])
    return "\n".join(table), covered, photos, denominator


def main():
    targets = load_catalog_counts()
    blocks = []
    total_photos = total_covered = total_catalog = 0
    summary = []

    for category in ("Vegetables", "Fruits", "Grains"):
        folder = ROOT / category
        files, products = scan_folder(folder) if folder.exists() else ([], {})
        block, covered, photos, denominator = category_block(category, files, products, targets.get(category))
        blocks.append(block)
        total_photos += photos
        total_covered += covered
        total_catalog += denominator
        summary.append((category, covered, photos, denominator))

    master_coverage = pct(total_covered, total_catalog)
    summary_table = [
        "## 📊 Live Master Dashboard", "", "| Catalog | Items detected | Catalog target | Photos | Coverage |",
        "|---|---:|---:|---:|---:|",
    ]
    for category, covered, photos, denominator in summary:
        summary_table.append(f"| {category} | {covered} | {denominator} | {photos} | {pct(covered, denominator):.1f}% |")
    summary_table += [
        "", f"**Total photos:** {total_photos}  ·  **Detected items:** {total_covered}  ·  **Overall coverage:** {master_coverage:.1f}%",
        "", f"`{progress(master_coverage)}` **{master_coverage:.1f}%**", "",
        "> 🤖 This section is generated by `scripts/update_image_inventory.py`. Do not edit it manually.", "",
    ]

    marker_start = "<!-- AUTO-INVENTORY:START -->"
    marker_end = "<!-- AUTO-INVENTORY:END -->"
    generated = marker_start + "\n" + "\n".join(summary_table + blocks) + marker_end
    original = README.read_text(encoding="utf-8") if README.exists() else "# Food Image Asset Library\n"
    if marker_start in original and marker_end in original:
        original = original.split(marker_start, 1)[0].rstrip() + original.split(marker_end, 1)[1]

    intro = "The system is designed for an e-commerce application where a single catalog item can have **multiple photographs**."
    if intro in original:
        insertion = intro + "\n\n---\n\n" + generated
        content = original.replace(intro + "\n\n---", insertion, 1)
    else:
        content = original.rstrip() + "\n\n" + generated + "\n"
    README.write_text(content, encoding="utf-8")
    print(f"Generated inventory: {total_photos} photos, {total_covered} dynamic items, {master_coverage:.1f}% coverage")


if __name__ == "__main__":
    main()
