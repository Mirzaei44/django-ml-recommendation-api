Django ML Recommendation API

A Django REST API that serves a machine learning recommendation model.

The project demonstrates how an ML model can be trained, saved as an artifact, and exposed through a production-style API with proper validation, logging, and error handling.

The focus is not on building a complex model, but on showing a realistic **ML serving pattern** within a backend system.

---

## Architecture Overview

The system follows a simple ML serving workflow:

train model → save artifact → load model in API → predict → store request

1. A training script generates synthetic training data and trains a model.
2. The trained model is saved as a `joblib` artifact.
3. The Django API loads the artifact.
4. Clients send prediction requests.
5. The prediction result is returned and stored for later inspection.

---

## Features

- Django REST Framework API endpoints
- Input validation with serializers
- Service-layer design (business logic separated from views)
- ML model training script
- Model artifact loading using `joblib`
- Prediction endpoint
- Request logging and global exception handling
- Pagination and filtering on stored requests
- Basic automated API tests

---

## Tech Stack

- Python
- Django
- Django REST Framework
- NumPy
- scikit-learn
- joblib
- SQLite

---

## Setup

Create virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate


⸻

Train the Model

Before using the recommendation endpoint, you must train the model and create the artifact:

python recommendations/train_model.py

This will generate:

artifacts/reco_model.joblib

If the artifact is missing, the API will return an error when prediction is requested.

⸻

Run the Server

python manage.py runserver 8001

Base API URL:

http://127.0.0.1:8001/api/


⸻

API Endpoints

Test Endpoint

GET /api/test/

Response:

{
  "message": "API is working"
}


⸻

Recommendation Endpoint

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

What happens internally:
	1.	Request input is validated
	2.	The model generates a prediction score
	3.	The request and result are stored in the database
	4.	The score is returned to the client

⸻

Stored Requests

GET /api/requests/

Optional query parameters:

category=tech
page=2

Example:

GET /api/requests/?category=tech


⸻

Run Tests

python manage.py test


⸻

Notes

The training script uses synthetic data.
The goal of this project is to demonstrate a realistic ML serving workflow:

train → save artifact → load → predict

rather than to build a complex production model.
