from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category


# Create your views here.
def home(request):
    catalog_list = Product.objects.all()
    category_list = Category.objects.all()
    context = {
        'object_list': catalog_list,
        'category_list': category_list,
        'title': 'Каталог'
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    catalog_list = Product.objects.all()
    context = {
        'object_list': catalog_list,
        'title': 'Контакты'
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')

    return render(request, 'catalog/contacts.html', context)


def product(request, pk):
    product_item = Product.objects.get(pk=pk)
    catalog_list = Product.objects.filter(id=pk)
    context = {
        'object_list': catalog_list,
        'title': f'{product_item.title}'
    }
    return render(request, 'catalog/product.html', context)
