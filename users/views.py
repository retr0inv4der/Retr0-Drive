from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from rest_framework import request
from rest_framework.permissions import IsAuthenticated , AllowAny
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken 
from rest_framework_simplejwt.authentication import AuthUser
from rest_framework_simplejwt.exceptions import TokenError , InvalidToken
from rest_framework.exceptions import ValidationError

from .serializers import UserSerializer
from SignUpService import SignUpService

class RegisterView(APIView) : 
    permission_classes= [AllowAny]
    def post(self ,request): 
        service = SignUpService()
        #try to sign up and handle exceptions
        try:
            user = service.signup(
                username=request.data.get('username'),
                email=request.data.get('email'),
                password=request.data.get('password')
            )
            #serilize the user for output
            output_ser = UserSerializer(user)
            return Response({
                "message":"successfully created the user.",
                "user": output_ser.data
            },status=status.HTTP_201_CREATED)
        
        except ValidationError as e : 
            return Response({
                "error" : e.detail
            },status=status.HTTP_405_METHOD_NOT_ALLOWED)
        