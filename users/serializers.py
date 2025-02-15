from rest_framework import serializers
from .models import UserInfo
from django.forms import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.hashers import check_password

class UserInfoSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = UserInfo
        fields = ['username', 'email', 'phone', 'password', 'confirm_password']
        extra_kwargs = {
            'password':{'write_only': True},
        }
    def validate_username(self, value):
        if len(value) < 4:
            raise serializers.ValidationError("Username must be at least 4 characters long.")
        return value

    def validate_email(self, value):
        try:
            validate_email(value)
        except ValidationError:
            raise serializers.ValidationError("Enter a valid email address.")
        return value

    def validate_phone(self, value):
        if value and len(value) != 10:
            raise serializers.ValidationError("Phone number must be exactly 10 digits long.")
        return value

    def validate_password(self, value):
        if len(value) < 4:
            raise serializers.ValidationError("Password must be at least 4 characters long.")
        return value

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password', None)  
        user = UserInfo.objects.create(**validated_data)
        return user
    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            raise serializers.ValidationError("Must include both username and password.")

        try:
            user = UserInfo.objects.get(username=username)
        except UserInfo.DoesNotExist:
            raise serializers.ValidationError("User with this username does not exist.")

        if not check_password(password, user.password):
            raise serializers.ValidationError("Incorrect password.")

        data['user'] = user
        return data