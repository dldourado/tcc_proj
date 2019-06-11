from summoner.models import Summoner
from .models import MatchBySummoner, Match, TeamStatsByMatch, ParticipantStatsByMatch, StatsByParticipant, FrameByMatch, ParticipantByFrame, EventByFrame
from request_maker.utils import make_request
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

NUMERO_PARTIDAS = 20

def get_matches_by_summoner():
	summoners = Summoner.objects.all()
	for player in summoners:
		error = True
		while error:
			matchList = make_request('match/v4/matchlists/by-account/%s' % player.accountId, {'endIndex':NUMERO_PARTIDAS})
			try:
				for match in matchList['matches']:
					#matchInfo = make_request('match/v4/matches/%s' % match['gameId'], None)
					#print(match)
					MatchBySummoner.objects.get_or_create(
						summoner = player,
						lane = match['lane'],
						gameId = match['gameId'],
						champion = match['champion'],
						platformId = match['platformId'],
						season = match['season'],
						queue = match['queue'],
						role  = match['role'],
						timestamp = match['timestamp']
					)
				error = False	
			except KeyError:
				print('keyerror')
				error = True

def get_matches():
	matches = MatchBySummoner.objects.all()
	for match in matches[:20]:
		try:
			Match.objects.get(gameId=match.gameId)

		except ObjectDoesNotExist as e:

			error = True
			while error:
				matchInfo = make_request('match/v4/matches/%s' % match.gameId, None)
				try:
					#for matchInfo in matchInfos:
					text = ''
					for p in matchInfo['participantIdentities']:
						#print(p)
						text+=p['player']['summonerName']+':'+str(p['participantId'])+(';' if p!=matchInfo['participantIdentities'][-1] else '')
					#print(text)
					match_criada = Match.objects.create(
						seasonId = matchInfo['seasonId'],
						queueId = matchInfo['queueId'],
						gameId = matchInfo['gameId'],
						participantIdentities = text,
						gameVersion = matchInfo['gameVersion'],
						platformId = matchInfo['platformId'],
						gameMode = matchInfo['gameMode'],
						mapId = matchInfo['mapId'],
						gameType = matchInfo['gameType'],
						gameDuration = matchInfo['gameDuration'],
						gameCreation = matchInfo['gameCreation']
					)
					if match_criada.queueId == 420:
						for team in matchInfo['teams']:
							bans = ''
							for ban in team['bans']:
								bans += str(ban['pickTurn'])+':'+str(ban['championId'])+(';' if ban!=team['bans'][-1] else '')
							teamStat = TeamStatsByMatch.objects.get_or_create(
								match = match_criada,
								firstDragon = team['firstDragon'],
								firstInhibitor = team['firstInhibitor'],
								bans = bans,
								baronKills = team['baronKills'],
								firstRiftHerald = team['firstRiftHerald'],
								firstBaron = team['firstBaron'],
								riftHeraldKills = team['riftHeraldKills'],
								firstBlood = team['firstBlood'],
								teamIsBlue = True if team['teamId']==100 else False,
								firstTower = team['firstTower'],
								inhibitorKills = team['inhibitorKills'],
								towerKills = team['towerKills'],
								win = True if team['win'] == 'Win' else False,
								dragonKills = team['dragonKills']
							)
						for participant in matchInfo['participants']:
							try:
								participant_criado = ParticipantStatsByMatch.objects.get(match=match_criada, participantId=participant['participantId'])

							except ObjectDoesNotExist as e:
								participant_criado = ParticipantStatsByMatch.objects.create(
									match = match_criada,
									participantId = participant['participantId'],
									teamIsBlue =  True if participant['teamId']==100 else False,
									spell1Id = participant['spell1Id'],
									spell2Id = participant['spell2Id'],
									highestAchievedSeasonTier = participant['highestAchievedSeasonTier'] if 'highestAchievedSeasonTier' in participant else '',
									championId = participant['championId'],
								)
							#print(participant['stats'])
							particípant_stat_criado = StatsByParticipant.objects.get_or_create(
								participant = participant_criado,
								magicDamageDealtToChampions = participant['stats']['magicDamageDealtToChampions'],
								damageDealtToObjectives = participant['stats']['damageDealtToObjectives'],
								damageDealtToTurrets = participant['stats']['damageDealtToTurrets'],
								physicalDamageDealtToChampions = participant['stats']['physicalDamageDealtToChampions'],
								magicDamageDealt = participant['stats']['magicDamageDealt'],
								damageSelfMitigated = participant['stats']['damageSelfMitigated'],
								magicalDamageTaken = participant['stats']['magicalDamageTaken'],
								trueDamageTaken = participant['stats']['trueDamageTaken'],
								trueDamageDealt = participant['stats']['trueDamageDealt'],
								totalDamageTaken = participant['stats']['totalDamageTaken'],
								physicalDamageDealt = participant['stats']['physicalDamageDealt'],
								totalDamageDealtToChampions = participant['stats']['totalDamageDealtToChampions'],
								physicalDamageTaken = participant['stats']['physicalDamageTaken'],
								totalDamageDealt = participant['stats']['totalDamageDealt'],
								trueDamageDealtToChampions = participant['stats']['trueDamageDealtToChampions'],
								totalHeal = participant['stats']['totalHeal'],
								perk0Var1 = participant['stats']['perk0Var1'],
								perk0Var2 = participant['stats']['perk0Var2'],
								perk0Var3 = participant['stats']['perk0Var3'],
								perk1Var1 = participant['stats']['perk1Var1'],
								perk1Var2 = participant['stats']['perk1Var2'],
								perk1Var3 = participant['stats']['perk1Var3'],
								perk2Var1 = participant['stats']['perk2Var1'],
								perk2Var2 = participant['stats']['perk2Var2'],
								perk2Var3 = participant['stats']['perk2Var3'],
								perk3Var1 = participant['stats']['perk3Var1'],
								perk3Var2 = participant['stats']['perk3Var2'],
								perk3Var3 = participant['stats']['perk3Var3'],
								perk4Var1 = participant['stats']['perk4Var1'],
								perk4Var2 = participant['stats']['perk4Var2'],
								perk4Var3 = participant['stats']['perk4Var3'],
								perk5Var1 = participant['stats']['perk5Var1'],
								perk5Var2 = participant['stats']['perk5Var2'],
								perk5Var3 = participant['stats']['perk5Var3'],
								perk0 = participant['stats']['perk0'],
								perk2 = participant['stats']['perk2'],
								perk1 = participant['stats']['perk1'],
								perk3 = participant['stats']['perk3'],
								perk4 = participant['stats']['perk4'],
								perk5 = participant['stats']['perk5'],
								perkPrimaryStyle = participant['stats']['perkPrimaryStyle'],
								perkSubStyle = participant['stats']['perkSubStyle'],
								timeCCingOthers = participant['stats']['timeCCingOthers'],
								totalTimeCrowdControlDealt = participant['stats']['totalTimeCrowdControlDealt'],
								longestTimeSpentLiving = participant['stats']['longestTimeSpentLiving'],
								firstBloodKill = participant['stats']['firstBloodKill'],
								kills = participant['stats']['kills'],
								doubleKills = participant['stats']['doubleKills'],
								tripleKills = participant['stats']['tripleKills'],
								quadraKills = participant['stats']['quadraKills'],
								pentaKills = participant['stats']['pentaKills'],
								unrealKills = participant['stats']['unrealKills'],
								killingSprees = participant['stats']['killingSprees'],
								largestMultiKill = participant['stats']['largestMultiKill'],
								largestKillingSpree = participant['stats']['largestKillingSpree'],
								assists = participant['stats']['assists'],
								firstBloodAssist = participant['stats']['firstBloodAssist'],
								deaths = participant['stats']['deaths'],
								playerScore0 = participant['stats']['playerScore0'],
								playerScore1 = participant['stats']['playerScore1'],
								playerScore2 = participant['stats']['playerScore2'],
								playerScore3 = participant['stats']['playerScore3'],
								playerScore4 = participant['stats']['playerScore4'],
								playerScore5 = participant['stats']['playerScore5'],
								playerScore6 = participant['stats']['playerScore6'],
								playerScore7 = participant['stats']['playerScore7'],
								playerScore8 = participant['stats']['playerScore8'],
								playerScore9 = participant['stats']['playerScore9'],
								totalScoreRank = participant['stats']['totalScoreRank'],
								neutralMinionsKilled = participant['stats']['neutralMinionsKilled'],
								neutralMinionsKilledTeamJungle = participant['stats']['neutralMinionsKilledTeamJungle'],
								neutralMinionsKilledEnemyJungle = participant['stats']['neutralMinionsKilledEnemyJungle'],
								totalMinionsKilled = participant['stats']['totalMinionsKilled'],
								totalUnitsHealed = participant['stats']['totalUnitsHealed'],
								largestCriticalStrike = participant['stats']['largestCriticalStrike'],
								item0 = participant['stats']['item0'],
								item1 = participant['stats']['item1'],
								item2 = participant['stats']['item2'],
								item3 = participant['stats']['item3'],
								item4 = participant['stats']['item4'],
								item5 = participant['stats']['item5'],
								item6 = participant['stats']['item6'],
								goldSpent = participant['stats']['goldSpent'],
								goldEarned = participant['stats']['goldEarned'],
								champLevel = participant['stats']['champLevel'],
								firstInhibitorKill = participant['stats']['firstInhibitorKill'] if 'firstInhibitorKill' in participant['stats'] else False,
								inhibitorKills = participant['stats']['inhibitorKills'],
								firstInhibitorAssist = participant['stats']['firstInhibitorAssist'] if 'firstInhibitorAssist' in participant['stats'] else False,
								firstTowerAssist = participant['stats']['firstTowerAssist'] if 'firstTowerAssist' in participant['stats'] else False,
								firstTowerKill = participant['stats']['firstTowerKill'] if 'firstTowerKill' in participant['stats'] else False,
								turretKills = participant['stats']['turretKills'],
								combatPlayerScore = participant['stats']['combatPlayerScore'],
								participantId = participant['stats']['participantId'],
								sightWardsBoughtInGame = participant['stats']['sightWardsBoughtInGame'],
								visionWardsBoughtInGame = participant['stats']['visionWardsBoughtInGame'],
								wardsPlaced = participant['stats']['wardsPlaced'],
								wardsKilled = participant['stats']['wardsKilled'],
								totalPlayerScore = participant['stats']['totalPlayerScore'],
								visionScore = participant['stats']['visionScore'],
								objectivePlayerScore = participant['stats']['objectivePlayerScore'],
								win = participant['stats']['win']
							)
					error = False	
				except KeyError:
					print('keyerror')
					error = True

			#print(e)
		except MultipleObjectsReturned:			
			objs = Match.objects.filter(gameId=match.gameId)
			for obj in objs:
				if obj!=objs[0]:
					obj.delete()

def get_timelines():
	matches = Match.objects.all()
	for match in matches:
		error = True
		while error:
			timelines = make_request('match/v4/timelines/by-match/%s' % match.gameId, {'includeTimeline':'true', 'frameInterval':'1000'})#None)
			try:
				for frame in timelines['frames']:
					frame_criado = FrameByMatch.objects.get_or_create(
						match = match,
						timestamp = frame['timestamp']
					)
					print(frame['participantFrames'])
					for key, participantFrame in frame['participantFrames'].items():
						print(participantFrame)
						pf = ParticipantByFrame.objects.get_or_create(
							frame = frame_criado,
							totalGold = participantFrame['totalGold'],
							teamScore = participantFrame['teamScore'],
							participantId = participantFrame['participantId'],
							level = participantFrame['level'],
							currentGold = participantFrame['currentGold'],
							minionsKilled = participantFrame['minionsKilled'],
							dominionScore = participantFrame['dominionScore'],
							position = participantFrame['position'],
							xp = participantFrame['xp'],
							jungleMinionsKilled = participantFrame['jungleMinionsKilled']
						)
					for eventFrame in frame['events']:
						ef = EventByFrame.objects.get_or_create(
							frame = frame_criado,
							eventType = eventFrame['eventType'] if 'eventType' in eventFrame else '',
							towerType = eventFrame['towerType'] if 'towerType' in eventFrame else '',
							teamId = eventFrame['teamId'] if 'teamId' in eventFrame else '',
							ascendedType = eventFrame['ascendedType'] if 'ascendedType' in eventFrame else '',
							killerId = eventFrame['killerId'] if 'killerId' in eventFrame else '',
							levelUpType = eventFrame['levelUpType'] if 'levelUpType' in eventFrame else '',
							pointCaptured = eventFrame['pointCaptured'] if 'pointCaptured' in eventFrame else '',
							assistingParticipantIds = eventFrame['assistingParticipantIds'] if 'assistingParticipantIds' in eventFrame else '',
							wardType = eventFrame['wardType'] if 'wardType' in eventFrame else '',
							monsterType = eventFrame['monsterType'] if 'monsterType' in eventFrame else '',
							eType = eventFrame['type'] if 'type' in eventFrame else '',
							skillSlot = eventFrame['skillSlot'] if 'skillSlot' in eventFrame else '',
							victimId = eventFrame['victimId'] if 'victimId' in eventFrame else '',
							timestamp = eventFrame['timestamp'] if 'timestamp' in eventFrame else '',
							afterId = eventFrame['afterId'] if 'afterId' in eventFrame else '',
							monsterSubType = eventFrame['monsterSubType'] if 'monsterSubType' in eventFrame else '',
							laneType = eventFrame['laneType'] if 'laneType' in eventFrame else '',
							itemId = eventFrame['itemId'] if 'itemId' in eventFrame else '',
							participantId = eventFrame['participantId'] if 'participantId' in eventFrame else '',
							buildingType = eventFrame['buildingType'] if 'buildingType' in eventFrame else '',
							creatorId = eventFrame['creatorId'] if 'creatorId' in eventFrame else '',
							position = eventFrame['position'] if 'position' in eventFrame else '',
							beforeId = eventFrame['beforeId'] if 'beforeId' in eventFrame else '',
						)
				error = False	
			except KeyError:
				print('keyerror')
				error = True

#from django.core import serializers
import json

def stats_by_team(team):
	total_stats = {
		'magicDamageDealtToChampions' : 0,
		'damageDealtToObjectives' : 0,
		'damageDealtToTurrets' : 0,
		'physicalDamageDealtToChampions' : 0,
		'magicDamageDealt' : 0,
		'damageSelfMitigated' : 0,
		'magicalDamageTaken' : 0,
		'trueDamageTaken' : 0,
		'trueDamageDealt' : 0,
		'totalDamageTaken' : 0,
		'physicalDamageDealt' : 0,
		'totalDamageDealtToChampions' : 0,
		'physicalDamageTaken' : 0,
		'totalDamageDealt' : 0,
		'trueDamageDealtToChampions' : 0,
		'totalHeal' : 0,
		'timeCCingOthers' : 0,
		'totalTimeCrowdControlDealt' : 0,
		'longestTimeSpentLiving' : 0
	}
	for player in team['participants']:
		total_stats['magicDamageDealtToChampions'] += player['stats']['magicDamageDealtToChampions']
		total_stats['damageDealtToObjectives'] += player['stats']['damageDealtToObjectives']
		total_stats['damageDealtToTurrets'] += player['stats']['damageDealtToTurrets']
		total_stats['physicalDamageDealtToChampions'] += player['stats']['physicalDamageDealtToChampions']
		total_stats['magicDamageDealt'] += player['stats']['magicDamageDealt']
		total_stats['damageSelfMitigated'] += player['stats']['damageSelfMitigated']
		total_stats['magicalDamageTaken'] += player['stats']['magicalDamageTaken']
		total_stats['trueDamageTaken'] += player['stats']['trueDamageTaken']
		total_stats['trueDamageDealt'] += player['stats']['trueDamageDealt']
		total_stats['totalDamageTaken'] += player['stats']['totalDamageTaken']
		total_stats['physicalDamageDealt'] += player['stats']['physicalDamageDealt']
		total_stats['totalDamageDealtToChampions'] += player['stats']['totalDamageDealtToChampions']
		total_stats['physicalDamageTaken'] += player['stats']['physicalDamageTaken']
		total_stats['totalDamageDealt'] += player['stats']['totalDamageDealt']
		total_stats['trueDamageDealtToChampions'] += player['stats']['trueDamageDealtToChampions']
		total_stats['totalHeal'] += player['stats']['totalHeal']
		total_stats['timeCCingOthers'] += player['stats']['timeCCingOthers']
		total_stats['totalTimeCrowdControlDealt'] += player['stats']['totalTimeCrowdControlDealt']
		total_stats['longestTimeSpentLiving'] += player['stats']['longestTimeSpentLiving']
	return total_stats

def create_team_stats_in_match(match):
	both_team_stats = TeamStatsByMatch.objects.filter(match=match)
	participants_each_team = ParticipantStatsByMatch.objects.filter(match=match)
	if both_team_stats.count()!=2 or participants_each_team.count()!=10:
		return None
	blueTeam = {}
	redTeam = {}
	summoners = match.participantIdentities.split(';')
	for team_stats in both_team_stats:
		t_stat = {
			'firstDragon' : team_stats.firstDragon,
			'firstInhibitor' : team_stats.firstInhibitor,
			'bans' : team_stats.bans,
			'baronKills' : team_stats.baronKills,
			'firstRiftHerald' : team_stats.firstRiftHerald,
			'firstBaron' : team_stats.firstBaron,
			'riftHeraldKills' : team_stats.riftHeraldKills,
			'firstBlood' : team_stats.firstBlood,
			'teamIsBlue' : team_stats.teamIsBlue,
			'firstTower' : team_stats.firstTower,
			'inhibitorKills' : team_stats.inhibitorKills,
			'towerKills' : team_stats.towerKills,
			'win' : team_stats.win,
			'dragonKills' : team_stats.dragonKills
		}
		if team_stats.teamIsBlue:
			blueTeam['teamStats'] = t_stat
		else:
			redTeam['teamStats'] = t_stat
	blueTeam['participants'] = list()
	redTeam['participants'] = list()
	for participant_team in participants_each_team:
		name = ''
		for summoner in summoners:
			s = summoner.split(':')
			if int(s[1])==participant_team.participantId:
				name = s[0]
		p_team = {
			'summonerName' : name,
			'participantId' : participant_team.participantId,
			'teamIsBlue' : participant_team.teamIsBlue,
			'spell1Id' : participant_team.spell1Id,
			'spell2Id' : participant_team.spell2Id,
			'highestAchievedSeasonTier' : participant_team.highestAchievedSeasonTier,
			'championId' : participant_team.championId
		}		
		statInMatch = StatsByParticipant.objects.filter(participant=participant_team).first()
		s_part = {
			'magicDamageDealtToChampions' : statInMatch.magicDamageDealtToChampions,
			'damageDealtToObjectives' : statInMatch.damageDealtToObjectives,
			'damageDealtToTurrets' : statInMatch.damageDealtToTurrets,
			'physicalDamageDealtToChampions' : statInMatch.physicalDamageDealtToChampions,
			'magicDamageDealt' : statInMatch.magicDamageDealt,
			'damageSelfMitigated' : statInMatch.damageSelfMitigated,
			'magicalDamageTaken' : statInMatch.magicalDamageTaken,
			'trueDamageTaken' : statInMatch.trueDamageTaken,
			'trueDamageDealt' : statInMatch.trueDamageDealt,
			'totalDamageTaken' : statInMatch.totalDamageTaken,
			'physicalDamageDealt' : statInMatch.physicalDamageDealt,
			'totalDamageDealtToChampions' : statInMatch.totalDamageDealtToChampions,
			'physicalDamageTaken' : statInMatch.physicalDamageTaken,
			'totalDamageDealt' : statInMatch.totalDamageDealt,
			'trueDamageDealtToChampions' : statInMatch.trueDamageDealtToChampions,
			'totalHeal' : statInMatch.totalHeal,
			'timeCCingOthers' : statInMatch.timeCCingOthers,
			'totalTimeCrowdControlDealt' : statInMatch.totalTimeCrowdControlDealt,
			'longestTimeSpentLiving' : statInMatch.longestTimeSpentLiving,
			'perk0Var1' : statInMatch.perk0Var1,
			'perk0Var2' : statInMatch.perk0Var2,
			'perk0Var3' : statInMatch.perk0Var3,
			'perk1Var1' : statInMatch.perk1Var1,
			'perk1Var2' : statInMatch.perk1Var2,
			'perk1Var3' : statInMatch.perk1Var3,
			'perk2Var1' : statInMatch.perk2Var1,
			'perk2Var2' : statInMatch.perk2Var2,
			'perk2Var3' : statInMatch.perk2Var3,
			'perk3Var1' : statInMatch.perk3Var1,
			'perk3Var2' : statInMatch.perk3Var2,
			'perk3Var3' : statInMatch.perk3Var3,
			'perk4Var1' : statInMatch.perk4Var1,
			'perk4Var2' : statInMatch.perk4Var2,
			'perk4Var3' : statInMatch.perk4Var3,
			'perk5Var1' : statInMatch.perk5Var1,
			'perk5Var2' : statInMatch.perk5Var2,
			'perk5Var3' : statInMatch.perk5Var3,
			'perk0' : statInMatch.perk0,
			'perk2' : statInMatch.perk2,
			'perk1' : statInMatch.perk1,
			'perk3' : statInMatch.perk3,
			'perk4' : statInMatch.perk4,
			'perk5' : statInMatch.perk5,
			'perkPrimaryStyle' : statInMatch.perkPrimaryStyle,
			'perkSubStyle' : statInMatch.perkSubStyle,
			'firstBloodKill' : statInMatch.firstBloodKill,
			'kills' : statInMatch.kills,
			'doubleKills' : statInMatch.doubleKills,
			'tripleKills' : statInMatch.tripleKills,
			'quadraKills' : statInMatch.quadraKills,
			'pentaKills' : statInMatch.pentaKills,
			'unrealKills' : statInMatch.unrealKills,
			'killingSprees' : statInMatch.killingSprees,
			'largestMultiKill' : statInMatch.largestMultiKill,
			'largestKillingSpree' : statInMatch.largestKillingSpree,
			'assists' : statInMatch.assists,
			'firstBloodAssist' : statInMatch.firstBloodAssist,
			'deaths' : statInMatch.deaths,
			'playerScore0' : statInMatch.playerScore0,
			'playerScore1' : statInMatch.playerScore1,
			'playerScore2' : statInMatch.playerScore2,
			'playerScore3' : statInMatch.playerScore3,
			'playerScore4' : statInMatch.playerScore4,
			'playerScore5' : statInMatch.playerScore5,
			'playerScore6' : statInMatch.playerScore6,
			'playerScore7' : statInMatch.playerScore7,
			'playerScore8' : statInMatch.playerScore8,
			'playerScore9' : statInMatch.playerScore9,
			'totalScoreRank' : statInMatch.totalScoreRank,
			'neutralMinionsKilled' : statInMatch.neutralMinionsKilled,
			'neutralMinionsKilledTeamJungle' : statInMatch.neutralMinionsKilledTeamJungle,
			'neutralMinionsKilledEnemyJungle' : statInMatch.neutralMinionsKilledEnemyJungle,
			'totalMinionsKilled' : statInMatch.totalMinionsKilled,
			'totalUnitsHealed' : statInMatch.totalUnitsHealed,
			'largestCriticalStrike' : statInMatch.largestCriticalStrike,
			'item0' : statInMatch.item0,
			'item1' : statInMatch.item1,
			'item2' : statInMatch.item2,
			'item3' : statInMatch.item3,
			'item4' : statInMatch.item4,
			'item5' : statInMatch.item5,
			'item6' : statInMatch.item6,
			'goldSpent' : statInMatch.goldSpent,
			'goldEarned' : statInMatch.goldEarned,
			'champLevel' : statInMatch.champLevel,
			'firstInhibitorKill' : statInMatch.firstInhibitorKill,
			'inhibitorKills' : statInMatch.inhibitorKills,
			'firstInhibitorAssist' : statInMatch.firstInhibitorAssist,
			'firstTowerAssist' : statInMatch.firstTowerAssist,
			'firstTowerKill' : statInMatch.firstTowerKill,
			'turretKills' : statInMatch.turretKills,
			'combatPlayerScore' : statInMatch.combatPlayerScore,
			'participantId' : statInMatch.participantId,
			'sightWardsBoughtInGame' : statInMatch.sightWardsBoughtInGame,
			'visionWardsBoughtInGame' : statInMatch.visionWardsBoughtInGame,
			'wardsPlaced' : statInMatch.wardsPlaced,
			'wardsKilled' : statInMatch.wardsKilled,
			'totalPlayerScore' : statInMatch.totalPlayerScore,
			'visionScore' : statInMatch.visionScore,
			'objectivePlayerScore' : statInMatch.objectivePlayerScore,
			'win' : statInMatch.win
		}
		p_team['stats'] = s_part
		if participant_team.teamIsBlue:
			blueTeam['participants'].append(p_team)
		else:
			redTeam['participants'].append(p_team)
	blueTeam['totalStats'] = stats_by_team(blueTeam)
	redTeam['totalStats'] = stats_by_team(redTeam)

	match_complete_info = {
		'gameId' : match.gameId,
		'gameDuration' : match.gameDuration,
		'gameCreation' : match.gameCreation,
		'blueTeam':blueTeam,
		'redTeam':redTeam
	}
	return match_complete_info

def create_resumed_stats_in_match(match):
	both_team_stats = TeamStatsByMatch.objects.filter(match=match)
	participants_each_team = ParticipantStatsByMatch.objects.filter(match=match)
	if both_team_stats.count()!=2 or participants_each_team.count()!=10:
		return None
	blueTeam = {}
	redTeam = {}
	summoners = match.participantIdentities.split(';')
	for team_stats in both_team_stats:
		t_stat = {
			'firstDragon' : team_stats.firstDragon,
			'firstInhibitor' : team_stats.firstInhibitor,
			'bans' : team_stats.bans,
			'baronKills' : team_stats.baronKills,
			'firstRiftHerald' : team_stats.firstRiftHerald,
			'firstBaron' : team_stats.firstBaron,
			'riftHeraldKills' : team_stats.riftHeraldKills,
			'firstBlood' : team_stats.firstBlood,
			'teamIsBlue' : team_stats.teamIsBlue,
			'firstTower' : team_stats.firstTower,
			'inhibitorKills' : team_stats.inhibitorKills,
			'towerKills' : team_stats.towerKills,
			'win' : team_stats.win,
			'dragonKills' : team_stats.dragonKills
		}
		if team_stats.teamIsBlue:
			blueTeam['teamStats'] = t_stat
		else:
			redTeam['teamStats'] = t_stat
	blueTeam['participants'] = list()
	redTeam['participants'] = list()
	for participant_team in participants_each_team:
		name = ''
		for summoner in summoners:
			s = summoner.split(':')
			if int(s[1])==participant_team.participantId:
				name = s[0]
		p_team = {
			'summonerName' : name,
			'participantId' : participant_team.participantId,
			'teamIsBlue' : participant_team.teamIsBlue,
			'spell1Id' : participant_team.spell1Id,
			'spell2Id' : participant_team.spell2Id,
			'highestAchievedSeasonTier' : participant_team.highestAchievedSeasonTier,
			'championId' : participant_team.championId
		}		
		statInMatch = StatsByParticipant.objects.filter(participant=participant_team).first()
		s_part = {
			'magicDamageDealtToChampions' : statInMatch.magicDamageDealtToChampions,
			'damageDealtToObjectives' : statInMatch.damageDealtToObjectives,
			'damageDealtToTurrets' : statInMatch.damageDealtToTurrets,
			'physicalDamageDealtToChampions' : statInMatch.physicalDamageDealtToChampions,
			'magicDamageDealt' : statInMatch.magicDamageDealt,
			'damageSelfMitigated' : statInMatch.damageSelfMitigated,
			'magicalDamageTaken' : statInMatch.magicalDamageTaken,
			'trueDamageTaken' : statInMatch.trueDamageTaken,
			'trueDamageDealt' : statInMatch.trueDamageDealt,
			'totalDamageTaken' : statInMatch.totalDamageTaken,
			'physicalDamageDealt' : statInMatch.physicalDamageDealt,
			'totalDamageDealtToChampions' : statInMatch.totalDamageDealtToChampions,
			'physicalDamageTaken' : statInMatch.physicalDamageTaken,
			'totalDamageDealt' : statInMatch.totalDamageDealt,
			'trueDamageDealtToChampions' : statInMatch.trueDamageDealtToChampions,
			'totalHeal' : statInMatch.totalHeal,
			'timeCCingOthers' : statInMatch.timeCCingOthers,
			'totalTimeCrowdControlDealt' : statInMatch.totalTimeCrowdControlDealt,
			'longestTimeSpentLiving' : statInMatch.longestTimeSpentLiving,
			'champLevel' : statInMatch.champLevel,
			'kills' : statInMatch.kills,
			'assists' : statInMatch.assists,
			'deaths' : statInMatch.deaths,
			'goldEarned' : statInMatch.goldEarned
		}
		p_team['stats'] = s_part
		if participant_team.teamIsBlue:
			blueTeam['participants'].append(p_team)
		else:
			redTeam['participants'].append(p_team)
	blueTeam['totalStats'] = stats_by_team(blueTeam)
	redTeam['totalStats'] = stats_by_team(redTeam)

	match_complete_info = {
		'gameId' : match.gameId,
		'gameDuration' : match.gameDuration,
		'gameCreation' : match.gameCreation,
		'blueTeam':blueTeam,
		'redTeam':redTeam
	}
	return match_complete_info

def create_stats():
	matches = Match.objects.all()
	for match in matches:
		match_complete_info = create_team_stats_in_match(match)
		if match_complete_info != None:
			with open('games_json/game%s.json'%match.gameId, 'w') as outfile:  
				json.dump(match_complete_info, outfile)
	#print(blueTeam)
	#print(redTeam)

def create_player_stats():
	summoner = Summoner.objects.filter(summonerName="Little Wos").first()
	matches_bs = MatchBySummoner.objects.filter(summoner=summoner)
	matches = Match.objects.filter(gameId__in=matches_bs.values_list('gameId'))
	player_matches = []
	for match in matches:
		match_complete_info = create_team_stats_in_match(match)
		if match_complete_info == None:
			continue
		m_info = {}
		m_info['gameCreation'] = match.gameCreation
		m_info['playerStats'] = {}
		m_info['teamIsBlue'] = False
		for participant in match_complete_info['blueTeam']['participants']:
			if participant['summonerName']==summoner.summonerName:
				m_info['playerStats']=participant
				m_info['teamIsBlue'] = True
		for participant in match_complete_info['redTeam']['participants']:
			if participant['summonerName']==summoner.summonerName:
				m_info['playerStats']=participant

		if m_info['teamIsBlue']:
			m_info['alliedStats'] = match_complete_info['blueTeam']['totalStats']
			m_info['oponentStats'] = match_complete_info['redTeam']['totalStats']
		else:
			m_info['alliedStats'] = match_complete_info['redTeam']['totalStats']
			m_info['oponentStats'] = match_complete_info['blueTeam']['totalStats']
		player_matches.append(m_info)

	player_complete_info = {
		'summonerName':summoner.summonerName,
		'matches':player_matches
	}
	with open('games_json_player/player%s.json'%summoner.summonerName, 'w') as outfile:  
		json.dump(player_complete_info, outfile)