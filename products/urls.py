from django.contrib import admin
from django.urls import path, include

from .views import ProductViewSet

urlpatterns = [
    path('products', ProductViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('products/<str:pk>', ProductViewSet.as_view({
        'get': 'get',
        'put': 'update',
        'delete': 'delete'
    }))
]