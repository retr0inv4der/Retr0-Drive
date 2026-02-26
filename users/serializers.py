from rest_framework import serializers
from .models import Users
from rest_framework.validators import UniqueValidator

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'username' , 'email' , 'password']

    def validate_username(self , value) : 
        if Users.objects.filter(username__iexact=value).exists() :
            raise serializers.ValidationError("Username is already taken.")
        return value
    
    def validate_email(self, value) : 
        if Users.objects.filter(email__iexact=value).exists() : 
            raise serializers.ValidationError("Email is already in use.")
        return value
        
    def create(self, validated_data):
        print("validated data:" , validated_data)
        password = validated_data.pop('password' , None)
        user = Users(**validated_data)
        if password :
            user.set_password(password) #hashed password
        user.save()
        return user
    

#serializer for outputing the data
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'username' , 'email' ]
