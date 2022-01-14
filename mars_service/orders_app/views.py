from django.http import HttpResponse
from django.shortcuts import render


def mainpage(request):
    data = {
        "data": [
            {
                "button_link": "admin",
                "name": "Заявки",
                "overview": "Работа с заявками на оборудование",
                "img_src": "https://ru.tripaggregator.com/photos/7166724.jpeg"
            },
            {
                "button_link": "#",
                "name": "Персонал",
                "overview": "Работа с базами персонала",
                "img_src": "https://www.hrhome.ru/images/upload/article2/personal-chto-eto-takoe-podgotovka-upravlenie.png"
            },
            {
                "button_link": "#",
                "name": "Финансы",
                "overview": "Работа с базами финансов",
                "img_src": "https://www.psychologos.ru/images/2ecc3f71141ef238dccbc1d31e669d4a.jpg"
            },
            {
                "button_link": "#",
                "name": "База знаний",
                "overview": "Работа с базами знаний",
                "img_src": "http://mospravda.ru/wp-content/uploads/2019/11/181108142443-large-c-800x509.jpg"
            },
        ]
    }
    return render(request, "orders_app/mainpage.html", data)


def test_thing(request):
    l = {1: 2, "l": [1, 2, 3, 4]}
    return render(request, "orders_app/test_thing.html", l)
