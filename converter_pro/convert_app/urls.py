from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name ='index'),
    path('convert_currency/', views.convert_currency, name ='convert_currency'),
]