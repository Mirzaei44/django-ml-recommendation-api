import os
import joblib
import numpy as np
from sklearn.linear_model import LinearRegression


def train_and_save(model_path: str):
    # Create simple synthetic data for training
    # Inputs: age and previous_score
    # Target: recommendation_score
    np.random.seed(42)

    ages = np.random.randint(18, 65, size=300)
    prev_scores = np.random.rand(300)

    # Simple linear relationship + small noise
    y = 0.6 * prev_scores + 0.01 * ages + np.random.normal(0, 0.02, size=300)

    # Combine features into model input shape
    X = np.column_stack([ages, prev_scores])

    # Train a basic linear regression model
    model = LinearRegression()
    model.fit(X, y)

    # Ensure the artifacts directory exists
    os.makedirs(os.path.dirname(model_path), exist_ok=True)

    # Save the trained model to disk
    joblib.dump(model, model_path)

    print(f"Model saved to: {model_path}")


if __name__ == "__main__":
    # Run training manually when executing this file
    train_and_save("artifacts/reco_model.joblib")