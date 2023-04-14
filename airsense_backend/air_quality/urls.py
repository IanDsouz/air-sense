from django.urls import path
from .views import add_air_quality_reading

urlpatterns = [
    path('add_reading/', add_air_quality_reading, name='add_reading'),
]