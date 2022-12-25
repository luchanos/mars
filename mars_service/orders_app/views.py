from django.contrib.auth.models import Group, User
from django.forms import BooleanField
from django.http import HttpResponseRedirect
from django.shortcuts import render

from orders_app.models import Device, DeviceInField
from orders_app.forms import SignUpForm, NameForm, SettingsForm, SearchForm


def mainpage(request):
    data = {
        "title": "Welcome to MARS!",
        "data": [
            {
                "button_link": "admin",
                "name": "Заявки",
                "overview": "Работа с заявками на оборудование"
            },
            {
                "button_link": "devpage",
                "name": "Персонал",
                "overview": "Работа с базами персонала"
            },
            {
                "button_link": "devpage",
                "name": "Финансы",
                "overview": "Работа с базами финансов"
            },
            {
                "button_link": "devpage",
                "name": "База знаний",
                "overview": "Работа с базами знаний"
            },
        ]
    }
    return render(request, "orders_app/mainpage.html", data)


def get_devices(request):
    devices = DeviceInField.objects.all()
    if request.method == 'POST':
        form = SearchForm(request.POST)

        if form.is_valid():
            search_res = []
            data_for_search = form.data['data_for_search']

            if data_for_search.isdigit():
                search_res = list(DeviceInField.objects.filter(analyzer_id=int(data_for_search)))
            search_res = set(list(DeviceInField.objects.filter(customer__customer_name__contains=data_for_search)) + \
                             list(DeviceInField.objects.filter(analyzer__manufacturer__contains=data_for_search)) + \
                             list(DeviceInField.objects.filter(analyzer__model__contains=data_for_search)) + \
                             list(DeviceInField.objects.filter(owner_status__contains=data_for_search)) + search_res)

            return render(request, "orders_app/table_part.html", {"devices": search_res, "form": form})

    return render(request, "orders_app/table_part.html", {"devices": devices})


def devpage(request):
    return render(request, "orders_app/devpage.html", {"title": "Oops!"})


def sign_up_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.clean_data.get("username")
            signup_user = User.objects.get(username=username)
            user_group = Group.objects.get(name='User')
            user_group.user_set.add(signup_user)
    else:
        form = SignUpForm()
    return render(request, 'orders_app/test.html', {'form': form})


def get_name(request):
    from random import randint

    d = {str(k): BooleanField() for k, v in enumerate(range(randint(1, 10)))}
    SettingsFormMine = type("SettingsFormMine", (SettingsForm,), d)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SettingsFormMine(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SettingsFormMine()

    return render(request, 'orders_app/name.html', {'form': form})


def your_name(request):
    return 123
