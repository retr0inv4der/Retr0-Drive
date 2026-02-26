from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import LoginSerializer
class LoginService:
    def login(self,data:dict)-> dict:
        #auth happens in validate method of the serializer
        ser = LoginSerializer(data=data) 
        if ser.is_valid(raise_exception=True) : 
            validated_data = ser.validated_data
            refresh = RefreshToken.for_user(validated_data.get('user'))
            return {
                'refresh' :str(refresh) ,
                'access' : str(refresh.access_token)
            }
        
        