# serializers.py
from rest_framework import serializers
from ..model.Entite import Entite

class EntiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entite
        fields = '__all__'