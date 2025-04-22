import pandas as pd
from django.contrib import admin, messages
from django.urls import path
from django.shortcuts import render, redirect
from django import forms
from .models import Restaurant, Category, MenuItem


@admin.register(Restaurant)
class RestaurantAdmin( admin.ModelAdmin):
    list_display = ('id', 'restaurant_name', 'address', 'phone', 'email')
    search_fields = ('restaurant_name', 'address', 'phone', 'email')
    list_filter = ('address',)
    ordering = ('id',)


@admin.register(Category)
class CategoryAdmin( admin.ModelAdmin):
    list_display = ('id', 'category_name', 'created_at')
    search_fields = ('category_name',)
    ordering = ('id',)


@admin.register(MenuItem)
class MenuItemAdmin( admin.ModelAdmin):
    list_display = ('id', 'menu_item_name', 'restaurant', 'category', 'price', 'is_available')
    search_fields = ('menu_item_name', 'description')
    list_filter = ('restaurant', 'category', 'is_available')
    ordering = ('id',)

