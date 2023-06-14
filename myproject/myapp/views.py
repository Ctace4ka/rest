from rest_framework import generics
from myapp.models import Point
from myapp.serializers import PointSerializer

class PointList(generics.ListCreateAPIView):
    queryset = Point.objects.all()
    serializer_class = PointSerializer
