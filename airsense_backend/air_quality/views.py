from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AirQualityReadingSerializer

@api_view(['POST'])
def add_air_quality_reading(request):
    serializer = AirQualityReadingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)