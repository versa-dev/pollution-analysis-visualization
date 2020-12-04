from django.db import models

# Create your models here.
class PollutionData(models.Model):
	id = models.AutoField(primary_key=True)
	# type = 
	typeid = models.IntegerField()
	so2 = models.DecimalField(max_digits=20, decimal_places=4)
	no2 = models.DecimalField(max_digits=20, decimal_places=4)
	pm10 = models.DecimalField(max_digits=20, decimal_places=4)
	co = models.DecimalField(max_digits=20, decimal_places=4)
	o3_8 = models.DecimalField(max_digits=20, decimal_places=4)
	pm25 = models.DecimalField(max_digits=20, decimal_places=4)
	receptor = models.CharField(max_length=30)
	wind_direction = models.IntegerField()
	wind_speed = models.DecimalField(max_digits=20, decimal_places=2)
	humidity = models.DecimalField(max_digits=20, decimal_places=2)
	temperature = models.DecimalField(max_digits=20, decimal_places=2)
	date = models.IntegerField()
	city = models.CharField(max_length=30)

class Vehicle(models.Model):
	id = models.AutoField(primary_key=True)
	engine_family = models.CharField(max_length=100)
	manufacturer = models.CharField(max_length=100)
	engine_code = models.CharField(max_length=30)
	engine_model = models.CharField(max_length=30)

class City(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=30)
	latitude = models.DecimalField(max_digits=20, decimal_places=4)
	longitude = models.DecimalField(max_digits=20, decimal_places=4)
	state = models.CharField(max_length=50)
	def __str__(self):
		return self.name