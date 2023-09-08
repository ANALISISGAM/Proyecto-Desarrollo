from django.shortcuts import render

def pagina_de_inicio(request):
    return render(request, 'pagina_inicio.html')
