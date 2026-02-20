# Django ML Recommendation API

Small production style Django REST API that demonstrates:
- REST endpoints with DRF
- Input validation with serializers
- Service layer separation
- ML model training + saved artifact (joblib) + prediction
- Logging + global exception handling
- Pagination + filtering
- Basic API tests

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 8001