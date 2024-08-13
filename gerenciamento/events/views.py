from django.shortcuts import render, redirect
from .forms import EventoForm
from .models import Evento


def listar(request):
    events = Evento.objects.all()
    return render(request, 'events/listar.html', {'events': events})

def cadastrar(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = EventoForm()
    return render(request, 'events/cadastrar.html', {'form': form})
