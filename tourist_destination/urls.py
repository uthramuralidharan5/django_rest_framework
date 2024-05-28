from django.urls import path
from .views import destination_list

app_name= 'tourist_destination'
urlpatterns = [
    path('destinations/', destination_list, name='destination_list'),
]
