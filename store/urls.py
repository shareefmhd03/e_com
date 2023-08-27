from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('categories/', views.category_list, name='category_list'),
    path('subcategories/<int:category_id>/', views.subcategory_list, name='subcategory_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]
