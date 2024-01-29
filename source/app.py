import os
import joblib
import pandas as pd
from flask import Flask, render_template, request

MODEL_NAME = "car_model.joblib"

# Initialize the app
app = Flask(__name__)

# Load the model when the application starts
model_path = os.path.join(os.path.dirname(__file__), 'static/model/' + MODEL_NAME)
model = joblib.load(model_path)

# Define app routes
# Index
@app.route('/')
def index():
    return render_template('index.html')

# Process user input and return response data
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST' and model:
        # Store the form input data by user
        hp = request.form.get('hp')
        wt = request.form.get('wt')
        # Prepare received data for test data according to your model
        data = {
            "hp": [hp],
            "wt": [wt]
        }
        test_data = pd.DataFrame(data)
        try:
            predict_mpg = model.predict(test_data)
            result = f"{predict_mpg[0]:.2f}"
            return f"Predicted : <strong>{result} MPG</strong>"
        except ValueError:
            return "<i class='text-danger'>Please Enter Correct Data!</i>"
    return "Failed to load model!"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)