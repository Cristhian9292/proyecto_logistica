"""
URL configuration for logistics project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from api.views import asignar_paquete_a_transportista as asignar_paquete, actualizar_estado_de_entrega as actualizar_estado

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('paquetes/<int:cliente_id>/', views.paquetes_por_cliente, name='paquetes_por_cliente'),
    path('paquetes_por_transportista/<int:transportista_id>/', views.paquetes_por_transportista, name='paquetes_por_transportista'),
    path('paquetes/crear/', views.PaqueteCreateView.as_view(), name='paquete_crear'),
    path('paquetes/<int:pk>/editar/', views.PaqueteUpdateView.as_view(), name='paquete_editar'),
    path('paquetes/<int:pk>/eliminar/', views.PaqueteDeleteView.as_view(), name='paquete_eliminar'),
    path('asignar_paquete', asignar_paquete, name='asignar_paquete'),
    path('paquete/<int:paquete_id>/actualizar_estado', actualizar_estado, name='actualizar_estado'),
]
