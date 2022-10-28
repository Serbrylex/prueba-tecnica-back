# Django REST Framework
from pdb import Pdb
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Serializers
from users.serializers import (
    UserLoginSerializer, UserSerializer, UserSignUpSerializer
)


@api_view(['POST'])
def signup(request): 
	""" User signup. """	

	serializer = UserSignUpSerializer(data=request.data)
	serializer.is_valid(raise_exception=True)	
	user = serializer.save()	
	data = UserSerializer(user).data		

	return Response(data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def login(request):	
    serializer = UserLoginSerializer(data=request.data)	    
    valido = serializer.is_valid() 
    if valido == False:
        data = {
            'state': False,
            'descriptionResponse': 'Usuario o contraseña invalido'
        }    
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
    user, token = serializer.save()	
    data = {
        'state': True,
        'descriptionResponse': '',
        'user': UserSerializer(user).data,
        'token': token
    }
    print(data)
    return Response(data, status=status.HTTP_201_CREATED)