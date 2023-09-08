from django.shortcuts import render, redirect
from django.views.generic import ListView
from AppGestion.models import Producto
from .forms import editarProductoForm

class ProductoListViews(ListView):
    model = Producto
    template_name = 'datos.html'
    context_object_name = 'productos'  # Establece el nombre de la variable de contexto

    def get_queryset(self):
        return Producto.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = Producto.objects.all()  # Agrega la lista de productos al contexto
        return context

def insertarProducto(request):
    var_id = request.POST['id']
    var_nombre = request.POST['nombre']
    var_imagen1 = request.POST['imagen1']
    var_precio = request.POST['precio']

    producto = Producto.objects.create(
        id=var_id,
        nombre=var_nombre,
        imagen1=var_imagen1,
        precio=var_precio
    )
    return redirect('gestion')
#ESTA FUNCION ELIMINA EL PRODUCTO PERO EL PRIMERO DE LA LISTA NO ELIMINA EL QUE SELECCIONO
def eliminarProducto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('gestion')


#HACEN EXACTAMENTE LO MISMO QUE LA ANTERIOR. 
#def eliminarProducto(request, id):
#    producto = Producto.objects.get(id=id)
    
#    if producto:
#        producto.delete()
#    
#    return redirect('gestion')

#def eliminarProducto(request, id):
#    producto = Producto.objects.filter(id=id).first()
    
#    if producto:
#        producto.delete()
    
#    return redirect('gestion') 
# 
#def editarProducto(request, id):
#    producto = Producto.objects.get(id=id)

#    if request.method == 'POST':
#        producto.nombre = request.POST['nombre']
#        producto.imagen1 = request.POST['imagen1']
#        producto.precio= request.POST['precio']
#        producto.save()
#        return redirect('gestion')
        
#    return render(request, 'editarProducto.html', {'producto': producto}) 




def editarProducto(request, id):
    producto = Producto.objects.get(id=id)

    if request.method == 'POST':
        form = editarProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('gestion')
    else:
        form = editarProductoForm(instance=producto)
        
    return render(request, 'editarProducto.html', {'form': form, 'producto': producto})


        
    
       

