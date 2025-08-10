<<<<<<< HEAD
<<<<<<< HEAD
# 🔥 Fire Weather Index (FWI) Prediction App

A lightweight Flask web application that predicts the **Fire Weather Index (FWI)** using a Ridge Regression model trained on Algerian forest fire data. Built with a clean, responsive UI using Bootstrap 5.

---

## 🚀 Features

- 🔢 Predicts FWI from user inputs:
  - Temperature (°C)
  - Relative Humidity (%)
  - Wind Speed (m/s)
  - Rainfall (mm)
  - FFMC (Fine Fuel Moisture Code)
  - DMC (Duff Moisture Code)
  - ISI (Initial Spread Index)
  - Classes (numeric category)
  - Region (numeric category)
- ⚙️ Preprocessing with Standard Scaler
- 📈 Ridge Regression model for predictions
- 💡 Clear and responsive UI with Bootstrap 5
- 🛡️ Basic input validation and error handling

---

## 🛠️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git https://github.com/Sure-Mohan-Kumar/Algerian-Forest-Fires.git
   cd fwi-prediction-app
   ```

2. **(Optional) Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure model files are present**:
   - Place `ridge.pkl` and `scaler.pkl` inside the `models/` directory.

---

## ▶️ Running the App

Start the Flask development server:
```bash
python app.py
```

Then, open your browser and go to:
```
http://127.0.0.1:5000/predictdata
```

Enter your weather data and click **"Predict FWI"**.

---

## 🧭 Project Structure

```
.
├── application.py                     # Flask application
├── models/
│   ├── ridge.pkl              # Trained Ridge Regression model
│   └── scaler.pkl             # Trained Standard Scaler
├── templates/
│   └── index.html
│   └── home.html
            # Frontend HTML with Bootstrap
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

---

## 🧪 Sample Input (for testing)

| Feature             | Value   |
|---------------------|---------|
| Temperature (°C)    | 25      |
| Relative Humidity (%) | 40    |
| Wind Speed (m/s)    | 4.5     |
| Rainfall (mm)       | 0.0     |
| FFMC                | 85.2    |
| DMC                 | 35.4    |
| ISI                 | 7.1     |
| Classes             | 1       |
| Region              | 2       |

---

## 📦 Dependencies

- Flask  
- numpy  
- pandas  
- scikit-learn  
=======
# Algerian-Forest-Fires
A simple app that predicts the Fire Weather Index (FWI) using an Algerian dataset. It applies Standard Scaler for preprocessing and Ridge Regression for prediction, helping with early fire risk assessment based on weather data.
>>>>>>> e5e7d7097db195aa82aa5b3d46f2ed5cca7fafc5
=======
# Algerian-Forest-Fires
A simple app that predicts the Fire Weather Index (FWI) using an Algerian dataset. It applies Standard Scaler for preprocessing and Ridge Regression for prediction, helping with early fire risk assessment based on weather data.
>>>>>>> 8deb98e47978a511306849fbd84db019a0a5897a
