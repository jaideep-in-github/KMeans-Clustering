# src/pca_visualization.py
# src/pca_visualization.py
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def plot_pca_clusters(X: np.ndarray, labels: np.ndarray, save_path: str = 'outputs/pca_plot.png') -> None:
    pca = PCA(n_components=2)
    components = pca.fit_transform(X)
    plt.figure(figsize=(8, 6))
    plt.scatter(components[:, 0], components[:, 1], c=labels, cmap='Set1', s=50)
    plt.title("PCA - Cluster Visualization")
    plt.xlabel("PC 1")
    plt.ylabel("PC 2")
    plt.grid(True)
    plt.savefig(save_path)
    plt.close()