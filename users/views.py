from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.exceptions import ValidationError

from .serializers import UserSerializer
from .SignUpService import SignUpService
from .LoginService import LoginService

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
            #gen the token via the signup service
            tokens = service.generate_token(user)

            #serilize the user for output
            output_ser = UserSerializer(user)
            return Response({
                "message":"successfully created the user.",
                "user": output_ser.data,
                "tokens" : tokens
            },status=status.HTTP_201_CREATED)
        
        except ValidationError as e : 
            return Response({
                "error" : e.detail
            },status=status.HTTP_405_METHOD_NOT_ALLOWED)
        

class LoginView(APIView) : 
    permission_classes = [AllowAny]
    #i want to make the client able to be able to login with username Or email as login field 
    def post(self, request) : 
        service = LoginService()

        try:
            tokens = service.login(data=request.data)
            return Response({
                'message': 'login was successful',
                'tokens' : tokens
            },status=status.HTTP_202_ACCEPTED)
        
        except ValidationError as e : 
            return Response({
                "error" : e.detail
            },status=status.HTTP_405_METHOD_NOT_ALLOWED)