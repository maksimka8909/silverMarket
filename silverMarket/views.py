from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, "mainPage.html")


def bucket(request):
    return render(request, "bucketPage.html")


def contacts(request):
    return render(request, "contactsPage.html")