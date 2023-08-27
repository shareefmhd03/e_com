from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Product, Category, Subcategory

def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'index.html', context)

def category_list(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'category_list.html', context)

def subcategory_list(request, category_id):
    subcategories = Subcategory.objects.filter(category_id=category_id)
    context = {'subcategories': subcategories}
    return render(request, 'subcategory_list.html', context)

def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    context = {'product': product}
    return render(request, 'product_detail.html', context)
