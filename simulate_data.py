# simulate_data.py
import random
import pandas as pd

def simulate_data(n=100):
    base_time = pd.Timestamp.now().floor('min')
    data = []
    for i in range(n):
        timestamp = base_time + pd.Timedelta(minutes=i)
        entry = {
            'timestamp': timestamp,
            'temperature': round(random.uniform(20, 30), 2),
            'humidity': round(random.uniform(30, 60), 2)
        }
        data.append(entry)
    df = pd.DataFrame(data)
    df.to_csv("room_data.csv", index=False)
    print("✅ Sensor data generated!")

if __name__ == "__main__":
    simulate_data()
