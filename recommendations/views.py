import logging

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from .models import RecommendationRequest
from .serializers import (
    RecommendInputSerializer,
    RecommendationRequestSerializer,
)
from .services import calculate_recommendation_score

# App-level logger for request and error tracking
logger = logging.getLogger("recommendations")


@api_view(['GET'])
def test_api(request):
    # Simple health check endpoint
    return Response({"message": "API is working"})


@api_view(['POST'])
def recommend(request):
    # Validate incoming request data
    serializer = RecommendInputSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Extract validated fields
    data = serializer.validated_data
    age = data["age"]
    category = data["category"]
    previous_score = data["previous_score"]

    # Call service layer to compute recommendation score
    recommendation_score = calculate_recommendation_score(
        age=age,
        previous_score=previous_score
    )

    # Store request and prediction in database
    RecommendationRequest.objects.create(
        age=age,
        category=category,
        previous_score=previous_score,
        recommendation_score=recommendation_score
    )

    # Return API response
    return Response(
        {"recommendation_score": recommendation_score},
        status=status.HTTP_201_CREATED
    )


class DefaultPagination(PageNumberPagination):
    # Limit number of records per page
    page_size = 10


@api_view(['GET'])
def list_requests(request):
    # Base queryset ordered by newest first
    qs = RecommendationRequest.objects.all().order_by("-created_at")

    # Optional filtering by category
    category = request.query_params.get("category")
    if category:
        qs = qs.filter(category__iexact=category)

    # Apply pagination
    paginator = DefaultPagination()
    page = paginator.paginate_queryset(qs, request)

    serializer = RecommendationRequestSerializer(page, many=True)

    # Return paginated response
    return paginator.get_paginated_response(serializer.data)