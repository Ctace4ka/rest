from rest_framework import serializers
from myapp.models import Point

class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = ['id', 'name', 'audioUrl', 'latitude', 'longitude', 'created_at', 'updated_at', 'picture']