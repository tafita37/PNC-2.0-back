from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed

from PNC_2_0_back.model.Entite import Entite
from PNC_2_0_back.model.Profil import Profil
from ..serializer.AuthUserSerializer import AuthUserSerializer, SignUserSerializer
from ..models import AuthUser
import jwt
from datetime import datetime, timedelta
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.crypto import get_random_string
import string

@api_view(['POST'])
def inscription(request) :
    chars = string.ascii_letters + string.digits + string.punctuation
    password = get_random_string(20, chars)
    entite=Entite.objects.filter(idEntite=request.data["entite"]).first()
    profil=Profil.objects.filter(idProfil=request.data["profil"]).first()
    request.data["password"]=password
    request.data["email"]=request.data["prenom"].strip().replace(" ", ".")+"."+request.data["nomUtilisateur"].strip().replace(" ", ".")+"."+entite.codeEntite.strip().replace(" ", ".")+"."+profil.nomProfil+"@pnc.mg"
    request.data["email"]=request.data["email"].lower()
    serializer=SignUserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({"datas": serializer.data, "mdp" : password, "email" : request.data["email"]}, status=status.HTTP_200_OK)

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    access_token = refresh.access_token
    access_token_lifetime = access_token.lifetime.total_seconds()  # Durée de vie du token d'accès en secondes
    access_token_expiration = datetime.now() + timedelta(seconds=access_token_lifetime)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'access_token_expiration': access_token_expiration
    }
    
@api_view(['POST'])
def login(request) :
    email=request.data['email']
    password=request.data['password']
    user=AuthUser.objects.filter(email=email).first()
    expiration = datetime.now() + timedelta(days=1)
    if user is None or not user.check_password(password):
        raise AuthenticationFailed('Email ou mot de passe incorrect')
    response=Response()
    token=get_tokens_for_user(user)
    response.data={
        "message": "Connexion reussie",
        "token" : token
    }
    response.set_cookie(key='jwt', value=token.get('access'), httponly=True, expires=expiration)
    return response

@api_view(['GET'])
def getUserConnected(request) :
    token=request.COOKIES.get('jwt')
    if not token : 
        raise AuthenticationFailed("Veuillez d'abord vous connecter")
    try :
        payload=jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed("Vous n'etes pas connectees")
    user=AuthUser.objects.filter(id_utilisateur=payload['id']).first()
    serializer=AuthUserSerializer(user)
    # print(serializer)
    return Response({"data " : serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def logout(request) :
    response=Response()
    response.delete_cookie("jwt")
    response.data={
        "message" : "Deconnectee"
    }
    return response