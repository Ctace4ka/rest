from django.contrib import admin
from django.urls import path
from myapp.views import PointList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('points/', PointList.as_view(), name='point-list'),
]
