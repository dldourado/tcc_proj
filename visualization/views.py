from django.shortcuts import render
from django.http import JsonResponse
from matches.models import Match
from matches.utils import create_resumed_stats_in_match

# Create your views here.
def index(request):
	return render(request, 'index.html', locals())

def get_match(request):
	if request.method == 'GET':
		try:
			match = Match.objects.get(gameId=request.GET['id'])
			data = create_resumed_stats_in_match(match)
			return JsonResponse({'data':data})
		except Exception as e:
			print(e)
	return JsonResponse({'data':None})