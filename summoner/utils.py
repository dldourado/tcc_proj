from .models import Summoner
from request_maker.utils import make_request

def get_challengers():
	challenger_data = make_request('league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5', None)
	for player in challenger_data['entries']:
		try:
			summoner = Summoner.objects.get(summonerName=player['summonerName'])
		except:
			player['accountInformation'] = make_request('summoner/v4/summoners/by-name/%s' % player['summonerName'], None)
			Summoner.objects.create(
				summonerName = player['summonerName'],
				accountId = player['accountInformation']['accountId']
			)
