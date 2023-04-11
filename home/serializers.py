from rest_framework import serializers
from .models import car_rating




class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = car_rating
        fields = '__all__'

# 