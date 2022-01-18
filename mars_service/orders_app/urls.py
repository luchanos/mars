from django.urls import path

from . import views

urlpatterns = [
    path('test_thing', views.test_thing, name='test_thing')
]
