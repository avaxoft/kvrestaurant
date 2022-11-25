from django.contrib.auth import get_user_model
from rest_framework import viewsets
from . import serializers
from .models import User
# Create your views here.


class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UsersSerializer
    queryset = User.objects.all()

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    # queryset = User.objects.all()

    def get_queryset(self):
        return User.objects.filter(username=self.request.user)
