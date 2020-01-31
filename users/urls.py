from django.urls import path, include
from django.conf.urls import url

from . import views

urlpatterns = [
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('loggedin', views.loggedin, name="loggedin"),
    path('logout', views.logout, name="logout"),
    url(r'^messages/', include('django_messages.urls')),
]
