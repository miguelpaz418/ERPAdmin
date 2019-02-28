from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from apps.inventario.models import *
from apps.inventario.forms import *

# Create your views here.


def index (request):

    return render(request, 'inventario/landing.html')

def entradas (request):
    ordenes = OrdenCompra.listar()

    return render(request, 'inventario/entrada.html', {'ordenes': ordenes})

def inventario (request):
    inventario = Inventario.listar()

    return render(request, 'inventario/inventario.html', {'inventario': inventario})

def registroEntrada(request, idOrden):
	orden = OrdenCompra.objects.get(id = idOrden)
	form = RegistroEntrada(initial={'ordenCompra': orden})
	if request.method == 'POST':
		POST = request.POST.copy()
		POST['ordenCompra'] = orden.id
		form = RegistroEntrada(POST, instance=orden)

		if form.is_valid():
			form.save()
			messages.success(request, 'Entrada registrada exitosamente')
			return redirect('entradas')
		else:
			messages.error(request, 'Por favor corrige los errores')
			form = RegistroEntrada(initial={'ordenCompra': orden})
			return render(request, 'inventario/registrarEntrada.html', {'form': form})

	return render(request, 'inventario/registrarEntrada.html', {'form': form})	
