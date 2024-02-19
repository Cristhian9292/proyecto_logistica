from .models import Paquete, Cliente, Transportista
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def inicio(request):
    return render(request, 'logistics/inicio.html')

def paquetes_por_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    paquetes = Paquete.objects.filter(cliente=cliente)
    
    if paquetes.exists():
        return render(request, 'logistics/paquetes_por_cliente.html', {'cliente': cliente, 'paquetes': paquetes})
    else:
        return render(request, 'logistics/sin_paquetes.html', {'cliente': cliente})


def paquetes_por_transportista(request, transportista_id):
    transportista = Transportista.objects.get(id=transportista_id)
    paquetes = Paquete.objects.filter(transportista=transportista)
    return render(request, 'logistics/paquetes_por_transportista.html', {'paquetes': paquetes})

class PaqueteCreateView(CreateView):
    model = Paquete
    fields = ['cliente','peso', 'dimensiones', 'direccion_origen', 'direccion_destino', 'estado_entrega']
    template_name = 'logistics/paquete_form.html'
    success_url = reverse_lazy('inicio')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clientes'] = Cliente.objects.all()
        return context

class PaqueteUpdateView(UpdateView):
    model = Paquete
    fields = ['peso', 'dimensiones', 'direccion_origen', 'direccion_destino', 'estado_entrega']
    template_name = 'logistics/paquete_form.html'
    success_url = reverse_lazy('inicio')

class PaqueteDeleteView(DeleteView):
    model = Paquete
    success_url = reverse_lazy('inicio')

