# 🥬🍎🌾 Food Image Asset Library

> **Master documentation and asset-tracking hub** for the local-commerce image library.

This repository is organized into three independent catalogs:

- 🥬 **Vegetables**
- 🍎 **Fruits**
- 🌾 **Grains, Cereals & Pulses**

The system is designed for an e-commerce application where a single catalog item can have **multiple photographs**.

---

# 🥬 Vegetables

The vegetable catalog currently contains **254 catalog entries**.

### Documentation

➡️ [Open Vegetable Image README](./vegetables/README.md)

Recommended vegetable image folders:

```text
vegetables/assets/images/
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

# 🍎 Fruits

The fruit catalog should track:

- common Indian fruits
- regional fruits
- seasonal fruits
- tropical fruits
- imported fruits
- berries
- citrus
- stone fruits
- melons
- dried/fresh distinctions where relevant

### Documentation

➡️ [Open Fruit Image README](./fruits/README.md)

Recommended folders:

```text
fruits/assets/images/
├── tropical/
├── citrus/
├── berries/
├── stone-fruits/
├── melons/
├── apples-pears/
├── grapes/
├── regional/
├── exotic/
└── seasonal/
```

---

# 🌾 Grains, Cereals & Pulses

The grains catalog should distinguish:

- whole grains
- cereals
- millets
- rice varieties
- wheat varieties
- maize/corn
- pulses
- dals
- legumes
- regional grains
- specialty grains

### Documentation

➡️ [Open Grains Image README](./grains/README.md)

Recommended folders:

```text
grains/assets/images/
├── rice/
├── wheat/
├── millets/
├── maize/
├── cereals/
├── pulses/
├── dals/
├── legumes/
├── regional/
└── specialty/
```

---

# 🏷️ Status Model

Each catalog item can eventually have:

```text
⚪ NOT STARTED
🟨 IMAGE FOUND
🟦 MULTIPLE IMAGES
🟩 VERIFIED
```

Suggested detailed state:

| Status | Condition |
|---|---|
| ⚪ Missing | 0 photos |
| 🟨 Covered | ≥1 photo |
| 🟦 Rich | ≥3 photos |
| 🟩 Verified | Manually reviewed |
| 🔴 Needs Review | Image exists but has a problem |

---

## 📊 Master Dashboard

| Metric | Meaning |
|---|---|
| 🗂️ Catalog items | Number of unique food/product entries defined |
| 🖼️ Items with images | Unique items that have at least one image |
| 📸 Total photos | Every image file across all catalogs |
| 📈 Coverage | `% of unique catalog items having ≥1 image` |
| ⚪ Zero-photo items | Items still requiring an image |
| 📸 Avg photos/item | Total photos ÷ unique catalog items |
| ✅ Verified items | Items manually reviewed for correctness/license/quality |
| 🏷️ Priority coverage | Coverage of P0/P1/P2/P3 items |
| 📦 Category coverage | Coverage broken down by category |
| 🔗 Source coverage | Items with a recorded source/license |
| 🧹 Quality review | Images passing visual/technical review |

> **Important:** The dashboard should be generated automatically by the repository's inventory script. Do not manually maintain calculated numbers.

---

# 🚦 Definition of Done

A product is considered **image-covered** when:

```text
≥ 1 correctly mapped image
```

A product is considered **richly covered** when:

```text
≥ 3 useful images
```

A product is considered **verified** when:

```text
Correct product
        +
Good quality
        +
License/source checked
        +
Correct catalog mapping
```

---

## 🎯 Core Metrics

### 1. Unique-item coverage

This is the primary completion metric.

```text
Items with ≥1 photo
──────────────────── × 100
Total unique items
```

Example:

```text
127 / 254 unique items
██████████░░░░░░░░░░ 50.0%
```

### 2. Total photo count

Every image is counted.

If Potato has:

```text
potato.jpg
potato-02.jpg
potato-03.jpg
potato-04.jpg
```

then:

```text
Unique items covered = 1
Total photos         = 4
```

### 3. Average photos per item

```text
Total photos / Total unique items
```

This measures how rich the image collection is.

### 4. Category coverage

Each category receives its own:

- unique item count
- items with ≥1 photo
- total photo count
- coverage %
- average photos/item
- zero-photo count
- status

### 5. Priority coverage

Recommended priority levels:

| Priority | Meaning |
|---|---|
| 🔴 P0 | Everyday / highest-demand products |
| 🟠 P1 | High-frequency products |
| 🟡 P2 | Regional / medium-frequency products |
| 🟢 P3 | Long-tail / exotic / premium products |

### 6. Verification

Image existence is **not** the same as image verification.

Verification should cover:

- correct product
- correct variety
- good resolution
- clean composition
- no unwanted watermark
- suitable commercial license
- source recorded
- correct filename
- correct catalog mapping
- image works in the application

---

# 🗺️ Repository Structure

```text
food-image-library/
│
├── README.md
│
├── vegetables/
│   ├── README.md
│   ├── data/
│   ├── assets/
│   │   └── images/
│   └── scripts/
│
├── fruits/
│   ├── README.md
│   ├── data/
│   ├── assets/
│   │   └── images/
│   └── scripts/
│
├── grains/
│   ├── README.md
│   ├── data/
│   ├── assets/
│   │   └── images/
│   └── scripts/
│
└── scripts/
    └── update_all_metrics.py
```

---

# 📸 Multiple Images Per Product

Multiple images are encouraged.

Recommended naming:

```text
potato.jpg
potato-02.jpg
potato-03.jpg

apple.jpg
apple-02.jpg
apple-03.jpg

basmati-rice.jpg
basmati-rice-02.jpg
```

The inventory system groups these under the same unique catalog item.

### Why multiple photos?

They can represent:

- front/product view
- alternate angle
- close-up
- whole item
- cut/open item
- packaged version
- size/variety difference
- marketplace thumbnail
- application-specific crop

---

# 🔐 Licensing & Source Tracking

For a commercial application, image licensing should be tracked separately from image availability.

Recommended metadata:

| Field | Example |
|---|---|
| Product ID | VEG-0001 |
| Product | Potato |
| Image | potato.jpg |
| Source | Openverse |
| Creator | Example Creator |
| License | CC BY 4.0 |
| Source URL | Recorded in metadata |
| Commercial use | Yes |
| Attribution required | Yes |
| Verified | Yes |

**Never assume that an image found online is commercially reusable.**

---

# 🧭 Long-Term Goal

Build a reusable, commercially suitable food-image dataset for the local-commerce application covering:

```text
🥬 Vegetables
🍎 Fruits
🌾 Grains
🫘 Pulses & legumes
🌿 Herbs
🥜 Nuts & seeds
🧂 Spices
🥛 Dairy
🧃 Packaged foods
```

The current documentation focuses on **vegetables, fruits and grains** and can be extended using the same tracking model.

---

# 🤖 Automation

The repository should automatically:

1. Scan image folders.
2. Match image filenames to catalog IDs.
3. Count total photos.
4. Count unique products with ≥1 image.
5. Calculate coverage.
6. Calculate category metrics.
7. Calculate priority metrics.
8. Calculate average photos/item.
9. Identify zero-photo items.
10. Generate README dashboards.
11. Generate SVG badges.
12. Update checkboxes.
13. Preserve manual verification fields.

GitHub Actions can run this whenever images or catalog files change.

---

## 📌 Maintenance Rule

**Catalog data is the source of truth.**

**Images are assets.**

**Generated dashboards are derived data.**

Do not manually edit calculated metrics when automation is available.
