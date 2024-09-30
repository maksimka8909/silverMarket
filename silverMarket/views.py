from django.http import HttpResponse
from django.shortcuts import render

from silverMarket.models import Product, Bucket


def index(request):
    products = Product.objects.all()
    products_dict = {
        'products': products
    }
    return render(request, "mainPage.html", products_dict)


def bucket(request):
    buckets = Bucket.objects.select_related('product')
    buckets_dict = {
        'bucket': buckets
    }
    return render(request, "bucketPage.html", buckets_dict)


def contacts(request):
    return render(request, "contactsPage.html")

def addProduct(request, productId):
    product = Product.objects.get(id=productId)
    Bucket.objects.create(product=product)
    products = Product.objects.all()
    products_dict = {
        'products': products
    }
    return render(request, "mainPage.html", products_dict)