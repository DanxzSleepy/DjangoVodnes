from django.urls import path, include
from . import views

app_name = 'AvoidNess'

urlpatterns = [
    path('', views.Avoidness, name='avoidness', ),
    path('AkumaVerse/', views.Akumaverse, name='akumaverse', ),
    path('LumenCore/', views.LumenCore, name='lumencore', ),
    path('NoctForge/', views.NoctForge, name='noctforge', )  
]
