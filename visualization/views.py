from django.shortcuts import render, redirect
from django.http import JsonResponse
from matches.models import Match
from summoner.models import Summoner
from matches.utils import create_resumed_stats_in_match, create_resumed_player_stats, generate_data
from django.conf import settings

# Create your views here.
def index(request):
	return render(request, 'home.html', locals())

def match(request):
	return render(request, 'match.html', locals())

def player(request):
	st_url = settings.STATIC_URL
	players = Summoner.objects.all().order_by('-leaguePoints')
	return render(request, 'player.html', locals())

def get_match(request):
	if request.method == 'GET':
		try:
			match = Match.objects.get(gameId=request.GET['id'])
			data = create_resumed_stats_in_match(match)
			return JsonResponse({'data':data})
		except Exception as e:
			print(e)
	return JsonResponse({'data':None})

def get_player(request):
	if request.method == 'GET':
		try:
			data = create_resumed_player_stats(request.GET['id'])
			return JsonResponse({'data':data})
		except Exception as e:
			print(e)
	return JsonResponse({'data':None})

def champions_network(request):
	st_url = settings.STATIC_URL
	dados = generate_data(False)
	return render(request, 'network-champions.html', locals())