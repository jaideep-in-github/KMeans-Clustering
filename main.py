#Created main driver script to execute full clustering pipeline

import os
import numpy as np  # Added import to fix NameError
from src.load_data import load_customer_data
from src.elbow_method import plot_elbow_method
from src.kmeans_clustering import apply_kmeans, plot_clusters
from src.silhouette_score import evaluate_silhouette
from src.pca_visualization import plot_pca_clusters

if __name__ == "__main__":
    os.makedirs("outputs", exist_ok=True)  # Create outputs folder if it doesn't exist

    # Load data
    df = load_customer_data("data/Mall_Customers.csv")
    X = np.array(df[["Annual Income (k$)", "Spending Score (1-100)"]].values)  # Ensure X is a NumPy array

    # Run clustering pipeline
    plot_elbow_method(X, save_path='outputs/elbow_plot.png')
    y_kmeans, kmeans = apply_kmeans(X, 5)
    plot_clusters(X, y_kmeans, save_path='outputs/cluster_plot.png')
    evaluate_silhouette(X, y_kmeans)
    plot_pca_clusters(X, y_kmeans, save_path='outputs/pca_plot.png')