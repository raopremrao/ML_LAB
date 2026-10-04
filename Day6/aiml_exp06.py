import matplotlib.pyplot as plt
import numpy as np

s1 = np.array([0, 1])
s2 = np.array([4, 1])
s3 = np.array([4, -1])

A = np.array([[2, 5, 5], [5, 18, 16], [5, 16, 18]])

B = np.array([-1, 1, 1])
alpha = np.linalg.solve(A, B)
a1, a2, a3 = alpha

print("alpha1 =", a1)
print("alpha2 =", a2)
print("alpha3 =", a3)

w = a1 * s1 + a2 * s2 + a3 * s3
print("\nw =", w)

positive = np.array([[4, 1], [4, -1], [6, 0]])

negative = np.array([[1, 0], [0, 1], [6, -1]])

plt.figure(figsize=(8, 6))

plt.scatter(
    positive[:, 0],
    positive[:, 1],
    marker="o",
    s=100,
    label="+ve class",
)

plt.scatter(
    negative[:, 0],
    negative[:, 1],
    marker="x",
    s=100,
    label="-ve class",
)

b = 0
x = np.linspace(-1, 7, 200)

if w[1] != 0:
    y = -(w[0] * x + b) / w[1]
    plt.plot(x, y, label="Decision boundary")

    y_upper = -(w[0] * x + b - 1) / w[1]
    y_lower = -(w[0] * x + b + 1) / w[1]

    plt.plot(x, y_upper, "--", label="Margin")
    plt.plot(x, y_lower, "--")

plt.scatter(
    [s1[0], s2[0], s3[0]],
    [s1[1], s2[1], s3[1]],
    s=250,
    facecolors="none",
    edgecolors="black",
    linewidths=2,
    label="Support vectors",
)

plt.axhline(0, linewidth=0.8)
plt.axvline(0, linewidth=0.8)
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Linear SVM")
plt.grid(True)
plt.legend()
plt.show()