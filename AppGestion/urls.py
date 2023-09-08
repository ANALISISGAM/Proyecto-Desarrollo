from django.urls import path
from AppGestion.views import ProductoListViews,  insertarProducto, eliminarProducto, editarProducto

urlpatterns = [
    path('',ProductoListViews.as_view(),name='gestion'),
    path('insertarProducto/',insertarProducto,name='Insertar'),
    path('eliminarProducto/<int:id>',eliminarProducto,name='eliminarProducto'),
    path('editarProducto/<int:id>', editarProducto, name='editarProducto')
    
]