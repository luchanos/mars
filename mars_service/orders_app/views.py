from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from orders_app.models import Device
from orders_app.forms import NameForm


def mainpage(request):
    data = {
        "title": "Welcome to MARS!",
        "data": [
            {
                "button_link": "admin",
                "name": "Заявки",
                "overview": "Работа с заявками на оборудование",
                "img_src": "{% static '1.png' %}"
            },
            {
                "button_link": "devpage",
                "name": "Персонал",
                "overview": "Работа с базами персонала",
                "img_src": "{% static '2.png' %}"
            },
            {
                "button_link": "devpage",
                "name": "Финансы",
                "overview": "Работа с базами финансов",
                "img_src": "3.png"
            },
            {
                "button_link": "devpage",
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
    devices = []
    if request.method == 'POST':
        form = NameForm(request.POST)

        if form.is_valid():
            search_res = []
            data_for_search = form.data['your_name']
            devices = Device.objects.all()

            for el in devices:
                if data_for_search in {el.model, el.manufacturer, el.id}:
                    search_res.append(el)

            return render(request, "orders_app/table_part.html", {"devices": search_res, "form": form})

    else:
        form = NameForm()

    return render(request, "orders_app/table_part.html", {"devices": devices, "form": form})


def test(request):
    if request.method == 'POST':
        form = NameForm(request.POST)

        if form.is_valid():
            search_res = []
            data_for_search = form.data['your_name']
            devices = Device.objects.all()

            for el in devices:
                if data_for_search in {el.model, el.manufacturer, el.id}:
                    search_res.append(el)

            return render(request, "orders_app/table_part.html", {"devices": search_res})

    else:
        form = NameForm()

    return render(request, 'orders_app/test.html', {'form': form})


def devpage(request):
    return render(request, "orders_app/devpage.html", {"title": "Oops!"})
