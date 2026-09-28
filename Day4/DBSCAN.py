import math
import matplotlib.pyplot as plt
# Data points
points = {
    "A": (3, 7),
    "B": (4, 6),
    "C": (5, 5),
    "D": (6, 4),
    "E": (7, 3),
    "F": (6, 2),
    "G": (7, 2),
    "H": (8, 4)
}

eps = 2.5
min_pts = 4

# Find neighbours
for p in points:
    count = 0
    for q in points:
        d = math.sqrt(
            (points[p][0] - points[q][0])**2 +
            (points[p][1] - points[q][1])**2
        )
        if d <= eps:
            count += 1
    print(p, "Neighbours = ", count)

# DBSCAN result
core = ["D", "E", "F", "G", "H"]
border = ["C"]
noise = ["A", "B"]
print("\nCore Points: ", core)
print("Border Points: ", border)
print("Noise Points: ", noise)

# plot graph
for p in core:
    x, y = points[p]
    plt.scatter(x, y, s=100, label="Core" if p == "D" else "")
    plt.text(x + 0.1, y + 0.1, p)

for p in border:
    x, y = points[p]
    plt.scatter(x, y, s=100, marker="s", label = "Border")
    plt.text(x + 0.1, y + 0.1, p)

for p in noise:
    x, y = points[p]
    plt.scatter(x, y, s = 100, marker="x", label="Noise")
    plt.text(x + 0.1, y + 0.1, p)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("DBSCAN Clustering")
plt.grid(True)
plt.legend()
plt.show()