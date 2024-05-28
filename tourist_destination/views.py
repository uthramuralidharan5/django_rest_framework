from rest_framework import viewsets
from .my_routers import MyRouter
from .serializers import DestinationSerializer

from django.shortcuts import render
from .models import Destination



def destination_list(request):
    destinations = Destination.objects.all()
    return render(request, 'tourist_destination/templates/destination_list.html', {'destinations': destinations})


class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer


class DestinationListCreate(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer


class DestinationRetrieveUpdateDestroy(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer


class PopularDestinationsView(viewsets.ViewSet):
    pass


my_router = MyRouter()
my_router.register(r'tourist-destinations', DestinationListCreate, basename='tourist-destination-list-create')
my_router.register(r'tourist-destinations/<int:pk>', DestinationRetrieveUpdateDestroy,
                   basename='tourist-destination-retrieve-update-destroy')
