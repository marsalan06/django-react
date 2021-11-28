from django.urls import path
from django.urls.conf import include
from .views import main, RoomView, CreateRoomView

urlpatterns = [
    path('',main,name='main'),
    path('room',RoomView.as_view()),
    path('createroom', CreateRoomView.as_view())
]
