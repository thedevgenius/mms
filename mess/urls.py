
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Mills, name='mills'),
    path('add-mill/', views.AddMill, name='add-mill'),
    path('add-establish/', views.AddEstablish, name='add-establish'),
    path('bill/', views.Bills, name='bill'),
    path('mill-delete/<int:id>', views.DeleteMill, name='mill-delete'),
]
