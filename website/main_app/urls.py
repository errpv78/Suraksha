"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from . import views

app_name = "main_app"

urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('women_rights/', views.women_rights, name='women_rights'),

    path('register/', views.register, name="register"),
    path('logout/', views.logout_request, name="logout"),
    path('login/', views.login_request, name="login"),

    path('emergency_contact/', views.emergency_contact, name="emergency_contact"),
    path("create_contact/", views.create_contact , name="create_contact"),
    path("update_contact/<str:pk>/", views.update_contact, name="update_contact"),
    path("delete_contact/<str:pk>/", views.delete_contact, name="delete_contact"),
    path("emergency/", views.emergency, name="emergency"),

    path("news/", views.news, name="news"),

    # path('admin/', admin.site.urls),
]
