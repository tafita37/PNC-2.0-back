# serializers.py
from rest_framework import serializers
from ..models import AuthUser
from PNC_2_0_back.serializer.EntiteSerializer import EntiteSerializer
from PNC_2_0_back.serializer.ProfilSerializer import ProfilSerializer

class AuthUserSerializer(serializers.ModelSerializer):
    entite = EntiteSerializer(fields=['idEntite', 'nomEntite'])
    profil = ProfilSerializer()
    class Meta:
        model = AuthUser
        fields = ['id', 'entite', 'profil', 'nomUtilisateur', 'prenom', 'email', 'password']
        extra_kwargs = {
            'password' : {'write_only' : True}
        }
        
    def create(self, validated_data):
        password=validated_data.pop('password', None)
        instance=self.Meta.model(**validated_data)
        if password is not None :
            instance.set_password(password)
        instance.save()
        return instance    
        
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if 'entite' in ret :
            ret['ent'] = ret.pop('entite')
        if 'profil' in ret :
            ret['pro'] = ret.pop('profil')
        if 'nomUtilisateur' in ret :
            ret['nom'] = ret.pop('nomUtilisateur')
        if 'prenom' in ret :
            ret['pre'] = ret.pop('prenom')
        if 'email' in ret :
            ret['ema'] = ret.pop('email')
        if 'password' in ret :
            ret['pas'] = ret.pop('password')
        return ret
        

class SignUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ['id', 'entite', 'profil', 'nomUtilisateur', 'prenom', 'email', 'password']
        extra_kwargs = {
            'password' : {'write_only' : True}
        }
        
    def create(self, validated_data):
        password=validated_data.pop('password', None)
        instance=self.Meta.model(**validated_data)
        if password is not None :
            instance.set_password(password)
        instance.save()
        return instance    
