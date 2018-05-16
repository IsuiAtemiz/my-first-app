from django.db import models
from django.utils import timezone

# Create your models here.	
class Persona(models.Model):
	#SEXO
	HOMBRE = 'H'
	MUJER = 'M'
	SEXO_CHOICE = (
		(HOMBRE, 'H'),
		(MUJER, 'M'),
	)
	
	#DISTRITO
	UNO = 1
	DOS = 2
	TRES = 3
	DISTRITO_CHOICE = (
		(UNO, 1),
		(DOS, 2),
		(TRES, 3),
	
	)
	
	nombre = models.CharField(max_length = 50)
	a_paterno = models.CharField(max_length = 50)
	a_materno = models.CharField(max_length = 50)
	distrito = models.IntegerField(choices = DISTRITO_CHOICE)
	clave_resp = models.PositiveIntegerField(primary_key = True)
	password = models.CharField(max_length = 12)
	puesto = models.CharField(max_length = 5)
	sexo = models.CharField(max_length = 2, choices = SEXO_CHOICE)