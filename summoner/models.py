from django.db import models

class Summoner(models.Model):
	summonerName = models.CharField(max_length=50)
	accountId = models.CharField(max_length=56)
	leaguePoints = models.IntegerField(default=0)

	def __str__(self):
		return self.summonerName
# Create your models here.
