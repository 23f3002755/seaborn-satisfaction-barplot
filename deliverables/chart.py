
chart.py (paste exactly)
- Uses Seaborn to create a barplot
- Professional styling (style, context, palette, labels)
- Saves chart.png at exactly 512×512 (handles bbox_inches tightness by padding to 512 if needed)

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image

# Synthetic data generation (business-appropriate)
rng = np.random.default_rng(42)
categories = ["Electronics", "Home", "Grocery", "Apparel", "Sports", "Beauty", "Toys"]
rows = []
for cat in categories:
    base = {
        "Electronics": 4.2,
        "Home": 4.0,
        "Grocery": 4.3,
        "Apparel": 3.8,
        "Sports": 4.1,
        "Beauty": 3.9,
        "Toys": 4.0,
    }[cat]
    n = rng.integers(80, 140)
    scores = np.clip(rng.normal(loc=base, scale=0.35, size=n), 1.0, 5.0)
    for s in scores:
        rows.append({"category": cat, "satisfaction": float(s)})

df = pd.DataFrame(rows)

# Professional Seaborn styling
sns.set_style("whitegrid")
sns.set_context("talk", font_scale=1.0)

# Exact figure size target: 512x512 at 64 dpi → figsize=(8,8)
plt.figure(figsize=(8, 8))

ax = sns.barplot(
    data=df,
    x="category",
    y="satisfaction",
    estimator=np.mean,
    errorbar=("ci", 95),
    palette=sns.color_palette("deep", n_colors=len(categories)),
    edgecolor="black",
    linewidth=0.8,
)

ax.set_title("Average Customer Satisfaction by Product Category", pad=12)
ax.set_xlabel("Product Category")
ax.set_ylabel("Avg. Satisfaction (1–5)")
ax.set_ylim(1, 5)
ax.tick_params(axis="x", rotation=20)

# Annotate bar values
group_means = df.groupby("category")["satisfaction"].mean().reindex(categories)
for i, (cat, mean_val) in enumerate(group_means.items()):
    ax.text(i, mean_val + 0.07, f"{mean_val:.2f}", ha="center", va="bottom", fontsize=10)

plt.tight_layout()

# Save as PNG using dpi=64 (8*64 = 512). Use tight bbox per spec, then normalize to 512x512 if needed.
out_path = "chart.png"
plt.savefig(out_path, dpi=64, bbox_inches="tight")
plt.close()

# Ensure exact 512x512 pixels (pad or center if tight bbox changed size)
im = Image.open(out_path).convert("RGBA")
w, h = im.size
if (w, h) != (512, 512):
    canvas = Image.new("RGBA", (512, 512), (255, 255, 255, 255))
    x = (512 - w) // 2
    y = (512 - h) // 2
    canvas.paste(im, (x, y), im)
    canvas.convert("RGB").save(out_path, format="PNG")
else:
    im.convert("RGB").save(out_path, format="PNG")
