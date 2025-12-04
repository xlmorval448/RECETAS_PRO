from django.urls import path
from . import views

urlpatterns = [
    path('', views.IngredienteListaView.as_view(), name='ingredientes_lista'),
    path('mostrar/<int:pk>', views.IngredienteMostrarView.as_view(), name='ingrediente_mostrar'),
    path('nuevo/', views.IngredienteNuevoView.as_view(), name='ingrediente_nuevo'),
    path('editar/<int:pk>', views.IngredienteEditarView.as_view(), name='ingrediente_editar'),
    path('eliminar/<int:pk>/', views.IngredienteEliminarView.as_view(), name='ingrediente_eliminar'),
    path('relaciones/', views.relaciones, name="relaciones"),
    path('receta/<int:pk>/', views.receta, name="receta"),
]
