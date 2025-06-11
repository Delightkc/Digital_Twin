import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load the sensor data
df = pd.read_csv("room_data.csv")

# Convert timestamp column to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Extract minute as a feature
df['minute'] = df['timestamp'].dt.minute

# Define input features and target
X = df[['minute']]       # Feature: minute
y = df['temperature']    # Target: temperature

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict temperature at minute 45 (as a DataFrame to avoid warning)
future_minute = pd.DataFrame({'minute': [45]})
future_temp = model.predict(future_minute)
print(f"📈 Predicted Temperature at minute 45: {future_temp[0]:.2f}°C")

# Optional: Plot predicted vs. actual
y_pred = model.predict(X_test)

plt.figure(figsize=(8, 5))
plt.scatter(X_test, y_test, label='Actual', color='blue')
plt.scatter(X_test, y_pred, label='Predicted', color='red', marker='x')
plt.title("Actual vs. Predicted Temperatures")
plt.xlabel("Minute")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
