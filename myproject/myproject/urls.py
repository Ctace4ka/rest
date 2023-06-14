from django.contrib import admin
from django.urls import path
from myapp.views import PointList
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('points/', PointList.as_view(), name='point-list'),
    path('media/', PointList.as_view(), name='upload'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)