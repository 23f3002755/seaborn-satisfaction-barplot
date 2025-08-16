import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image

# Synthetic data generation (customer satisfaction by category)
rng = np.random.default_rng(42)
categories = ["Electronics", "Home", "Grocery", "Apparel", "Sports", "Beauty", "Toys"]

rows = []
base_means = {
    "Electronics": 4.2,
    "Home": 4.0,
    "Grocery": 4.3,
    "Apparel": 3.8,
    "Sports": 4.1,
    "Beauty": 3.9,
    "Toys": 4.0,
}
for cat in categories:
    n = int(rng.integers(80, 140))
    mu = base_means[cat]
    scores = np.clip(rng.normal(loc=mu, scale=0.35, size=n), 1.0, 5.0)
    rows += [{"category": cat, "satisfaction": float(s)} for s in scores]

df = pd.DataFrame(rows)

# Professional Seaborn styling
sns.set_style("whitegrid")
sns.set_context("talk", font_scale=1.0)

# Exact 512x512 target: figsize (8,8) at dpi=64
plt.figure(figsize=(8, 8), dpi=64)

ax = sns.barplot(
    data=df,
    x="category",
    y="satisfaction",
    estimator=np.mean,
    palette=sns.color_palette("deep", n_colors=len(categories)),
    edgecolor="black",
    linewidth=0.8,
)

ax.set_title("Average Customer Satisfaction by Product Category", pad=12)
ax.set_xlabel("Product Category")
ax.set_ylabel("Avg. Satisfaction (1-5)")
ax.set_ylim(1, 5)
ax.tick_params(axis="x", rotation=20)

# Annotate bar means
means = df.groupby("category")["satisfaction"].mean().reindex(categories)
for i, (cat, val) in enumerate(means.items()):
    ax.text(i, val + 0.07, f"{val:.2f}", ha="center", va="bottom", fontsize=10)

plt.tight_layout(pad=1.0)

out_path = "chart.png"
plt.savefig(out_path, dpi=64)
plt.close()

# Enforce exactly 512x512 pixels (in case tight layout shifts size)
im = Image.open(out_path).convert("RGB")
if im.size != (512, 512):
    im = im.resize((512, 512), Image.LANCZOS)
im.save(out_path, format="PNG")
