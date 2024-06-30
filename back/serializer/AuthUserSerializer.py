# serializers.py
from rest_framework import serializers
from ..models import AuthUser
from PNC_2_0_back.serializer.EntiteSerializer import EntiteSerializer
from PNC_2_0_back.serializer.ProfilSerializer import ProfilSerializer

class AuthUserSerializer(serializers.ModelSerializer):
    id_entite = EntiteSerializer()
    id_profil = ProfilSerializer()
    class Meta:
        model = AuthUser
        fields = ['id', 'id_entite', 'id_profil', 'nom_utilisateur', 'prenom', 'email', 'password']
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
        

class SignUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ['id', 'id_entite', 'id_profil', 'nom_utilisateur', 'prenom', 'email', 'password']
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
        if 'id_entite' in ret :
            ret['en'] = ret.pop('id_entite')
        if 'id_profil' in ret :
            ret['profil'] = ret.pop('id_profil')
        if 'code_entite' in ret :
            ret['code'] = ret.pop('code_entite')
        if 'email_entite' in ret :
            ret['email'] = ret.pop('email_entite')
        return ret
