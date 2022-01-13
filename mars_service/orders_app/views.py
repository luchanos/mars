from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "orders_app/home.html")


def mainpage(request):
    return render(request, "orders_app/mainpage.html")
