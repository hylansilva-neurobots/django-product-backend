from django.urls import path
from . import views

urlpatterns = [
    path('',views.product_view),
    path('buy/', views.buy_product, name='buy_product'),
]