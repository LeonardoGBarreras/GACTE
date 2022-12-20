from dataclasses import dataclass
from email import message
import imp
from tkinter.tix import Form
from django.shortcuts import render,redirect,get_object_or_404
from .models import CrearEvento, Evento
from .forms import CrearEventoForm, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required,permission_required


def home(request):

    return render(request, 'app/home.html')

@permission_required ('app.add_crear evento')
def crearevento(request):
    
    data = {
        'form' : CrearEventoForm()
    }
    if request.method == "POST":
        formulario = CrearEventoForm (data=request.POST)
        if formulario.is_valid():
            formulario.save()
            
        else :
            data ['form'] = formulario
    return render(request, 'app/crearevento.html',data)

   
def eventos(request):
    eventos = CrearEvento.objects.all()
    data = {
        'eventos': eventos 
    }
    return render(request, 'app/eventos.html',data)

@permission_required ('app.change_crear evento') 
def modificar(request,id):

    evento = get_object_or_404(CrearEvento, id=id)
    data = {
        'form': CrearEventoForm(instance=evento)
        }
    if request.method == "POST":
        formulario = CrearEventoForm (data=request.POST, instance=evento)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Modificado Correctamente")
            return redirect (to=eventos)
        else :
            data ['form'] = formulario
    
    return render (request,'app/modificar.html',data)

@permission_required ('app.delete_crear evento') 
def eliminar(request,id):
    
    evento = get_object_or_404(CrearEvento,id=id)
    evento.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect ( to = eventos)


def registro( request):
    data = {
       'form' : CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            login(request,user)
          
            return redirect(to="home")
        data [ "form"]  = formulario
    return render(request, 'registration/registro.html',data)

 
# Create your views here.
