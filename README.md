# RPi5 Predictive Maintenance System 🚀

This project demonstrates a **Predictive Maintenance** solution deployed on a **Raspberry Pi 5**. It uses Machine Learning to predict industrial machine failures before they occur.

## 🛠️ Project Overview
ኣብ Raspberry Pi 5 ዝሰርሕ ናይ ኢንዱስትሪ ማሽናት ብልሽት ኣቐዲሙ ዝፈልጥ (Predictive Maintenance) AI ፕሮጀክት እዩ። እዚ ሞዴል እዚ ዝተፈላለዩ ናይ ሰንሰር ዳታታት (mahcine parameters) ብምርኣይ፡ ሓደጋ ከጋጥም ይኽእል ድዩ ኣይክእልን ይንበ።

### Features:
- **Real-time Prediction:** Uses a Random Forest model.
- **Hardware:** Raspberry Pi 5.
- **Language:** Python (Scikit-learn, Pandas, Joblib).

## 📁 File Structure
- `train_maintenance.py`: Script used to train the ML model.
- `maintenance_model.pkl`: The saved brain (model) of our AI.
- `dashboard.py`: The main script to run the predictive dashboard.
- `ai4i2020.csv`: The dataset used for training and testing.

## 🚀 How to Run
1. Clone this repository.
2. Install dependencies: `pip install pandas scikit-learn joblib`
3. Run the dashboard: `python3 dashboard.py`

---
*Created by [Your Name]*
