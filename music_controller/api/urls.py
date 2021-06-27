from django.urls import path
from django.urls.conf import include
from .views import main,RoomView

urlpatterns = [
    path('',main,name='main'),
    path('room',RoomView.as_view()),
]
