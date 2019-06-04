import requests
import json
from operator import itemgetter
import time

#initial_time = time.time()

NUMERO_JOGADORES = 30
NUMERO_PARTIDAS = 20

INITIAL_URL = 'https://'
SERVER = 'br1'
URL = '.api.riotgames.com/lol/'

API_KEY = "RGAPI-8c078f07-6472-4279-bf9a-0d42a7441be5"

def make_request(search_type, query_paramethers):
    q = ''
    if query_paramethers:
        for key, value in query_paramethers.items():
            q += '&%s=%s' %(key,value)
    r = requests.get(INITIAL_URL + SERVER + URL + search_type  + '?api_key=' +API_KEY + q)
    if r.status_code >= 400:
        print(r.text)
        while r.status_code == 429:#Codigo para limite da API excedido
            print('Esperando: %ss'%r.headers['Retry-After'])
            t = time.time()
            time.sleep(int(r.headers['Retry-After'])+1)
            print('esperou ', time.time()-t, 'segundos...')
            r = requests.get(INITIAL_URL + SERVER + URL + search_type  + '?api_key=' +API_KEY + q)
            if r.status_code >= 400:
                print(r.text)
    return r.json()

