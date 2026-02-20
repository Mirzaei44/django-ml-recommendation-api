from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import RecommendationRequest


class RecommendationAPITestCase(APITestCase):

    def test_recommend_success(self):
        url = reverse("recommend")
        data = {
            "age": 25,
            "category": "tech",
            "previous_score": 0.8
        }

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("recommendation_score", response.data)

    def test_recommend_invalid_input(self):
        url = reverse("recommend")
        data = {
            "age": 25,
            "category": "tech",
            "previous_score": "invalid"
        }

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_requests(self):
        RecommendationRequest.objects.create(
            age=30,
            category="tech",
            previous_score=0.5,
            recommendation_score=0.6
        )

        url = reverse("list_requests")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("results", response.data)