from source import app, model
import pandas as pd
from flask import render_template, request

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
