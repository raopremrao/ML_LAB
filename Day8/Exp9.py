import numpy as np

# Training data
X = np.array([0, 1, 2, 3, 4, 5], dtype=float)
Y = np.array([0, 1, 0, 1, 0, 1], dtype=float)

# Number of RBF neurons
centers = np.array([0, 2, 4])

# Spread of RBF
sigma = 1.0

# Radial Basis Function
def rbf(x, center, sigma):
    return np.exp(-((x - center) ** 2) / (2 * sigma ** 2))

# Create RBF hidden layer
G = np.zeros((len(X), len(centers)))

for i in range(len(X)):
    for j in range(len(centers)):
        G[i, j] = rbf(X[i], centers[j], sigma)

# Train output layer using pseudo-inverse
W = np.linalg.pinv(G).dot(Y)

# Calculate output
Y_pred = G.dot(W)

# Display results
print("RBF Hidden Layer Output:")
print(np.round(G, 3))

print("\nOutput Weights:")
print(np.round(W, 3))

print("\nActual Output : ", Y)
print("Predicted Output:", np.round(Y_pred, 3))