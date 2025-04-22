from rest_framework import serializers
from .models import Restaurant, Category, MenuItem


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'restaurant_name', 'address', 'phone', 'email', 'created_at', 'updated_at']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'created_at', 'updated_at']


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'restaurant', 'category', 'menu_item_name', 'price', 'description', 'is_available', 'created_at', 'updated_at']