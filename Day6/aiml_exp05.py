import math
from collections import Counter
import matplotlib.pyplot as plt

# Training data
brightness = [40, 50, 60, 10, 70, 60, 25]
saturation = [20, 50, 90, 25, 70, 10, 80]
classes = ["Red", "Blue", "Blue", "Red", "Blue", "Red", "Blue"]

# Test data
test_brightness = 20
test_saturation = 35
k = 5

distances = []
for i in range(len(brightness)):
    distance = math.sqrt(
        (brightness[i] - test_brightness) ** 2
        + (saturation[i] - test_saturation) ** 2
    )
    distances.append(
        (distance, classes[i], brightness[i], saturation[i])
    )

distances.sort(key=lambda x: x[0])

print("Distances in ascending order:")
print("----------------------------")
for d, c, b, s in distances:
    print(
        "Brightness =",
        b,
        "Saturation =",
        s,
        "Class =",
        c,
        "Distance =",
        round(d, 2),
    )

nearest_neighbors = distances[:k]
print("\n", k, "Nearest Neighbours:")
print("----------------------------")
for d, c, b, s in nearest_neighbors:
    print(
        "Brightness =",
        b,
        "Saturation =",
        s,
        "Class =",
        c,
        "Distance =",
        round(d, 2),
    )

neighbor_classes = [x[1] for x in nearest_neighbors]
prediction = Counter(neighbor_classes).most_common(1)[0][0]

print("\nClass count:")
print(Counter(neighbor_classes))
print("\nPredicted Class =", prediction)

# Separate Red and Blue points
red_x = []
red_y = []
blue_x = []
blue_y = []

for i in range(len(brightness)):
    if classes[i] == "Red":
        red_x.append(brightness[i])
        red_y.append(saturation[i])
    else:
        blue_x.append(brightness[i])
        blue_y.append(saturation[i])

# Plot training data
plt.scatter(red_x, red_y, label="Red")
plt.scatter(blue_x, blue_y, label="Blue")

# Plot test point
plt.scatter(
    test_brightness,
    test_saturation,
    marker="*",
    s=250,
    label="Test Point",
)

# Label the test point
plt.annotate(
    "Test (20,35)",
    (test_brightness, test_saturation),
    xytext=(5, 5),
    textcoords="offset points",
)

plt.xlabel("Brightness")
plt.ylabel("Saturation")
plt.title("K-Nearest Neighbours (KNN)")
plt.legend()
plt.grid(True)
plt.show()