from django.urls import path
from . import views

urlpatterns = [
    path('', views.ingredientes_lista, name='ingredientes_lista'),
]
