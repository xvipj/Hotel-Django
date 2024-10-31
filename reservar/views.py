from django.shortcuts import render, redirect
from .forms import ReservaForm
from datetime import time

def home(request):
    MAX_NOCHES = 5  # Límite de noches permitido

    if request.method == "POST":
        form = ReservaForm(request.POST) 
        if form.is_valid():
            # Obtenemos las fechas de entrada y salida del formulario
            fecha_entrada = form.cleaned_data.get('fecha_entrada')
            fecha_salida = form.cleaned_data.get('fecha_salida')
            
            # Calculamos el número de noches y verificamos el límite
            numero_de_dias = (fecha_salida - fecha_entrada).days
            numero_de_noches = abs(numero_de_dias - 1)
            if numero_de_noches <= MAX_NOCHES:
                form.save()  # Guarda la reserva si es válida
                return redirect('home')
            else:
                context = {
                    'form': form,
                    'mensaje': "Superas el número de noches permitido. Por favor, comuníquese al +57 3248076520"
                }
                return render(request, 'home.html', context)  # Renderiza la página con mensaje de error
    else:
        form = ReservaForm()
        return render(request, 'home.html', {'form': form})
