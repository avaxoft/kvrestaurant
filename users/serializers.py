from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'is_manager', 'is_staffer', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    # def create(self, validated_data):
    #     return User.objects.create_user(**validated_data)

    # def create(self, validated_data):
    #     if "password" in validated_data:
    #         validated_data["password"] = make_password(validated_data["password"])
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     if "password" in validated_data:
    #         validated_data["password"] = make_password(validated_data["password"])
    #     return super().update(instance, validated_data)


    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'is_manager', 'is_staffer']




