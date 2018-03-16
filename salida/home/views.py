from django.shortcuts import render, redirect
from .models import *
from .forms import *

def  vista_about(request):
	return render (request,'about.html')

# Create your views here.

def  vista_hobbit(request):
	return render (request,'hobbit.html')

def  vista_empresa(request):
	empresa=['poemas', 'obras']
	diccionario={'nombre':empresa}
	return render (request,'empresa.html', diccionario)   

def  vista_contactos(request):
	contactos= 'SENA'
	diccionario={'nombre':contactos}
	return render (request,'contactos.html', diccionario)

def vista_lista_Producto(request):
	lista= Producto.objects.filter()
	return render(request,'lista_producto.html', locals())

def vista_lista_Marca(request):
	listar= Marca.objects.filter()
	return render(request,'lista_marca.html', locals())

def vista_lista_Categoria(request):
	lista2= Categoria.objects.filter()
	return render(request,'lista_categoria.html', locals())

def vista_agregar_producto(request):
	if request.method == 'POST':
		formulario = agregar_producto_form(request.POST, request.FILES)
		if formulario.is_valid():
			prod = formulario.save(commit = False)
			prod.status = True
			prod.save()
			formulario.save_m2m()
			return redirect ('/lista_producto/')

	else:
		formulario = agregar_producto_form()
	return render(request, 'agregar_Producto.html', locals())

def vista_ver_producto(request, id_prod):
	p=Producto.objects.get(id=id_prod)
	return render(request,'ver_producto.html', locals())

def vista_editar_producto(request, id_prod):
	prod=Producto.objects.get(id=id_prod)
	if request.method =='POST':
		formulario = agregar_producto_form(request.POST, request.FILES, instance= prod)
		if formulario.is_valid():
			prod=formulario.save()
			return redirect ('/lista_producto/')
	else:
		formulario = agregar_producto_form(instance= prod)
		return render(request, 'agregar_producto.html', locals())

def vista_eliminar_producto(request, id_prod):
	prod = Producto.objects.get(id=id_prod)
	prod.delete()
	return redirect('/lista_producto/', locals())

