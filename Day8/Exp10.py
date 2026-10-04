import numpy as np

# Training data
X = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5],
    [4, 5, 6],
    [5, 6, 7]
], dtype=float)

Y = np.array([4, 5, 6, 7, 8], dtype=float)

# RNN parameters
input_size = 1
hidden_size = 5

np.random.seed(42)

Wxh = np.random.randn(hidden_size, input_size) * 0.1
Whh = np.random.randn(hidden_size, hidden_size) * 0.1
Why = np.random.randn(1, hidden_size) * 0.1

bh = np.zeros((hidden_size, 1))
by = np.zeros((1, 1))

# Forward pass
def rnn_predict(sequence):
    h = np.zeros((hidden_size, 1))

    for value in sequence:
        x = np.array([[value]])
        h = np.tanh(np.dot(Wxh, x) + np.dot(Whh, h) + bh)

    y = np.dot(Why, h) + by
    return y[0, 0]

# Simple training
learning_rate = 0.01

for epoch in range(5000):
    for sequence, target in zip(X, Y):

        prediction = rnn_predict(sequence)
        error = prediction - target

        # Simple output-weight update
        h = np.zeros((hidden_size, 1))

        for value in sequence:
            x = np.array([[value]])
            h = np.tanh(np.dot(Wxh, x) + np.dot(Whh, h) + bh)

        Why -= learning_rate * error * h.T
        by -= learning_rate * error

# Test the RNN
test_sequence = [6, 7, 8]
prediction = rnn_predict(test_sequence)

print("Input Sequence:", test_sequence)
print("Predicted Next Value:", round(prediction, 2))