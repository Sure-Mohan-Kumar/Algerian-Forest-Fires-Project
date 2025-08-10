import pickle
from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import os


app = Flask(__name__)

# Load your trained model and scaler
ridge_model = pickle.load(open('models/ridge.pkl', 'rb'))
standard_scaler = pickle.load(open('models/scaler.pkl', 'rb'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predictdata", methods=['GET', 'POST'])
def predict_datapoint():
    result = None
    error = None

    if request.method == 'POST':
        try:
            # Extract form input, convert to appropriate types
            Temperature = float(request.form.get('Temperature'))
            RH = float(request.form.get('RH'))
            Ws = float(request.form.get('Ws'))
            Rain = float(request.form.get('Rain'))
            FFMC = float(request.form.get('FFMC'))
            DMC = float(request.form.get('DMC'))
            ISI = float(request.form.get('ISI'))
            Classes = int(request.form.get('Classes'))
            Region = int(request.form.get('Region'))

            # Create DataFrame with the features in correct order
            features = pd.DataFrame([[
                Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region
            ]], columns=['Temperature', 'RH', 'Ws', 'Rain', 'FFMC', 'DMC', 'ISI', 'Classes', 'Region'])

            # Scale the features
            features_scaled = standard_scaler.transform(features)

            # Predict using the model
            prediction = ridge_model.predict(features_scaled)

            # Round the prediction to 3 decimals
            result = round(float(prediction[0]), 3)

        except Exception as e:
            error = f"Error: {str(e)}"

    return render_template('home.html', result=result, error=error)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Vercel's port or 5000 locally
    app.run(host="0.0.0.0", port=port)
