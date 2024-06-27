from django.urls import path
from back.controller.AuthController import *

urlpatterns = [
    path('register/', inscription),
    path('login/', login),
    path('logout/', logout),
]
