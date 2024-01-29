import os
import joblib
from flask import Flask

MODEL_NAME = "car_model.joblib"

# Initialize the app
app = Flask(__name__)

# Load the model when the application starts
model_path = os.path.join(os.path.dirname(__file__), 'static/model/' + MODEL_NAME)
model = joblib.load(model_path)

from source import routes
