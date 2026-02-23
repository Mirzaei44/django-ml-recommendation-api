# Django ML Recommendation API

A Django REST API that serves a recommendation model (joblib).
Focus: service-layer design, validation, and error handling.

## What this project includes

- Django REST Framework endpoints
- Input validation with serializers
- Service layer separation (business logic outside views)
- ML model training script and saved model artifact (joblib)
- Prediction endpoint that uses the saved model
- Logging + custom global exception handling
- Pagination and optional filtering on list endpoint
- Basic automated API tests
- SQLite database (default)

## Tech stack

- Python
- Django
- Django REST Framework
- NumPy
- scikit-learn
- joblib
- SQLite

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate

Train the model (required)

Before using the recommendation endpoint, train and save the model artifact:

python recommendations/train_model.py

This will create:
	•	artifacts/reco_model.joblib

Note: the API will raise an error if the model artifact is missing.

Run the server

python manage.py runserver 8001

Base URL:
	•	http://127.0.0.1:8001/api/

API endpoints

Test endpoint

GET /api/test/

Response:

{"message": "API is working"}

Recommend

POST /api/recommend/

Request body:

{
  "age": 25,
  "category": "tech",
  "previous_score": 0.8
}

Response:

{
  "recommendation_score": 0.7334
}

What happens:
	•	input is validated
	•	the model predicts a score
	•	the request and prediction are stored in the database
	•	the score is returned

List stored requests

GET /api/requests/

Optional query params:
	•	category=tech
	•	page=2

Example:
	•	GET /api/requests/?category=tech

Run tests

python manage.py test

Notes

The training script uses synthetic data. The goal is to demonstrate a realistic serving pattern (train -> save artifact -> load -> predict), not to build a complex ML model.
