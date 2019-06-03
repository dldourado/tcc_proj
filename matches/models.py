from django.db import models
from summoner.models import Summoner

class MatchBySummoner(models.Model):
	summoner = models.ForeignKey(Summoner, null=True, on_delete=models.SET_NULL)
	lane = models.CharField(max_length=128)
	gameId = models.CharField(max_length=128)
	champion = models.PositiveIntegerField()
	platformId = models.CharField(max_length=128)	
	season = models.PositiveIntegerField()	
	queue = models.PositiveIntegerField()	
	role  = models.CharField(max_length=128)	
	timestamp = models.CharField(max_length=128)

	def __str__(self):
		return self.summoner.summonerName+'-'+self.gameId

class Match(models.Model):
	seasonId = models.PositiveIntegerField()
	queueId = models.PositiveIntegerField()
	gameId = models.CharField(max_length=128)	
	participantIdentities = models.TextField()#summonerName-participantId
	gameVersion = models.CharField(max_length=128)
	platformId = models.CharField(max_length=128)
	gameMode = models.CharField(max_length=128)
	mapId = models.PositiveIntegerField()
	gameType = models.CharField(max_length=128)
	#teams List[TeamStatsDto]
	#participants List[ParticipantDto]
	gameDuration = models.CharField(max_length=128)
	gameCreation = models.CharField(max_length=128)
# Create your models here.
