from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from ..serializer.AuthUserSerializer import AuthUserSerializer, SignUserSerializer
from ..models import AuthUser
import jwt, datetime

@api_view(['POST'])
def inscription(request) :
    serializer=SignUserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({"datas": serializer.data}, status=status.HTTP_200_OK)

from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

@api_view(['POST'])
def login(request) :
    email=request.data['email']
    password=request.data['password']
    user=AuthUser.objects.filter(email=email).first()
    if user is None or not user.check_password(password):
        raise AuthenticationFailed('Email ou mot de passe incorrect')
    # payload={
    #     'id' : user.id_utilisateur,
    #     'exp' : datetime.datetime.utcnow()+datetime.timedelta(minutes=60),
    #     'iat' : datetime.datetime.utcnow()
    # }
    # token=jwt.encode(payload, 'secret', algorithm='HS256')
    response=Response()
    # response.set_cookie(key='jwt', value=token, httponly=True)
    response.data={
        "message": "Connectee en attente de jwt",
        "token" : get_tokens_for_user(user)
    }
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