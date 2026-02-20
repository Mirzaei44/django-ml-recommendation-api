from rest_framework import serializers


class RecommendInputSerializer(serializers.Serializer):
    # Input validation for the recommendation endpoint
    age = serializers.IntegerField(min_value=0, max_value=120)
    category = serializers.CharField(max_length=100)
    previous_score = serializers.FloatField(min_value=0, max_value=1)


from .models import RecommendationRequest


class RecommendationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        # Serialize database model for list endpoint responses
        model = RecommendationRequest
        fields = [
            "id",
            "age",
            "category",
            "previous_score",
            "recommendation_score",
            "created_at",
        ]