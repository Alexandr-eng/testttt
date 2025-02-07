from django.urls import path
from .views import CategoryListView, ProductListView

urlpatterns = [
    path('', CategoryListView.as_view(), name='category-list'),
    path('products/', ProductListView.as_view(), name='product-list'),
]