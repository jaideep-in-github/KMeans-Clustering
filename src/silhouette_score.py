# src/silhouette_score.py

import numpy as np
from sklearn.metrics import silhouette_score

def evaluate_silhouette(X: np.ndarray, labels: np.ndarray) -> None:
    score = silhouette_score(X, labels)
    print(f"Silhouette Score: {score:.4f}")