# serializers.py
from rest_framework import serializers
from ..model.Entite import Entite

class EntiteSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        # Pop the 'fields' argument if it is present
        fields = kwargs.pop('fields', None)
        super(EntiteSerializer, self).__init__(*args, **kwargs)

        # Dynamically set the fields to be serialized
        if fields is not None:
            # Drop any fields that are not specified in the 'fields' argument
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = Entite
        fields = '__all__'
        
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        # Renommer les champs dans la représentation
        if 'idEntite' in ret :
            ret['id'] = ret.pop('idEntite')
        if 'nomEntite' in ret :
            ret['nom'] = ret.pop('nomEntite')
        if 'codeEntite' in ret :
            ret['cod'] = ret.pop('codeEntite')
        if 'emailEntite' in ret :
            ret['ema'] = ret.pop('emailEntite')
        return ret


class EntiteSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entite
        fields = ['idEntite', 'nomEntite']
        
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        # Renommer les champs dans la représentation
        if 'idEntite' in ret :
            ret['id'] = ret.pop('idEntite')
        if 'nomEntite' in ret :
            ret['nom'] = ret.pop('nomEntite')
        if 'codeEntite' in ret :
            ret['code'] = ret.pop('codeEntite')
        if 'emailEntite' in ret :
            ret['email'] = ret.pop('emailEntite')
        return ret