from .models import Audio, Agente
from django import forms
import django_filters

class ReporteFilter(django_filters.FilterSet):
    
    class Meta:
        model = Audio
        fields = {'ponderacion': ['lt'],
                    'agente__nombre':['icontains'],
                    'idInteraccion':['icontains']}
                    #'campaña__nombre':['icontains']}
        #fields = ['ponderacion','nombre_agente','nombre_audio','nombre_campaña']