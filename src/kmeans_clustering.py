# src/kmeans_clustering.py
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def apply_kmeans(X: np.ndarray, n_clusters: int) -> tuple[np.ndarray, KMeans]:
    """
    Apply KMeans clustering to the data.
    
    Args:
        X (np.ndarray): Feature matrix for clustering.
        n_clusters (int): Number of clusters.
    
    Returns:
        tuple: Cluster labels and fitted KMeans model.
    """
    kmeans = KMeans(n_clusters=n_clusters, init='k-means++', random_state=42)
    y_kmeans = kmeans.fit_predict(X)
    return y_kmeans, kmeans

def plot_clusters(X: np.ndarray, y_kmeans: np.ndarray, save_path: str = 'outputs/cluster_plot.png') -> None:
    plt.figure(figsize=(8, 6))
    plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s=100, c='red', label='Cluster 1')
    plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s=100, c='blue', label='Cluster 2')
    plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s=100, c='green', label='Cluster 3')
    plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s=100, c='cyan', label='Cluster 4')
    plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s=100, c='magenta', label='Cluster 5')
    plt.title('Customer Segments')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.grid(True)
    plt.savefig(save_path)
    plt.close()