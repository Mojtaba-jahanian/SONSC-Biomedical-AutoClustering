import numpy as np
from sklearn.cluster import KMeans

def compute_isi(X, labels):
    k = len(np.unique(labels))
    centroids = np.array([X[labels == i].mean(axis=0) for i in range(k)])
    cohesion = np.sum([np.sum((X[labels == i] - centroids[i])**2) for i in range(k)]) / len(X)

    sep = 0
    for i in range(k):
        for j in range(i + 1, k):
            sep += np.linalg.norm(centroids[i] - centroids[j])**2
    separation = (2 / (k * (k - 1))) * sep

    isi = separation**2 / (cohesion + separation**2)
    return isi

def run_sonsc(X, max_k=10):
    isi_scores = []
    best_k = 2
    best_labels = None
    prev_isi = -1

    for k in range(2, max_k + 1):
        kmeans = KMeans(n_clusters=k, n_init=10, random_state=42)
        labels = kmeans.fit_predict(X)
        isi = compute_isi(X, labels)
        isi_scores.append(isi)

        if isi > prev_isi:
            prev_isi = isi
            best_k = k
            best_labels = labels
        else:
            break
    return best_labels, isi_scores, best_k
