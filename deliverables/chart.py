import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image

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

sns.set_style("whitegrid")
sns.set_context("talk", font_scale=1.0)

plt.figure(figsize=(8, 8), dpi=64)
ax = sns.barplot(
    data=df,
    x="category",
    y="satisfaction",
    estimator=np.mean,
