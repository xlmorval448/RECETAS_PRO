from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('ingredientes/', views.ingredientes_lista, name='ingredientes_lista'),
]
