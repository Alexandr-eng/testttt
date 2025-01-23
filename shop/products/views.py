from rest_framework import generics, pagination
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = pagination.PageNumberPagination

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = pagination.PageNumberPagination