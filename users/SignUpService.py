from .models import Users
from .serializers import SignUpSerializer
class SignUpService : 
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


