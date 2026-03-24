from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile

        fields = [
            'id',
            'user',
            'bio',
            'location',
            'travel_style',
            'pace',
            'accommodation_preference',
            'budget_level',
            'adventure_level',
            'social_level'
        ]