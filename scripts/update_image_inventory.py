#!/usr/bin/env python3
"""Generate a fully dynamic food-image inventory dashboard.

Category is determined only by the top-level folder:
  Vegetables/ -> vegetables
  Fruits/     -> fruits
  Grains/     -> grains

Filename grammar:
  <item_name>_<type/specification>_<count_number>
  <item_name>_<count_number>

The folder contents are the source of truth. There is deliberately no fixed
catalog-size target: adding an image can discover a new item or specification.
"""
from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".bmp", ".avif"}

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
    s = clean_token(stem)
    match = re.match(r"^(?P<body>.+?)(?:_(?P<count>\d+))$", s)
    body = match.group("body") if match else s
    count = int(match.group("count")) if match else None
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
        parent, spec, _ = parse_filename(path.stem)
        if spec:
            products[parent]["specs"][spec].append(path)
        elif parent:
            products[parent]["base"].append(path)
    return files, products


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


def category_block(category: str, files, products):
    photos = len(files)
    unique_items = len(products)
    unique_specs = sum(len(data["specs"]) for data in products.values())
    coverage = 100.0 if unique_items else 0.0
    emoji = {"Vegetables": "🥬", "Fruits": "🍎", "Grains": "🌾"}[category]

    table = [
        f"## {emoji} {category}", "",
        f"**{unique_items} unique items** · **{unique_specs} unique specifications** · **{photos} photos**", "",
        f"`{progress(coverage)}` **{unique_items} items discovered**", "",
        "<details>",
        f"<summary>📋 View all {category.lower()} image statuses ({unique_items} items)</summary>",
        "",
        "| Item | Photos | Specifications | Status |", "|---|---:|---:|---|",
    ]

    for parent in sorted(products):
        data = products[parent]
        total = item_total(data)
        spec_count = len(data["specs"])
        table.append(f"| **{display_name(parent)}** | **{total}** | **{spec_count}** | **{status(total)}** |")
        if data["specs"]:
            table.extend(["", "<details>", f"<summary>↳ {display_name(parent)} — specifications</summary>", "", "| Subtype / Specification | Photos | Status |", "|---|---:|---|"])
            for spec in sorted(data["specs"]):
                n = len(data["specs"][spec])
                table.append(f"| `{parent.replace(' ', '_')}_{spec.replace(' ', '_')}` | {n} | {status(n)} |")
            table.extend(["", "</details>", ""])

    table.extend(["", "</details>", "", "---", ""])
    return "\n".join(table), unique_items, unique_specs, photos


def main():
    blocks = []
    total_photos = total_items = total_specs = 0
    summary = []

    for category in ("Vegetables", "Fruits", "Grains"):
        folder = ROOT / category
        files, products = scan_folder(folder) if folder.exists() else ([], {})
        block, items, specs, photos = category_block(category, files, products)
        blocks.append(block)
        total_photos += photos
        total_items += items
        total_specs += specs
        summary.append((category, items, specs, photos))

    summary_table = [
        "## 📊 Live Master Dashboard", "",
        "| Category | Unique items | Unique specifications | Total photos |", "|---|---:|---:|---:|",
    ]
    for category, items, specs, photos in summary:
        summary_table.append(f"| {category} | **{items}** | **{specs}** | **{photos}** |")
    summary_table += [
        "",
        f"**Master totals:** {total_items} unique items · {total_specs} unique specifications · {total_photos} photos",
        "",
        "> 🔄 **100% dynamic:** these numbers come directly from the current image folders. There is no fixed catalog target.",
        "",
        "### 🧩 Dynamic Structure", "",
        "| Level | What is counted |", "|---|---|",
        "| 🥬/🍎/🌾 Category | Top-level folder |",
        "| 🧺 Unique item | Parent name discovered from filenames |",
        "| 🏷️ Unique specification | Distinct `<type/specification>` under an item |",
        "| 📸 Photo | Every image file |",
        "| 📈 Item status | Based on total photos for that item |",
        "",
        "> Example: `grapes_red_1.jpg`, `grapes_red_2.jpg`, `grapes_green_1.jpg` → **Grapes: 3 photos, 2 unique specifications** → `grapes_red: 2`, `grapes_green: 1`.",
        "",
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
    print(f"Generated dynamic inventory: {total_items} items, {total_specs} specifications, {total_photos} photos")


if __name__ == "__main__":
    main()
