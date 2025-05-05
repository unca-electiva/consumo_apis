from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('departamentos/', views.get_departamentos, name='get_departamentos'),
    path('localidades/', views.get_localidades, name='get_localidades'),
    path('clima/', views.get_clima, name='get_clima'),
]
