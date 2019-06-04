from summoner.models import Summoner
from .models import MatchBySummoner, Match, TeamStatsByMatch, ParticipantStatsByMatch, StatsByParticipant
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
					print(match)
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
	for match in matches:
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
						text+=p['player']['summonerName']+'-'+str(p['participantId'])+(';' if p!=matchInfo['participantIdentities'][-1] else '')
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
								bans += str(ban['pickTurn'])+'-'+str(ban['championId'])+(';' if ban!=team['bans'][-1] else '')
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
									teamIsBlue =  True if team['teamId']==100 else False,
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
	"""challenger_data = make_request('league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5', None)
	for player in challenger_data['entries']:
		try:
			summoner = Summoner.objects.get(summonerName=player['summonerName'])
		except:
			player['accountInformation'] = make_request('summoner/v4/summoners/by-name/%s' % player['summonerName'], None)
			Summoner.objects.create(
				summonerName = player['summonerName'],
				accountId = player['accountInformation']['accountId']
			)"""

def get_test_obj():
	match_criada = Match.objects.all().first()
	matchInfo = make_request('match/v4/matches/%s' % match_criada.gameId, None)
	for team in matchInfo['teams']:
		bans = ''
		for ban in team['bans']:
			bans += str(ban['pickTurn'])+'-'+str(ban['championId'])+(';' if ban!=team['bans'][-1] else '')
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
				teamIsBlue =  True if team['teamId']==100 else False,
				spell1Id = participant['spell1Id'],
				spell2Id = participant['spell2Id'],
				highestAchievedSeasonTier = participant['highestAchievedSeasonTier'] if 'highestAchievedSeasonTier' in participant else '',
				championId = participant['championId'],
			)
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
			firstInhibitorKill = participant['stats']['firstInhibitorKill'],
			inhibitorKills = participant['stats']['inhibitorKills'],
			firstInhibitorAssist = participant['stats']['firstInhibitorAssist'],
			firstTowerAssist = participant['stats']['firstTowerAssist'],
			firstTowerKill = participant['stats']['firstTowerKill'],
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