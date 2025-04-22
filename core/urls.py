from django.urls import path
from .views import (
    RestaurantListCreateAPIView, RestaurantDetailAPIView,
    CategoryListCreateAPIView, CategoryDetailAPIView,
    MenuItemListCreateAPIView, MenuItemDetailAPIView,
    BulkUploadAPIView
)

urlpatterns = [
    path('restaurants/', RestaurantListCreateAPIView.as_view(), name='restaurant-list-create'),
    path('restaurants/<int:pk>/', RestaurantDetailAPIView.as_view(), name='restaurant-detail'),
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('menu-items/', MenuItemListCreateAPIView.as_view(), name='menu-item-list-create'),
    path('menu-items/<int:pk>/', MenuItemDetailAPIView.as_view(), name='menu-item-detail'),
    path('bulk-upload/', BulkUploadAPIView.as_view(), name='bulk-upload')
]