from django.urls import path
from .views import index
urlpatterns = [
    path('home',index),
    path('join',index),
    path('create',index)
]
