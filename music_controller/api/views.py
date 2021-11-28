from django.db.models import query
from .serializers import RoomSerializer, CreateRoomSerializer
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from .models import Room
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

def main(request):
    return HttpResponse("Hello")

                                        #CreateAPIView shows form as well 
class RoomView(generics.ListAPIView): #ListAPIView shows just data not the form 
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class CreateRoomView(APIView):
    serializer_class = CreateRoomSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            guest_can_pause = serializer.data.get('guest_can_pause')
            votes_to_skip = serializer.data.get('votes_to_skip')
            host = self.request.session.session_key

            if Room.objects.filter(host = host).exists(): #verify if a already exist for the host
                queryset = Room.objects.filter(host = host)
                room = queryset[0] #database object
                print(queryset)
                print(room)
                room.guest_can_pause = guest_can_pause
                room.votes_to_skip = votes_to_skip
                room.save(update_fields=['guest_can_pause','votes_to_skip'])
            
            else: #create a room
                room = Room(host = host, guest_can_pause = guest_can_pause, votes_to_skip = votes_to_skip)
                room.save()

            return Response(RoomSerializer(room).data, status = status.HTTP_201_CREATED) #return json formatted data 