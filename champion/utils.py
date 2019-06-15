from .models import Champion
from request_maker.utils import make_request_endpoint
import requests
import shutil
import re
def get_champions():
	champion_list = make_request_endpoint('http://ddragon.leagueoflegends.com/cdn/9.3.1/data/en_US/champion.json', None)
	for champion in champion_list['data']:
		value = champion_list['data'][champion]
		try:
			champion = Champion.objects.get(championId=value['key'])
		except:
			Champion.objects.create(
				name = value['name'],
				nameId = value['id'],
				championId = value['key']
			)

def get_champions_icons():
	champions = Champion.objects.all()
	for champion in champions:
		r = requests.get('http://raw.communitydragon.org/latest/game/assets/characters/%s/hud/'%champion.nameId.lower(), stream=True)
		if r.status_code == 200:
			name = re.findall('title=".*square.*.png"',r.text)[0].split('"')[1]
			r = requests.get('http://raw.communitydragon.org/latest/game/assets/characters/%s/hud/%s'%(champion.nameId.lower(),name), stream=True)
			if r.status_code == 200:
			    with open('champion/static/champion/%s.png'%champion.championId, 'wb') as f:
			        r.raw.decode_content = True
			        shutil.copyfileobj(r.raw, f)

			
		else:
			print(champion.championId, '-', champion.name)