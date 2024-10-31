from django.shortcuts import render, redirect
from .forms import ReservaForm
from datetime import time

def home(request):
    if request.method == "POST":
        form = ReservaForm(request.POST) 
        if form.is_valid():
            # Accede a las fechas de entrada y salida
            fecha_entrada = form.cleaned_data.get('fecha_entrada')
            fecha_salida = form.cleaned_data.get('fecha_salida')

            # Calcula el número de días entre las dos fechas
            numero_de_dias = (fecha_salida - fecha_entrada).days

            # Calcula el número de noches como un valor positivo
            numero_de_noches = abs(numero_de_dias - 1)

            # Verifica si el número de noches está dentro del límite permitido (5 noches)
            if numero_de_noches <= 5:
                form.save()  # Guarda la reserva si es válida
                return redirect('home')
            else:
                # Contexto cuando el número de noches excede el límite permitido
                context = {
                    'form': form,
                    'mensaje': "Superas el número de noches permitido. Por favor, comuníquese al +57 3248076520"
                }
                return render(request, 'home.html', context)  # Renderiza la página con mensaje de error
    else:
        form = ReservaForm()
        # Renderiza la página inicial con el formulario
        return render(request, 'home.html', {'form': form})