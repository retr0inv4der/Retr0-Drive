from rest_framework import serializers
from .models import Users



class UserSerializer(serializers.Serializer):
    class Meta : 
        model = Users 
        fields = ['username' , 'password'  ]
        read_only_fields = ['joined' , 'space_left']