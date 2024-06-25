from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .functions import *
from .serializers import *

@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello, World!"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def getAllEntitePaginate(request, nbPage) :
    rows = Entite.objects.raw("SELECT * FROM entite LIMIT 20 OFFSET %s", [(nbPage-1)*20])
    serializer = EntiteSerializer(rows, many=True)
    return Response({"datas": serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def getAllProfilPaginate(request, nbPage) :
    rows = Profil.objects.raw("SELECT * FROM profil LIMIT 20 OFFSET %s", [(nbPage-1)*20])
    serializer = ProfilSerializer(rows, many=True)
    return Response({"datas": serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def getAllEntite(request) :
    rows = Entite.objects.raw("SELECT * FROM entite")
    serializer = EntiteSerializer(rows, many=True)
    return Response({"datas": serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def getAllProfil(request) :
    rows = Profil.objects.raw("SELECT * FROM profil")
    serializer = ProfilSerializer(rows, many=True)
    return Response({"datas": serializer.data}, status=status.HTTP_200_OK)