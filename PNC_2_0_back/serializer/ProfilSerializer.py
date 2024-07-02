from rest_framework import serializers
from ..model.Profil import Profil

class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profil
        fields = '__all__'
        
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        # Renommer les champs dans la représentation
        if 'idProfil' in ret :
            ret['id'] = ret.pop('idProfil')
        if 'nomProfil' in ret :
            ret['nom'] = ret.pop('nomProfil')
        return ret