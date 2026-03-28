from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Destination
from .serializers import DestinationSerializer


@api_view(['GET', 'POST'])
def create_destination(request):
    if request.method == 'GET':
        destinations = Destination.objects.all()
        serializer = DestinationSerializer(destinations, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DestinationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def city_list(request):
    cities = Destination.objects.values_list('city', flat=True).distinct()
    return Response(cities)