from django.db import models

class Champion(models.Model):
	name = models.CharField(max_length=50)
	nameId = models.CharField(max_length=56)
	championId = models.IntegerField(unique=True)

	def __str__(self):
		return self.name
# Create your models here.
