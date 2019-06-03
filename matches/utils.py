from summoner.models import Summoner
from .models import MatchBySummoner, Match
from request_maker.utils import make_request
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


NUMERO_PARTIDAS = 20

def get_matches_by_summoner():
	summoners = Summoner.objects.all()
	for player in summoners:
		matchList = make_request('match/v4/matchlists/by-account/%s' % player.accountId, {'endIndex':NUMERO_PARTIDAS})
		for match in matchList['matches']:
			#matchInfo = make_request('match/v4/matches/%s' % match['gameId'], None)
			print(match)
			MatchBySummoner.objects.create(
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
def get_matches():
	matches = MatchBySummoner.objects.all()
	for match in matches:
		try:
			Match.objects.get(gameId=match.gameId)

		except ObjectDoesNotExist as e:
			matchInfo = make_request('match/v4/matches/%s' % match.gameId, None)
			#for matchInfo in matchInfos:
			text = ''
			for p in matchInfo['participantIdentities']:
				print(p)
				text+=p['player']['summonerName']+'-'+str(p['participantId'])+(';' if p!=matchInfo['participantIdentities'][-1] else '')
			print(text)
			Match.objects.create(
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
			print(e)
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
