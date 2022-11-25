
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('itemsdeals', views.ItemsDealViewSet, basename='itemsdeals')
router.register('dealitem', views.DealItemViewSet, basename='dealitem')



router.register('items', views.ItemsViewSet, basename='items')
router.register('deals', views.DealsViewSet, basename='deals')
router.register('order', views.OrderViewSet, basename='order')
router.register('orderdone', views.OrderDoneViewSet, basename='orderdone')
router.register('ordercanceled', views.OrderCanceledViewSet, basename='ordercanceled')

urlpatterns = [
    path('', include(router.urls)),
]