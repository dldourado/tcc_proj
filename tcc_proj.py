import requests

FINAL_URL = 'https://'

URL = '.api.riotgames.com/lol/'
SERVER = 'br1'

SEARCH_TYPE = 'league/v4/challengerleagues/by-queue/'
CHALLENGER_QUEUE = 'RANKED_SOLO_5x5'

FINAL_URL += SERVER + URL + SEARCH_TYPE + CHALLENGER_QUEUE
print(FINAL_URL)

API_KEY = input("API KEY:")
FINAL_URL += '?api_key=%s' % API_KEY
print(FINAL_URL)

#requests
r = requests.get(FINAL_URL)
print(r.status_code)
print(r.json())