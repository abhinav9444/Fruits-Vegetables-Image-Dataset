#!/usr/bin/env python3
"""Generate the food-image inventory dashboard from the existing repo layout.

The repository intentionally keeps its existing top-level folders:
  Vegetables/, Fruits/, Grains/

The script groups files such as potato1.jpg, potato_2.jpg and potato-03.jpg
under one product and writes a generated dashboard to README.md.
"""
from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".bmp", ".avif"}

# Current master target from the project documentation. The catalog CSV can later
# replace this estimate with explicit item-level rows without changing the scanner.
CATALOG_TARGETS = {"Vegetables": 254}

# Filename aliases that occur commonly in the existing dataset.
ALIASES = {
    "eggplant": "brinjal",
    "aubergine": "brinjal",
    "jalepeno": "jalapeno",
    "green_bell_pepper": "green capsicum",
    "bell_pepper": "capsicum",
    "lady_finger": "okra",
    "ladyfinger": "okra",
    "bhindi": "okra",
    "drumstick": "moringa drumstick",
    "moringa": "moringa drumstick",
    "arbi": "colocasia arbi",
    "taro": "colocasia arbi",
    "suran": "elephant foot yam",
    "jimikand": "elephant foot yam",
    "karela": "bitter gourd",
    "lauki": "bottle gourd",
    "tori": "ridge gourd",
    "turai": "ridge gourd",
    "parwal": "pointed gourd",
    "kundru": "ivy gourd",
    "tinda": "round gourd",
    "chukandar": "beetroot",
    "gajar": "carrot",
    "mooli": "radish",
    "aloo": "potato",
    "adrak": "ginger",
    "lehsun": "garlic",
    "pyaz": "onion",
}


def normalize(value: str) -> str:
    value = value.lower().replace("&", " and ")
    value = re.sub(r"\.(jpg|jpeg|png|webp|gif|bmp|avif)$", "", value, flags=re.I)
    value = re.sub(r"[\-_]+", " ", value)
    # Remove dataset numbering and common image suffixes.
    value = re.sub(r"(?:\s+|^)(?:image|img|photo|pic)?\s*\d{1,6}$", "", value)
    value = re.sub(r"\s+(?:copy|final|edited|new|original|small|large)$", "", value)
    value = re.sub(r"\s+", " ", value).strip()
    if value in ALIASES:
        value = ALIASES[value]
    return value


def scan_folder(folder: Path):
    files = [p for p in folder.rglob("*") if p.is_file() and p.suffix.lower() in IMAGE_EXTENSIONS]
    products: dict[str, list[str]] = defaultdict(list)
    for path in files:
        key = normalize(path.stem)
        if key:
            products[key].append(path.relative_to(ROOT).as_posix())
    return files, products


def load_catalog_counts():
    """Use explicit catalog CSVs when the user adds them; otherwise keep targets from docs."""
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
    return (a / b * 100) if b else 0.0


def progress(value: float, width: int = 20) -> str:
    filled = round(width * value / 100)
    return "█" * filled + "░" * (width - filled)


def category_block(category: str, files, products, target: int | None):
    photos = len(files)
    covered = len(products)
    denominator = target or covered
    coverage = pct(covered, denominator)
    zero = max(denominator - covered, 0) if target else 0
    rows = sorted(products.items(), key=lambda x: (-len(x[1]), x[0]))
    table = [
        f"## {'🥬' if category == 'Vegetables' else '🍎' if category == 'Fruits' else '🌾'} {category}",
        "",
        f"**{covered} detected product groups** · **{photos} photos** · **{coverage:.1f}% coverage**",
        "",
        f"`{progress(coverage)}` **{covered}/{denominator}**",
        "",
        "| Product | Photos | Status |",
        "|---|---:|---|",
    ]
    for name, paths in rows:
        status = "🟦 Rich" if len(paths) >= 3 else "🟨 Covered"
        table.append(f"| {name.title()} | {len(paths)} | {status} |")
    if zero:
        table.extend(["", f"> ⚪ **{zero} catalog items still need at least one image.**"])
    table.extend(["", "---", ""])
    return "\n".join(table), covered, photos, denominator


def main():
    targets = load_catalog_counts()
    blocks = []
    total_photos = 0
    total_covered = 0
    total_catalog = 0
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
        "## 📊 Live Master Dashboard",
        "",
        "| Catalog | Items detected | Catalog target | Photos | Coverage |",
        "|---|---:|---:|---:|---:|",
    ]
    for category, covered, photos, denominator in summary:
        summary_table.append(f"| {category} | {covered} | {denominator} | {photos} | {pct(covered, denominator):.1f}% |")
    summary_table += [
        "",
        f"**Total photos:** {total_photos}  ·  **Detected product groups:** {total_covered}  ·  **Overall coverage:** {master_coverage:.1f}%",
        "",
        f"`{progress(master_coverage)}` **{master_coverage:.1f}%**",
        "",
        "> 🤖 This section is generated by `scripts/update_image_inventory.py`. Do not edit it manually.",
        "",
    ]

    original = README.read_text(encoding="utf-8") if README.exists() else "# Food Image Asset Library\n"
    marker_start = "<!-- AUTO-INVENTORY:START -->"
    marker_end = "<!-- AUTO-INVENTORY:END -->"
    generated = marker_start + "\n" + "\n".join(summary_table + blocks) + marker_end
    if marker_start in original and marker_end in original:
        before = original.split(marker_start, 1)[0]
        after = original.split(marker_end, 1)[1]
        content = before.rstrip() + "\n\n" + generated + after
    else:
        content = original.rstrip() + "\n\n" + generated + "\n"
    README.write_text(content, encoding="utf-8")

    print(f"Generated inventory: {total_photos} photos, {total_covered} product groups, {master_coverage:.1f}% coverage")


if __name__ == "__main__":
    main()
