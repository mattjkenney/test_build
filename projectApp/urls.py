from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("tests", views.tests, name="tests"),
    path("parameters", views.parameters, name="parameters"),
    path("criteria", views.criteria, name="criteria"),
    path("builds", views.builds, name="builds")
]