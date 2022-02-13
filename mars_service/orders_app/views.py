from django.http import HttpResponse
from django.shortcuts import render

from orders_app.models import Device


def mainpage(request):
    data = {
        "data": [
            {
                "button_link": "admin",
                "name": "Заявки",
                "overview": "Работа с заявками на оборудование",
                "img_src": "{% static '1.png' %}"
            },
            {
                "button_link": "#",
                "name": "Персонал",
                "overview": "Работа с базами персонала",
                "img_src": "{% static '2.png' %}"
            },
            {
                "button_link": "#",
                "name": "Финансы",
                "overview": "Работа с базами финансов",
                "img_src": "3.png"
            },
            {
                "button_link": "#",
                "name": "База знаний",
                "overview": "Работа с базами знаний",
                "img_src": "{% static '4.png' %}"
            },
        ]
    }
    return render(request, "orders_app/mainpage.html", data)


def test_thing(request):
    l = {1: 2, "l": [1, 2, 3, 4]}
    return render(request, "orders_app/test_thing.html", l)


def get_devices(request):
    devices = Device.objects.all()
    return render(request, "orders_app/table_part.html", {"devices": devices})
