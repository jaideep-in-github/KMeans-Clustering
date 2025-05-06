# src/elbow_method.py

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def plot_elbow_method(X: np.ndarray, save_path: str = 'outputs/elbow_plot.png') -> None:
    wcss = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)
    plt.figure(figsize=(8, 6))
    plt.plot(range(1, 11), wcss, marker='o')
    plt.title('Elbow Method')
    plt.xlabel('Number of Clusters')
    plt.ylabel('WCSS')
    plt.grid(True)
    plt.savefig(save_path)
    plt.close()