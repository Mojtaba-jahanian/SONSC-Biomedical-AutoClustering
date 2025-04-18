import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import seaborn as sns
import matplotlib.pyplot as plt

from sonsc import run_sonsc
from utils import plot_isi

# Example data
X = np.random.rand(100, 20)

# Normalize
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Run SONSC
labels, isi_scores, best_k = run_sonsc(X_scaled)
print(f"✅ Best k found by SONSC: {best_k}")

# Plot ISI
plot_isi(isi_scores, best_k)

# t-SNE visualization
X_tsne = TSNE(n_components=2, random_state=42).fit_transform(X_scaled)
plt.figure(figsize=(6, 5))
sns.scatterplot(x=X_tsne[:, 0], y=X_tsne[:, 1], hue=labels, palette='tab10')
plt.title("t-SNE Projection of SONSC Clusters")
plt.xlabel("t-SNE-1")
plt.ylabel("t-SNE-2")
plt.legend(title="Cluster")
plt.grid(True)
plt.tight_layout()
plt.savefig("../results/tsne_plot.png")
plt.show()
