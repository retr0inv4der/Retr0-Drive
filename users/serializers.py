from rest_framework import serializers
from .models import Users



class UserSerializer(serializers.ModelSerializer):
    space_left = serializers.DecimalField(
        max_digits=20, 
        decimal_places=20, 
        allow_null=True,
        required=False
    )
    class Meta : 
        model = Users 
        fields = '__all__'
        