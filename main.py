from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

centers = [(50, 50)]
cluster_std = [2]

X, y = make_blobs(n_samples=100, cluster_std=cluster_std, centers=centers, n_features=1, random_state=1)

plt.scatter(X[y == 0, 0], X[y == 0, 1], color="red", s=10, label="Cluster1")

plt.show()