from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Campaña(models.Model):
	nombre = models.CharField(max_length=80, unique=True)
	
	def __str__(self):
		return self.nombre
	
class Agente(models.Model):
	nombre = models.CharField(max_length=60, unique=True, default="")

class Audio(models.Model):
	file = models.FileField(upload_to='audios/files/',default=None)
	inicio = models.DateTimeField(default=None)
	idInteraccion = models.CharField(max_length=60,default=None, unique=True)
	agente = models.ForeignKey(Agente, related_name='agente', on_delete=models.CASCADE,default=None)
	campaña = models.ForeignKey(Campaña, related_name='campaña_audio', on_delete=models.CASCADE,default=None)
	canal_1 = models.TextField(max_length=4000, default="")
	canal_2 = models.TextField(max_length=4000, default="")

	
	def __str__(self):
		#return self.title
		return str(self.idInteraccion)
	
	
	def delete(self, *args):
		self.file.delete()
		super().delete(*args)

class Funcion(models.Model):
	HABILITADO = 1
	DESHABILITADO = 2
	ESTADOS = ((HABILITADO, 'Habilitado'),(DESHABILITADO, 'Deshabilitado'))
	
	nombre = models.CharField(max_length=30, unique=True)
	descripcion = models.CharField(max_length=255)
	frase = models.CharField(max_length=255, default="")
	ponderacion = models.IntegerField(default=0)
	estado = models.PositiveSmallIntegerField(choices=ESTADOS, default=2)
	
	def __str__(self):
		return self.nombre

class Palabras(models.Model):
	fk_funcion = models.ForeignKey(Funcion, related_name='funcion', on_delete=models.CASCADE)
	palabra = models.CharField(max_length=30)#, unique=True)
	porcentaje = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
	
	class Meta:
		unique_together = ("fk_funcion", "palabra"),
		
	def __str__(self):
		return self.palabra
		
class Reporte(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	ponderacion = models.IntegerField()
	fk_funcion = models.ForeignKey(Funcion, related_name='funcion_reporte', on_delete=models.CASCADE)
	fk_audio = models.ForeignKey(Audio, related_name='audio', on_delete=models.CASCADE)
	canal_1 = models.TextField()
	canal_2 = models.TextField()
	nombre = models.CharField(max_length=255)
	nombre_audio = models.CharField(max_length=255)
	
	def __str__(self):
		return self.nombre
		
#class Lote(models.Model):


	
class Campaña_funciones(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	funciones = models.ManyToManyField('Funcion',limit_choices_to = {'estado': 1})
	fk_campaña = models.ForeignKey(Campaña, related_name='fk_campaña', on_delete=models.CASCADE, default=None)
	
	def getFunciones(self):
		temp = ''
		for f in self.funciones.all():
			temp = temp+f.nombre+','
			
		return temp[:-1]

class Campaña_Audio_Analisis(models.Model):
	analisis = models.IntegerField()
	fk_audio = models.ForeignKey(Audio, related_name='fk_audio_campaña', on_delete=models.CASCADE)
	fk_campaña_funcion = models.ForeignKey(Campaña_funciones, related_name='fk_campaña_funcion', on_delete=models.CASCADE,default=None)
	fk_funcion = models.ForeignKey(Funcion, related_name='fk_funcion', on_delete=models.CASCADE,default=None)
	fk_campaña = models.ForeignKey(Campaña, related_name='campaña', on_delete=models.CASCADE)
	
	class Meta:
		unique_together = (("fk_audio", "fk_campaña_funcion","fk_campaña","fk_funcion"),)
		
