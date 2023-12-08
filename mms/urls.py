"""
URL configuration for mms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from core import views as core_view
from account import views as acc_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_view.HomePage, name='home'),
    path('register/', acc_view.RegisterPage, name='register'),
    path('login/', acc_view.LoginPage, name='login'),
    path('logout/', acc_view.LogoutPage, name='logout'),
    path('dashboard/', core_view.Dashboard, name='dashboard'),
    path('mess/', include('mess.urls'))
]
