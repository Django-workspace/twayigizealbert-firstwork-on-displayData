
from .import views
from django.urls import path


urlpatterns = [

    path("home", views.home, name= 'home'),
    path("registration", views.registration, name= 'registration'),
    path("login", views.login, name="login")
]