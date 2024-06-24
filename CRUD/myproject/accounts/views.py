# accounts/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento
from .forms import EventoForm

def criar_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_eventos')
    else:
        form = EventoForm()
    return render(request, 'accounts/criar_evento.html', {'form': form})

def listar_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'accounts/listar_eventos.html', {'eventos': eventos})

def atualizar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('listar_eventos')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'accounts/atualizar_evento.html', {'form': form})

def deletar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    if request.method == 'POST':
        evento.delete()
        return redirect('listar_eventos')
    return render(request, 'accounts/deletar_evento.html', {'evento': evento})

def home_view(request):
    return redirect('listar_eventos')
