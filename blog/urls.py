from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('<int:pk>/', views.detalle_post, name='detalle_post'),
    path('autor/<int:pk>/', views.post_autor, name='post_autor'),
    path('autores/', views.autores, name='autores'),
    path('autor/nuevo', views.autor_nuevo, name='autor_nuevo'),
    path('autor/editar/<int:pk>', views.autor_editar, name='autor_editar'),
    path('autor/eliminar/<int:pk>', views.autor_eliminar, name='autor_eliminar'),
]
