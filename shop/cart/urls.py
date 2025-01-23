from django.urls import path
from .views import CartView, CartDetailView, clear_cart

urlpatterns = [
    path('', CartView.as_view(), name='cart-list'),
    path('<int:pk>/', CartDetailView.as_view(), name='cart-detail'),
    path('clear/', clear_cart, name='clear-cart'),
]
