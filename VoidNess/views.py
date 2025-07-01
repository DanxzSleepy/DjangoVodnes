from django.shortcuts import render
from .forms import ideiasForm


# Create your views here.
def Avoidness(request):
    return render(request, 'VoidNess/AvoidNess-Creative_Hub.html')

def Akumaverse(request):
    return render(request, 'VoidNess/Akumaverse-Dimensão_Sombria.html')  

def LumenCore(request):
    return render(request, 'VoidNess/LumenCore-Dimensão_do_Conhecimento.html')

def NoctForge(request):
    contexto = {
       
    }
    return render(request, 'VoidNess/NoctForge-Forja_de_Ideias.html')  

def form(request):
    
    return render(request, 'form.html', {'form': ideiasForm})
