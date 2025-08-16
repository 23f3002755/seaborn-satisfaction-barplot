import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image

# Minimal synthetic data (business-appropriate averages)
df = pd.DataFrame({
    "category": ["Electronics", "Home", "Grocery", "Apparel", "Sports", "Beauty", "Toys"],
    "satisfaction": [4.2, 4.0, 4.3, 3.8, 4.1, 3.9, 4.0]
})

sns.set_style("whitegrid")
sns.set_context("talk", font_scale=1.0)

# 512x512 target via 8x8 inches at 64 dpi
plt.figure(figsize=(8, 8), dpi=64)
ax = sns.barplot(
    data=df,
    x="category",
    y="satisfaction",
    palette="deep",
    edgecolor="black",
    linewidth=0.8,
    ci=None
)

ax.set_title("Average Customer Satisfaction by Product Category", pad=12)
ax.set_xlabel("Product Category")
ax.set_ylabel("Avg. Satisfaction (1-5)")
ax.set_ylim(1, 5)
ax.tick_params(axis="x", rotation=20)
plt.tight_layout(pad=1.0)

out_path = "deliverables/chart.png"
plt.savefig(out_path, dpi=64)
plt.close()

# Enforce exact 512x512 pixels
im = Image.open(out_path).convert("RGB")
if im.size != (512, 512):
    im = im.resize((512, 512), Image.LANCZOS)
im.save(out_path, format="PNG")
