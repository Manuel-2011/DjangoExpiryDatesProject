from django.shortcuts import render, redirect
from .forms import ProductoForm, SearchForm
from .models import Producto
from django.contrib.auth.decorators import login_required
import openpyxl
import os
from django.http import HttpResponse
from django.utils import timezone
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
@login_required
def inventario(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        print(form)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.usuario_crea = request.user
            producto.save()
            print(producto)
            return redirect('inventario')

    else:
        form = ProductoForm()
        search_form = SearchForm()

    object_list = Producto.objects.all().filter(activo=True).order_by('fecha_creado')
    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')
    try:
        productos = paginator.page(page)
    except PageNotAnInteger:
        productos = paginator.page(1)
    except EmptyPage:
        productos = paginator.page(paginator.num_pages)
    
    context = {'productos': productos, 'form': form, 'search_form': search_form, 'page': page, 'section': 'inventario'}
    return render(request, 'expiry_dates/inventario.html', context)

@login_required
def historico(request):
    object_list = Producto.objects.all().filter(activo=False).order_by('-fecha_salida')
    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')
    try:
        productos = paginator.page(page)
    except PageNotAnInteger:
        productos = paginator.page(1)
    except EmptyPage:
        productos = paginator.page(paginator.num_pages)

    search_form = SearchForm()
    
    context = {'productos': productos, 'search_form': search_form, 'page': page, 'section': 'historico'}
    return render(request, 'expiry_dates/historico.html', context)

@login_required
def producto_delete(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    
    if producto != None:
        # print(producto)
        producto.fecha_salida = timezone.now()
        producto.usuario_elimina = request.user
        producto.activo = False
        producto.save()

    return redirect ('inventario')

@login_required
def filtro_nombre(request):
    if request.method == "POST":
        search = ''
        form = SearchForm(request.POST)
        if form.is_valid(): 
            search = form.cleaned_data['search_word']
            if search == "":
                return redirect('inventario')

    form = ProductoForm()
    search_form = SearchForm()
    productos = Producto.objects.filter(activo=True).filter(nombre__contains=search).order_by('nombre')
    
    context = {'productos': productos, 'form': form, 'search_form': search_form}
    return render(request, 'expiry_dates/inventario.html', context)

@login_required
def filtro_nombre_historico(request):
    if request.method == "POST":
        search = ''
        form = SearchForm(request.POST)
        if form.is_valid(): 
            search = form.cleaned_data['search_word']
            if search=="":
                return redirect('historico')

    search_form = SearchForm()
    productos = Producto.objects.filter(activo=False).filter(nombre__contains=search).order_by('nombre')
    
    context = {'productos': productos, 'search_form': search_form}
    return render(request, 'expiry_dates/historico.html', context)