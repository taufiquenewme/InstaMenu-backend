import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Restaurant, Category, MenuItem
from .serializers import RestaurantSerializer, CategorySerializer, MenuItemSerializer


class RestaurantListCreateAPIView(APIView):
    def get(self, request):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RestaurantDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Restaurant.objects.get(pk=pk)
        except Restaurant.DoesNotExist:
            return None

    def get(self, request, pk):
        restaurant = self.get_object(pk)
        if not restaurant:
            return Response({"error": "Restaurant not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)

    def put(self, request, pk):
        restaurant = self.get_object(pk)
        if not restaurant:
            return Response({"error": "Restaurant not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = RestaurantSerializer(restaurant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        restaurant = self.get_object(pk)
        if not restaurant:
            return Response({"error": "Restaurant not found"}, status=status.HTTP_404_NOT_FOUND)
        restaurant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryListCreateAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return None

    def get(self, request, pk):
        category = self.get_object(pk)
        if not category:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        category = self.get_object(pk)
        if not category:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = self.get_object(pk)
        if not category:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MenuItemListCreateAPIView(APIView):
    def get(self, request):
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MenuItemDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return MenuItem.objects.get(pk=pk)
        except MenuItem.DoesNotExist:
            return None

    def get(self, request, pk):
        menu_item = self.get_object(pk)
        if not menu_item:
            return Response({"error": "Menu item not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = MenuItemSerializer(menu_item)
        return Response(serializer.data)

    def put(self, request, pk):
        menu_item = self.get_object(pk)
        if not menu_item:
            return Response({"error": "Menu item not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = MenuItemSerializer(menu_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        menu_item = self.get_object(pk)
        if not menu_item:
            return Response({"error": "Menu item not found"}, status=status.HTTP_404_NOT_FOUND)
        menu_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BulkUploadAPIView(APIView):
    def post(self, request):
        if 'excel_file' not in request.FILES:
            return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)

        excel_file = request.FILES['excel_file']
        try:
            df = pd.read_excel(excel_file)
            for _, row in df.iterrows():
                restaurant, _ = Restaurant.objects.get_or_create(
                    restaurant_name=row['restaurant_name'],
                    address=row['address'],
                    phone=row['phone'],
                    email=row['email']
                )
                category, _ = Category.objects.get_or_create(
                    category_name=row['category_name']
                )
                MenuItem.objects.create(
                    restaurant=restaurant,
                    category=category,
                    menu_item_name=row['menu_item_name'],
                    price=row['price'],
                    description=row['description'],
                    is_available=row['is_available']
                )
            return Response({"message": "Data uploaded successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": f"Error processing file: {e}"}, status=status.HTTP_400_BAD_REQUEST)