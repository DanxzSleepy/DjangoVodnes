from django.shortcuts import render

# Create your views here.
def Avoidness(request):
    return render(request, 'VoidNess/AvoidNess-Creative_Hub.html')

def Akumaverse(request):
    return render(request, 'VoidNess/Akumaverse-Dimensão_Sombria.html')  

def LumenCore(request):
    return render(request, 'VoidNess/LumenCore-Dimensão_do_Conhecimento.html')

def NoctForge(request):
    return render(request, 'VoidNess/NoctForge-Forja_de_Ideias.html')  
