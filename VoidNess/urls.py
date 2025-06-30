from django.urls import path, include
from . import views

app_name = 'AvoidNess'

urlpatterns = [
    path('', views.Avoidness, name='avoidness', ),
    path('Akumaverse/', views.Akumaverse, name='akumaverse', ),
    path('Lumencore/', views.LumenCore, name='lumencore', ),
    path('Noctforge/', views.NoctForge, name='noctforge', )  
]
