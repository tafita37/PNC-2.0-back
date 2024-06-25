# serializers.py
from rest_framework import serializers
from .models import *

class EntiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entite
        fields = '__all__'

class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profil
        fields = '__all__'