from django.urls import path

from . import views

app_name = "website"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("about/<slug:slug>/", views.subsystem_detail, name="subsystem_detail"),
]
