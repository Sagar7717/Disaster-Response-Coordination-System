# ai_safety_model.py
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Example disaster data (features: weather, population density, alert level, resources available)
data = np.array([
    [1, 500, 3, 10],  # Safe
    [2, 800, 4, 7],   # At Risk
    [3, 1200, 5, 5],  # Critical
    [1, 300, 2, 12],  # Safe
    [2, 700, 4, 6],   # At Risk
])

labels = np.array([0, 1, 2, 0, 1])  # 0: Safe, 1: At Risk, 2: Critical

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate the model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save the model
joblib.dump(model, 'disaster_impact_model.pkl')

# Function to predict disaster impact level
def predict_impact(features):
    loaded_model = joblib.load('disaster_impact_model.pkl')
    prediction = loaded_model.predict([features])
    levels = {0: 'Safe', 1: 'At Risk', 2: 'Critical'}
    return levels[prediction[0]]

# Example prediction
example_features = [2, 1000, 4, 8]  # Input example
impact_level = predict_impact(example_features)
print(f"Predicted Impact Level: {impact_level}")
