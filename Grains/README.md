# 🌾 Grains, Cereals & Pulses Image Library

> Dedicated tracking document for grains, cereals, millets, pulses and dals.

## 📊 Dashboard

| Metric | Value |
|---|---:|
| 🌾 Unique catalog items | **Auto-generated from catalog** |
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

# 🌾 Recommended Grain Categories

## 🍚 Rice

```text
Basmati Rice
Sona Masuri
Brown Rice
Parboiled Rice
White Rice
Red Rice
Black Rice
Brown Basmati
Jeera Rice varieties
Regional rice varieties
```

## 🌾 Wheat

```text
Whole Wheat
Wheat Grain
Durum Wheat
Emmer Wheat
Khapli Wheat
Sharbati Wheat
```

## 🌱 Millets

```text
Ragi / Finger Millet
Bajra / Pearl Millet
Jowar / Sorghum
Foxtail Millet
Little Millet
Kodo Millet
Barnyard Millet
Proso Millet
Browntop Millet
```

## 🌽 Maize & Corn

```text
Yellow Maize
White Maize
Corn Grain
Popcorn
Baby Corn
```

## 🫘 Pulses

```text
Chickpeas / Chana
Kabuli Chana
Black Chickpeas / Kala Chana
Pigeon Pea / Toor
Green Gram / Moong
Black Gram / Urad
Red Lentil / Masoor
Kidney Beans / Rajma
Black-eyed Peas / Lobia
Moth Beans
Horse Gram
Field Peas
Cowpea
```

## 🥣 Dals

Track whole and split forms separately where relevant:

```text
Toor Dal
Moong Dal
Moong Whole
Urad Dal
Urad Whole
Masoor Dal
Masoor Whole
Chana Dal
Chana Whole
```

## 🌿 Regional & Specialty Grains

Include regionally important grains and traditional varieties.

---

# 📈 Progress Rules

Each catalog item gets:

```text
0 photos → ❌ uncovered
1+ photos → ✅ covered
3+ photos → ⭐ rich image coverage
```

Additional photographs increase the total photo metric without creating duplicate catalog items.

---

# 📸 Naming

```text
basmati-rice.jpg
basmati-rice-02.jpg
basmati-rice-03.jpg

ragi.jpg
ragi-02.jpg
```

Recommended folders:

```text
assets/images/grains/
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

# 🔐 Verification

- [ ] Correct grain
- [ ] Correct variety
- [ ] Whole/split state correctly represented
- [ ] Good resolution
- [ ] No unwanted watermark
- [ ] Commercial-use license checked
- [ ] Source recorded
- [ ] Correct filename
- [ ] Correct catalog mapping
- [ ] Application tested

---

# 🤖 Automation

Use the same inventory architecture as vegetables and fruits.

The system should automatically calculate:

- unique items
- items with images
- total photos
- category coverage
- average photos/item
- zero-photo queue
- priority coverage
- generated badges
- README dashboard
