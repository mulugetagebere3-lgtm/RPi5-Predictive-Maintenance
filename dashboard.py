import joblib
import pandas as pd
import time
import os

# ሞዴል ነምጽኣዮ
model = joblib.load('maintenance_model.pkl')

def predict_status(air, proc, speed, torque, wear):
    data = pd.DataFrame([[air, proc, speed, torque, wear]], 
                        columns=['Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]'])
    prediction = model.predict(data)
    return "⚠️ FAILURE" if prediction[0] == 1 else "✅ NORMAL"

# ንፈተነ ዝኸውን (Simulation)
test_scenarios = [
    [298.1, 308.6, 1551, 42.8, 0],   # Normal case
    [302.5, 312.1, 1300, 65.0, 200], # High Torque & Wear (Possible Failure)
    [295.0, 305.0, 2800, 10.0, 5]    # High Speed case
]

os.system('clear')
print("=== RASPBERRY PI 5: REAL-TIME MAINTENANCE MONITOR ===")
print("Status: Monitoring Machine Sensors...\n")

for scenario in test_scenarios:
    status = predict_status(*scenario)
    print(f"Sensors: {scenario} --> Result: {status}")
    time.sleep(2)

print("\nMonitoring Complete.")
