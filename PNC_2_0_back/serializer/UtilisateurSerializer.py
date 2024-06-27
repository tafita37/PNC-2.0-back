from rest_framework import serializers
from ..model.Utilisateur import Utilisateur
from .EntiteSerializer import EntiteSerializer
from .ProfilSerializer import ProfilSerializer

class UtilisateurSerializer(serializers.ModelSerializer):
    id_entite = EntiteSerializer()
    id_profil = ProfilSerializer()
    class Meta:
        model = Utilisateur
        fields = ['id_utilisateur', 'id_entite', 'id_profil', 'titre', 'nom_utilisateur', 'prenom', 'email']