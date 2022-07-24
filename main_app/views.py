from django.shortcuts import render, get_object_or_404
from .models import Category, Product
# Create your views here.

def categories(request):
    return{
        'categories': Category.objects.all()
    }

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/detail.html', {'product': product})

def category_index(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category= category )