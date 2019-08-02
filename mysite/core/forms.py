from django import forms

from .models import Audio, Funcion, Palabras, Campaña, Reporte


class AudioForm(forms.ModelForm):
    #a = Agente.objects.get(id=915)
    #agente = forms.IntegerField(widget=forms.HiddenInput(), initial=915)
    #campaña = forms.IntegerField(widget=forms.HiddenInput(), initial=98)
    class Meta:
        model = Audio
        fields = ('id','file','idInteraccion','agente','campaña')

class ComentarioAudioForm(forms.ModelForm):
	class Meta:
		model = Audio
		fields = ('comentario','id')

class ComentarioReporteForm(forms.ModelForm):
	class Meta:
		model = Reporte
		fields = ('comentario','id')

		
class FuncionForm(forms.ModelForm):
	class Meta:
		model = Funcion
		fields = ('nombre', 'descripcion')
		
class PalabraForm(forms.ModelForm):
	class Meta:
		model = Palabras
		fields = ('palabra','porcentaje','fk_funcion')
		widgets = {'fk_funcion': forms.HiddenInput()}
		
#class AnalisisForm(forms.ModelForm):
	#widgets={'funciones':forms.CheckboxSelectMultiple}
#	class Meta:
#		model = Analisis
#		fields = ('funciones','fk_campaña')
#		widgets = {'fk_campaña': forms.HiddenInput()}

class CampañaFuncionForm(forms.ModelForm):
	class Meta:
		model = Campaña
		fields = ('fk_funciones',)