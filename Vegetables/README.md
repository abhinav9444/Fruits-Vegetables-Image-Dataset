# 🥬 Vegetable Image Library

> Complete tracking document for the vegetable image catalog.

## 📊 Dashboard

| Metric | Value |
|---|---:|
| 🥬 Unique catalog items | **254** |
| 🖼️ Items with ≥1 image | **Auto-generated** |
| 📸 Total photos | **Auto-generated** |
| 📈 Unique-item coverage | **Auto-generated** |
| ⚪ Zero-photo items | **Auto-generated** |
| 📸 Average photos/item | **Auto-generated** |
| 🔴 P0 coverage | **Auto-generated** |
| 🟠 P1 coverage | **Auto-generated** |
| 🟡 P2 coverage | **Auto-generated** |
| 🟢 P3 coverage | **Auto-generated** |

---

## 📈 Progress Model

### Unique-item progress

```text
Items with ≥1 photo / 254
```

Each vegetable contributes **one point**, regardless of how many photos it has.

### Photo progress

Every image contributes to:

```text
Total photos
```

Therefore:

```text
Potato → 5 photos
```

means:

```text
1 unique item covered
5 total photos
```

---

# 📦 Categories

1. 🥔 Root, Tuber & Underground
2. 🍅 Tomato, Brinjal & Solanaceae
3. 🥒 Gourds
4. 🫘 Beans, Pods & Legumes
5. 🌽 Corn & Baby Corn
6. 🥦 Cruciferous Vegetables
7. 🌿 Indian Leafy Vegetables
8. 🌱 Shoots, Flowers & Tender Vegetables
9. 🍄 Mushrooms
10. 🌾 Less-common / Regional Indian Vegetables
11. 🌶️ Aromatics & Cooking Vegetables
12. 🫑 Premium / Exotic Vegetables

Each category receives:

```text
Items
Items with images
Total photos
Coverage
Average photos/item
Zero-photo items
Status
```

---

# 🗂️ Unique Vegetable Checklist

The canonical catalog contains **254 entries**.

The generated inventory should display:

```text
- [ ] Potato — Aloo · 📸 0
- [x] Sweet Potato — Shakarkand · 📸 3
```

`[x]` means at least one image exists.

`📸 N` is the exact number of detected photos.

The complete machine-readable catalog is maintained in:

```text
data/vegetables.csv
```

---

# ⭐ Priority

| Priority | Meaning |
|---|---|
| 🔴 P0 | Everyday essential |
| 🟠 P1 | High-frequency |
| 🟡 P2 | Regional / medium-frequency |
| 🟢 P3 | Long-tail / exotic |

Focus first on:

```text
Potato
Onion
Garlic
Ginger
Tomato
Carrot
Beetroot
Radish
Sweet Potato
Yam
Green Chilli
Capsicum
Bottle Gourd
Ridge Gourd
Bitter Gourd
Pointed Gourd
French Beans
Green Peas
Cauliflower
Broccoli
Cabbage
Spinach
Coriander
Mint
```

---

# 📸 Filename Rules

```text
potato.jpg
potato-02.jpg
potato-03.jpg
```

The scanner treats these as:

```text
Potato = 3 photos
```

Recommended folders:

```text
assets/images/vegetables/
├── root/
├── solanaceae/
├── gourds/
├── beans/
├── corn/
├── cruciferous/
├── leafy/
├── shoots-flowers/
├── mushrooms/
├── regional/
├── aromatics/
└── exotic/
```

---

# 🔐 Verification Checklist

For every selected image:

- [ ] Correct vegetable
- [ ] Correct variety
- [ ] Good resolution
- [ ] Clean background/presentation
- [ ] No unwanted watermark
- [ ] Commercial-use permission checked
- [ ] Source recorded
- [ ] Correct filename
- [ ] Correct catalog item
- [ ] Application test completed

---

# 🤖 Automation

Run:

```bash
python scripts/update_image_inventory.py
```

Or use GitHub Actions.

Automation should regenerate:

- README metrics
- category metrics
- progress bars
- SVG badges
- native image-coverage checkboxes
- per-item photo counts
- zero-photo queue
