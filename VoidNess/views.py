from django.shortcuts import render

# Create your views here.
def Avoidness(request):
    return render(request, 'VoidNess/avoidness.html')

def Akumaverse(request):
    return render(request, 'VoidNess/akumaverse.html')  

def LumenCore(request):
    return render(request, 'VoidNess/lumencore.html')

def NoctForge(request):
    return render(request, 'VoidNess/noctforge.html')  
