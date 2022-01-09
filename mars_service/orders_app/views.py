from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def home(request):
    return render(request, "orders_app/home.html")
