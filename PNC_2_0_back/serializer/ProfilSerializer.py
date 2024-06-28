from rest_framework import serializers
from ..model.Profil import Profil

class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profil
        fields = '__all__'
        
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        # Renommer les champs dans la représentation
        if 'id_profil' in ret :
            ret['id'] = ret.pop('id_profil')
        if 'nom_profil' in ret :
            ret['nom'] = ret.pop('nom_profil')
        return ret