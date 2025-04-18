import matplotlib.pyplot as plt

def plot_isi(isi_scores, best_k):
    ks = list(range(2, 2 + len(isi_scores)))
    plt.figure(figsize=(8, 4))
    plt.plot(ks, isi_scores, marker='o', color='darkblue')
    plt.axvline(best_k, color='red', linestyle='--', label=f'Best k = {best_k}')
    plt.xlabel("k")
    plt.ylabel("ISI")
    plt.title("ISI Score vs. Number of Clusters")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("../results/isi_vs_k.png")
    plt.show()
