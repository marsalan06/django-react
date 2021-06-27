from .serializers import RoomSerializer
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Room
# Create your views here.

def main(request):
    return HttpResponse("Hello")

                                        #CreateAPIView shows form as well 
class RoomView(generics.ListAPIView): #ListAPIView shows just data not the form 
    queryset=Room.objects.all()
    serializer_class=RoomSerializer

