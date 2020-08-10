from django.shortcuts import render, redirect
from .forms import ProductoForm, SearchForm
from .models import Producto, Historico
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def inventario(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        print(form)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.usuario = request.user
            producto.save()
            print(producto)
            return redirect('inventario')

    else:
        form = ProductoForm()
        search_form = SearchForm()

    productos = Producto.objects.all().order_by('fecha_vencimiento')
    
    context = {'productos': productos, 'form': form, 'search_form': search_form}
    return render(request, 'expiry_dates/inventario.html', context)

@login_required
def historico(request):
    productos = Historico.objects.all().order_by('fecha_salida').reverse()
    search_form = SearchForm()
    
    context = {'productos': productos, 'search_form': search_form}
    return render(request, 'expiry_dates/historico.html', context)

@login_required
def producto_delete(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    
    if producto != None:
        print(producto)
        historico = Historico()
        historico.nombre = producto.nombre
        historico.fecha_vencimiento = producto.fecha_vencimiento
        historico.fecha_creado = producto.fecha_creado
        historico.usuario_elimina = request.user
        historico.save()
        producto.delete()

    return redirect ('inventario')

@login_required
def filtro_nombre(request):
    if request.method == "POST":
        search = ''
        form = SearchForm(request.POST)
        if form.is_valid(): 
            search = form.cleaned_data['search_word']
            print(search)

    form = ProductoForm()
    search_form = SearchForm()
    productos = Producto.objects.filter(nombre__contains=search).order_by('nombre')
    
    context = {'productos': productos, 'form': form, 'search_form': search_form}
    return render(request, 'expiry_dates/inventario.html', context)

@login_required
def filtro_nombre_historico(request):
    if request.method == "POST":
        search = ''
        form = SearchForm(request.POST)
        if form.is_valid(): 
            search = form.cleaned_data['search_word']
            print(search)

    search_form = SearchForm()
    productos = Historico.objects.filter(nombre__contains=search).order_by('nombre')
    
    context = {'productos': productos, 'search_form': search_form}
    return render(request, 'expiry_dates/historico.html', context)