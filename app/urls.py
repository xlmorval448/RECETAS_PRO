from django.urls import path
from . import views

urlpatterns = [
    path('', views.ingredientes_lista, name='ingredientes_lista'),
    path('<int:pk>/', views.ingrediente_crud, name='ingrediente_crud'),
    path('eliminar/<int:pk>/', views.ingrediente_eliminar, name='ingrediente_eliminar'),
]
