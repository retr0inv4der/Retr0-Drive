
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from rest_framework import request
#sers

from .serializers import UserSerializer


class UserRegisterAPI(APIView) : 

    def post(self, request : request):
        ser = UserSerializer(request.data)
        ser.is_valid(raise_exception= True)
        ser.save()
        return Response({
            "message" : "user registered successfully"} ,
             status= status.HTTP_201_CREATED
            )
    
class UserLoginAPI(APIView) : 
    def post(self  , request ) : 
        ser = UserSerializer(request.data )
        ser.is_valid(raise_exception=True)
        return Response({"Logged in"}  , status=status.HTTP_202_ACCEPTED)
    