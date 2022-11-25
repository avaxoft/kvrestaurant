from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets
from . import serializers
from . import models
# Create your views here.

User = get_user_model()


class ItemsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = serializers.ItemSerializer

    def get_queryset(self):
        return models.Item.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


class DealsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = serializers.DealSerializer
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.DealsSerializer
        return serializers.DealSerializer

    

    def get_queryset(self):
        return models.Deal.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

class ItemsDealViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = serializers.ItemsDealSerializer

    def get_queryset(self):
        return models.Item.objects.filter(created_by=self.request.user)


class DealItemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = serializers.DealItemSerializer    

    def get_queryset(self):
        return models.DealItem.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = serializers.OrderSerializer    

    def get_queryset(self):
        return models.Order.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

class OrderDoneViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = serializers.OrderSerializer    

    def get_queryset(self):
        q = models.Order.objects.filter(created_by=self.request.user)
        return q.filter(is_active = True)
class OrderCanceledViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = serializers.OrderSerializer    

    def get_queryset(self):
        q = models.Order.objects.filter(created_by=self.request.user)
        return q.filter(is_active = False)
