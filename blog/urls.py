from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('<int:pk>/', views.detalle_post, name='detalle_post'),
    path('autor/<int:autor_pk>/', views.post_autor, name='post_autor'),
    path('autores/', views.autores, name='autores'),
    path('autor/nuevo', views.autor_nuevo, name='autor_nuevo')
]
