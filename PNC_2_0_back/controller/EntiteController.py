from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from PNC_2_0_back.Constantes import get_nb_pages
from back.models import AuthUser
from back.serializer.AuthUserSerializer import AuthUserSerializer
from ..model.Entite import Entite
from ..model.Profil import Profil
from ..serializer.EntiteSerializer import EntiteSelectSerializer, EntiteSerializer
from ..serializer.ProfilSerializer import ProfilSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
def getAllProfilPaginate(request, nbPage) :
    rows = Profil.objects.raw("SELECT * FROM profil LIMIT 20 OFFSET %s", [(nbPage-1)*20])
    serializer = ProfilSerializer(rows, many=True)
    return Response({"datas": serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getAllEntite(request):
    entites = Entite.objects.raw("SELECT id_entite, nom_entite FROM entite")
    serializer = EntiteSerializer(entites, many=True, fields=['idEntite', 'nomEntite'])
    return Response({"datas": serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def getAllEntitePaginate(request, nbPage) :
    rows = Entite.objects.raw("SELECT * FROM entite LIMIT 20 OFFSET %s", [(nbPage-1)*20])
    serializer = EntiteSerializer(rows, many=True)
    return Response({"datas": serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def getAllUtilisateur(request):
    # Récupérer tous les utilisateurs avec Django ORM
    utilisateurs = AuthUser.objects.all()
    
    # Sérialiser les résultats avec le sérialiseur Django REST Framework
    serializer = AuthUserSerializer(utilisateurs, many=True)
    
    # Retourner la réponse avec les données sérialisées
    return Response({"datas": serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def getAllProfil(request) :
    rows = Profil.objects.raw("SELECT id_profil, nom_profil FROM profil")
    serializer = ProfilSerializer(rows, many=True)
    return Response({"datas": serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllEntitePaginate(request, nbPage) :
    rows = Entite.objects.raw("SELECT * FROM entite LIMIT 20 OFFSET %s", [(nbPage-1)*20])
    serializer = EntiteSerializer(rows, many=True)
    return Response({"datas": serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllUtilisateurPaginate(request, nbPage) :
    rows=AuthUser.objects.raw("select*from utilisateur limit 20 offset %s", [(nbPage-1)*20])
    serializer = AuthUserSerializer(rows, many=True)
    return Response({"datas": serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNbPagesUtilisateur(request) :
    return Response(
        {
            "datas": {
                "nbPages" : get_nb_pages('utilisateur')
            }
        }, 
        status=status.HTTP_200_OK
    )

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNbPagesEntity(request) :
    return Response(
        {
            "datas": {
                "nbPages" : get_nb_pages('entite')
            }
        }, 
        status=status.HTTP_200_OK
    )