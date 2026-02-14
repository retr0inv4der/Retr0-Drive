
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from rest_framework import request
from rest_framework.permissions import IsAuthenticated , AllowAny
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken 
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import TokenError , InvalidToken
from .models import Users
#sers
from .serializers import UserSerializer


class CookieJwtAuthentication(JWTAuthentication):
    def authenticate(self, request):
        # Get the token from HttpOnly cookie
        token = request.COOKIES.get("access_token")
        if token is None:
            return None  # DRF will set request.user = AnonymousUser

        try:
            validated_token = self.get_validated_token(token)
            user = self.get_user(validated_token)
            return (user, validated_token)
        except (TokenError, InvalidToken):
            return None

class UserRegisterAPI(APIView) : 
    permission_classes = [AllowAny]
    def post(self, request : request):
        ser = UserSerializer(data= request.data)
        ser.is_valid(raise_exception= True)
        user= ser.save()
        
        refresher = RefreshToken.for_user(user=user)
        response =  Response({
            "message" : "user registered successfully"} ,
             status= status.HTTP_201_CREATED
            )
        response.set_cookie(
            key="access_token",
            value=str(refresher.access_token),
            httponly=True , 
            secure=False # TODO : https in production
        )
        response.set_cookie(
            key="refresh_token",
            value=str(refresher),
            httponly=True , 
            secure=False # TODO : https in production
        )
        return response
        
    
class UserLoginAPI(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"error": "username and password required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = Users.objects.get(username=username)
        print(user.id)


        if user.password != password:
            return Response(
                {"error": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)

        response = Response(
            {"message": f"user {user.username} successfully logged in."},
            status=status.HTTP_200_OK
        )

        response.set_cookie(
            key="refresh_token",
            value=str(refresh),
            httponly=True,
            secure=False
        )
        response.set_cookie(
            key="access_token",
            value=str(refresh.access_token),
            httponly=True,
            secure=False
        )

        return response

class GetUserProfileInfoAPI(APIView):
    authentication_classes = [CookieJwtAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request) :
        ser = UserSerializer(request.user)
        return Response(ser.data , status=status.HTTP_202_ACCEPTED)
