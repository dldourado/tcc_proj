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

class TeamStatsByMatch(models.Model):
	match = models.ForeignKey(Match, null=True, on_delete=models.CASCADE)
	firstDragon	= models.BooleanField()
	firstInhibitor	= models.BooleanField()
	bans =  models.TextField()#pickTurn-championId;
	baronKills = models.PositiveIntegerField()#	int	Number of times the team killed Baron.
	firstRiftHerald	= models.BooleanField()
	firstBaron	= models.BooleanField()
	riftHeraldKills = models.PositiveIntegerField()#	int	Number of times the team killed Rift Herald.
	firstBlood	= models.BooleanField()
	teamIsBlue = models.BooleanField()#= teamId	int	100 for blue side. 200 for red side.
	firstTower	= models.BooleanField()
	inhibitorKills = models.PositiveIntegerField()
	towerKills = models.PositiveIntegerField()
	win	= models.BooleanField()
	dragonKills = models.PositiveIntegerField()

class ParticipantStatsByMatch(models.Model):
	match = models.ForeignKey(Match, null=True, on_delete=models.CASCADE)
	participantId = models.IntegerField()
	#timeline	ParticipantTimelineDto	Participant timeline data.
	teamIsBlue = models.BooleanField()#= teamId	int	100 for blue side. 200 for red side.
	spell1Id = models.IntegerField()
	spell2Id = models.IntegerField()
	highestAchievedSeasonTier = models.CharField(max_length=128)
	championId = models.IntegerField()

class StatsByParticipant(models.Model):
	participant = models.ForeignKey(ParticipantStatsByMatch, null=True, on_delete=models.CASCADE)
	magicDamageDealtToChampions = models.IntegerField()
	damageDealtToObjectives = models.IntegerField()
	damageDealtToTurrets = models.IntegerField()
	physicalDamageDealtToChampions = models.IntegerField()
	magicDamageDealt = models.IntegerField()
	damageSelfMitigated = models.IntegerField()
	magicalDamageTaken = models.IntegerField()
	trueDamageTaken = models.IntegerField()
	trueDamageDealt = models.IntegerField()
	totalDamageTaken = models.IntegerField()
	physicalDamageDealt = models.IntegerField()
	totalDamageDealtToChampions = models.IntegerField()
	physicalDamageTaken = models.IntegerField()
	totalDamageDealt = models.IntegerField()
	trueDamageDealtToChampions = models.IntegerField()
	totalHeal = models.IntegerField()
	perk0Var1 = models.IntegerField()
	perk0Var2 = models.IntegerField()
	perk0Var3 = models.IntegerField()
	perk1Var1 = models.IntegerField()
	perk1Var2 = models.IntegerField()
	perk1Var3 = models.IntegerField()
	perk2Var1 = models.IntegerField()
	perk2Var2 = models.IntegerField()
	perk2Var3 = models.IntegerField()
	perk3Var1 = models.IntegerField()
	perk3Var2 = models.IntegerField()
	perk3Var3 = models.IntegerField()
	perk4Var1 = models.IntegerField()
	perk4Var2 = models.IntegerField()
	perk4Var3 = models.IntegerField()
	perk5Var1 = models.IntegerField()
	perk5Var2 = models.IntegerField()
	perk5Var3 = models.IntegerField()
	perk0 = models.IntegerField()
	perk2 = models.IntegerField()
	perk1 = models.IntegerField()
	perk3 = models.IntegerField()
	perk4 = models.IntegerField()
	perk5 = models.IntegerField()
	perkPrimaryStyle = models.IntegerField()
	perkSubStyle = models.IntegerField()
	timeCCingOthers = models.IntegerField()
	totalTimeCrowdControlDealt = models.IntegerField()
	longestTimeSpentLiving = models.IntegerField()
	firstBloodKill = models.BooleanField()	
	kills = models.IntegerField()
	doubleKills = models.IntegerField()	
	tripleKills = models.IntegerField()
	quadraKills = models.IntegerField()
	pentaKills = models.IntegerField()
	unrealKills = models.IntegerField()	
	killingSprees = models.IntegerField()	
	largestMultiKill = models.IntegerField()
	largestKillingSpree = models.IntegerField()
	assists = models.IntegerField()	
	firstBloodAssist = models.BooleanField()
	deaths = models.IntegerField()	
	playerScore0 = models.IntegerField()
	playerScore1 = models.IntegerField()
	playerScore2 = models.IntegerField()
	playerScore3 = models.IntegerField()
	playerScore4 = models.IntegerField()
	playerScore5 = models.IntegerField()
	playerScore6 = models.IntegerField()
	playerScore7 = models.IntegerField()
	playerScore8 = models.IntegerField()
	playerScore9 = models.IntegerField()
	totalScoreRank = models.IntegerField()
	neutralMinionsKilled = models.IntegerField()
	neutralMinionsKilledTeamJungle = models.IntegerField()	
	neutralMinionsKilledEnemyJungle = models.IntegerField()	
	totalMinionsKilled = models.IntegerField()
	totalUnitsHealed = models.IntegerField()
	largestCriticalStrike = models.IntegerField()
	item0 = models.IntegerField()	
	item1 = models.IntegerField()	
	item2 = models.IntegerField()	
	item3 = models.IntegerField()	
	item4 = models.IntegerField()	
	item5 = models.IntegerField()	
	item6 = models.IntegerField()	
	goldSpent = models.IntegerField()	
	goldEarned = models.IntegerField()	
	champLevel = models.IntegerField()	
	firstInhibitorKill = models.BooleanField()	
	inhibitorKills = models.IntegerField()	
	firstInhibitorAssist = models.BooleanField()	
	firstTowerAssist = models.BooleanField()	
	firstTowerKill = models.BooleanField()	
	turretKills = models.IntegerField()
	combatPlayerScore = models.IntegerField()	
	participantId = models.IntegerField()	
	sightWardsBoughtInGame = models.IntegerField()	
	visionWardsBoughtInGame = models.IntegerField()	
	wardsPlaced = models.IntegerField()	
	wardsKilled = models.IntegerField()
	totalPlayerScore = models.IntegerField()	
	visionScore = models.IntegerField()
	objectivePlayerScore = models.IntegerField()
	win = models.BooleanField()

class FrameByMatch(models.Model):
	match = models.ForeignKey(Match, null=True, on_delete=models.CASCADE)
	timestamp = models.IntegerField()

class ParticipantByFrame(models.Model):
	frame = models.ForeignKey(FrameByMatch, null=True, on_delete=models.CASCADE)
	totalGold = models.IntegerField()	
	teamScore = models.IntegerField()	
	participantId = models.IntegerField()	
	level = models.IntegerField()	
	currentGold = models.IntegerField()	
	minionsKilled = models.IntegerField()	
	dominionScore = models.IntegerField()	
	position = models.CharField(max_length=40)#x-y;
	xp = models.IntegerField()	
	jungleMinionsKilled = models.IntegerField()

class EventByFrame(models.Model):
	frame = models.ForeignKey(FrameByMatch, null=True, on_delete=models.CASCADE)
	eventType = models.CharField(max_length=64, blank=True, null=True)
	towerType = models.CharField(max_length=64, blank=True, null=True)
	teamId = models.IntegerField(blank=True, null=True)
	ascendedType = models.CharField(max_length=64, blank=True, null=True)
	killerId = models.IntegerField(blank=True, null=True)
	levelUpType = models.CharField(max_length=64, blank=True, null=True)
	pointCaptured = models.CharField(max_length=64, blank=True, null=True)
	assistingParticipantIds = models.CharField(max_length=40, blank=True, null=True)#x-y-z-w;
	wardType = models.CharField(max_length=64, blank=True, null=True)
	monsterType = models.CharField(max_length=64, blank=True, null=True)
	eType = models.CharField(max_length=64, blank=True, null=True)
	skillSlot = models.IntegerField(blank=True, null=True)
	victimId = models.IntegerField(blank=True, null=True)
	timestamp = models.CharField(max_length=128, blank=True, null=True)	
	afterId = models.IntegerField(blank=True, null=True)
	monsterSubType = models.CharField(max_length=64, blank=True, null=True)
	laneType = models.CharField(max_length=64, blank=True, null=True)
	itemId = models.IntegerField(blank=True, null=True)
	participantId = models.IntegerField(blank=True, null=True)
	buildingType = models.CharField(max_length=64, blank=True, null=True)
	creatorId = models.IntegerField(blank=True, null=True)
	position = models.CharField(max_length=40, blank=True, null=True)#x-y
	beforeId = models.IntegerField(blank=True, null=True)

# class TimelineByParticipant(models.Model):
# 	participant = models.ForeignKey(ParticipantStatsByMatch, null=True, on_delete=models.SET_NULL)
# 	lane = models.CharField(max_length=20)
# 	role = models.CharField(max_length=20)
# 	participantId = models.IntegerField()
# 	csDiffPerMinDeltas	Map[String, double]	Creep score difference versus the calculated lane opponent(s) for a specified period.
# 	goldPerMinDeltas	Map[String, double]	Gold for a specified period.
# 	xpDiffPerMinDeltas	Map[String, double]	Experience difference versus the calculated lane opponent(s) for a specified period.
# 	creepsPerMinDeltas	Map[String, double]	Creeps for a specified period.
# 	xpPerMinDeltas	Map[String, double]	Experience change for a specified period.
# 	damageTakenDiffPerMinDeltas	Map[String, double]	Damage taken difference versus the calculated lane opponent(s) for a specified period.
# 	damageTakenPerMinDeltas	Map[String, double]	
