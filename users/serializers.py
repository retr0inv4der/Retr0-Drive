from rest_framework import serializers
from .models import Users
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate

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
        
        password = validated_data.pop('password' , None)
        user = Users(**validated_data)
        if password :
            user.set_password(password) #hashed password
        user.save()
        return user

    
class LoginSerializer(serializers.Serializer) : 
    username = serializers.CharField(required = False )
    email = serializers.EmailField(required = False )
    password = serializers.CharField()


    def validate_password(self, value) : 
        if value is None : 
            raise serializers.ValidationError("password must be provided")
        return value
    
    def validate_emptiness(self , data ) :
        if data.get('username') is None and data.get('email') is None : 
            raise serializers.ValidationError("username or email should be provided")
        
    def validate(self, data):
        self.validate_emptiness(data=data)
        #uses the custom backend for authentication registered in backends.py bcz of the AUTHENTICATION_BACKENDS in settings.py
        user = authenticate(username = data.get('username') or data.get('email') , password= data.get('password'))
        if user is None : 
            raise serializers.ValidationError('invalid credentials.')

        if not user.is_active:
            raise serializers.ValidationError('User is disabled')
        data['user'] = user 
        return data

#serializer for outputing the data
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'username' , 'email' ]
