import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# 1. ነቲ ሓድሽ ዳታ ነንብቦ
print("ነቲ ሓድሽ Predictive Maintenance ዳታ ነንብቦ ኣለና...")
df = pd.read_csv('ai4i2020.csv')

# 2. ዘየድልዩ ዓንድታት ምእላይ
# እዞም ስዒቦም ዘለዉ ንትንቢት ኣገደስቲ ዝበሃሉ እዮም
features = ['Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]']
X = df[features]
y = df['Machine failure']

# 3. ንስልጠናን ንፈተነን ምምቓል
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. ሞዴል ምስልጣን
print("ሞዴል ይስልጥን ኣሎ...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. ውጽኢት ምርኣይ
y_pred = model.predict(X_test)
print(f"\nእዚ ሓድሽ Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
print("\n--- ዝርዝር ጸብጻብ ---")
print(classification_report(y_test, y_pred))

# 6. ነቲ ሞዴል ዕቀቦ
joblib.dump(model, 'maintenance_model.pkl')
print("\nእቲ ሓድሽ ሞዴል 'maintenance_model.pkl' ተባሂሉ ተዓቂቡ ኣሎ!")
