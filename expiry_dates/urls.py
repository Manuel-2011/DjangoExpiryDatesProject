from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import ExtendedAuthenticationForm

urlpatterns = [
    path('', views.inventario, name="inventario"),
    path('delete/<int:producto_id>', views.producto_delete, name="producto_delete"),
    path('filter', views.filtro_nombre, name="filtro_nombre"),
    path('historico/', views.historico, name="historico"),
    path('historico/filter', views.filtro_nombre_historico, name="filtro_historico"),
    path('login/', auth_views.LoginView.as_view(template_name="expiry_dates/login.html", authentication_form=ExtendedAuthenticationForm), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
]