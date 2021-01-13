from rest_framework import serializers
from .models import User

class registerSerializer (serializers.ModelSerializer) :
    password = serializers.CharField(max_length=255, min_length=8, write_only=True)
    
    class Meta :
        model = User
        fields = ['email', 'username', 'identity', 'password']

    def validate (self, attrs) :
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        identity = attrs.get('identity', '')

        return attrs
        
    def create (self, validate_data) :
        return User.objects.create_user(**validate_data)

class loginSerializer (serializers.ModelSerializer) :
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255, min_length=8)

    class Meta :
        model = User
        fields = ['email', 'password']

    def validate (self, attrs) :
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        return attrs