from .models import Users
from .serializers import SignUpSerializer
from rest_framework_simplejwt import tokens

class SignUpService :
    def generate_token(self, user):
        Refresh = tokens.RefreshToken.for_user(user)

        #custom tags for the token : 
        Refresh['username']  = user.username
        Refresh['email'] = user.email 

        return {
            'refresh' : str(Refresh),
            'access' : str(Refresh.access_token)
        }
    
    def signup(self ,username , email , password ):
        data = {
            "username" : username, 
            "email" : email , 
            "password" : password
        }
        ser = SignUpSerializer(data=data) 
        if ser.is_valid(raise_exception=True) : 
            user = ser.save()
            return user


