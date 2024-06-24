from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello, World!"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def goodbye_world(request):
    return Response({"message": "Goodbye, World!"}, status=status.HTTP_200_OK)

@api_view(['POST'])
def custom_message(request):
    message = request.data.get('message', 'Default message')
    return Response({"message": message}, status=status.HTTP_200_OK)