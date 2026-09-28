# Multilayer Perceptron (MLP) Neural Network

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load Iris dataset
iris = load_iris()

# Features and target
X = iris.data
y = iris.target

# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create MLP neural network
model = MLPClassifier(
    hidden_layer_sizes=(10,),
    activation='relu',
    solver='adam',
    max_iter=1000,
    random_state=42
)

# Train the neural network
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Display actual and predicted values
print("Actual Values:")
print(y_test)

print("\nPredicted Values:")
print(y_pred)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy:", accuracy)

# Display confusion matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Display classification report
print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    target_names=iris.target_names
))

# Predict a new sample
new_sample = [[5.1, 3.5, 1.4, 0.2]]
prediction = model.predict(new_sample)

print("\nPrediction for New Sample:")
print(iris.target_names[prediction[0]])