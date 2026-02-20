import os
import joblib
import numpy as np

# Path to the saved ML model artifact
MODEL_PATH = "artifacts/reco_model.joblib"

# Load model once at startup (if available)
MODEL = None

if os.path.exists(MODEL_PATH):
    MODEL = joblib.load(MODEL_PATH)


def calculate_recommendation_score(age: int, previous_score: float) -> float:
    # Ensure the model is loaded before prediction
    if MODEL is None:
        raise RuntimeError("Model artifact not found. Please train the model.")

    # Prepare input in the shape expected by the model
    X = np.array([[age, previous_score]])

    # Run prediction
    pred = MODEL.predict(X)[0]

    # Return a rounded float for cleaner API output
    return round(float(pred), 4)