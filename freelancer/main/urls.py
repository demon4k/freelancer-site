from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/<int:pk>/buy/', views.place_order, name='place_order'),  # ✅ Додано
    path('category/<int:pk>/', views.category_detail, name='category_detail'),
]
