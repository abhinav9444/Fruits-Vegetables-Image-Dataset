# 🍎 Fruit Image Library

> Dedicated tracking document for fruit image assets.

## 📊 Dashboard

| Metric | Value |
|---|---:|
| 🍎 Unique fruit items | **Auto-generated from catalog** |
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

# 🍎 Recommended Fruit Categories

## 🍌 Tropical

Examples:

```text
Banana
Plantain
Mango
Papaya
Pineapple
Jackfruit
Guava
Coconut
Dragon Fruit
Passion Fruit
```

## 🍊 Citrus

```text
Orange
Sweet Lime / Mosambi
Lemon
Lime
Grapefruit
Pomelo
Mandarin
Kinnow
```

## 🍓 Berries

```text
Strawberry
Blueberry
Raspberry
Blackberry
Mulberry
Cranberry
Indian Gooseberry / Amla
```

## 🍑 Stone Fruits

```text
Peach
Plum
Apricot
Cherry
Nectarine
```

## 🍎 Apples & Pears

```text
Apple
Green Apple
Red Apple
Fuji Apple
Gala Apple
Granny Smith
Pear
Asian Pear
```

## 🍉 Melons

```text
Watermelon
Muskmelon
Cantaloupe
Honeydew
```

## 🍇 Grapes

```text
Green Grapes
Black Grapes
Red Grapes
Seedless Grapes
Thompson Seedless
```

## 🌾 Regional & Seasonal Indian Fruits

Include regional fruits that are useful to a local-commerce catalog, such as:

```text
Jamun
Ber
Bael
Custard Apple / Sitaphal
Wood Apple
Karonda
Phalsa
Tadgola
Kokum
Star Fruit / Kamrakh
Langsat
Lychee
```

---

# 📈 Progress Rules

A fruit receives **1 unique-item coverage point** when it has ≥1 image.

Every additional photograph increases:

```text
Total photos
Average photos/item
Category photo count
```

Example:

```text
Mango
mango.jpg
mango-02.jpg
mango-03.jpg
```

Results:

```text
Unique fruits covered: 1
Total photos: 3
```

---

# 📸 Naming

```text
mango.jpg
mango-02.jpg
mango-03.jpg

green-apple.jpg
green-apple-02.jpg
```

Recommended folders:

```text
assets/images/fruits/
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

# 🔐 Verification

- [ ] Correct fruit
- [ ] Correct variety
- [ ] Good quality
- [ ] No unwanted watermark
- [ ] Commercial-use license checked
- [ ] Source recorded
- [ ] Correct filename
- [ ] Correct catalog mapping
- [ ] Application tested

---

# 🤖 Automation

The fruit catalog should use the same inventory engine as vegetables:

```text
Catalog CSV
    ↓
Image folder
    ↓
Filename matching
    ↓
Unique-item count
    ↓
Total-photo count
    ↓
Category metrics
    ↓
README + badges
```
