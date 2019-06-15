import requests
import json
from operator import itemgetter
import time

#initial_time = time.time()

INITIAL_URL = 'https://'
SERVER = 'br1'
URL = '.api.riotgames.com/lol/'

API_KEY = "RGAPI-9c79873a-cfdb-4058-ab37-701726c263cb"

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

def make_request_endpoint(endpoint, query_paramethers):
    q = ''
    if query_paramethers:
        for key, value in query_paramethers.items():
            q += '&%s=%s' %(key,value)
    r = requests.get(endpoint  + '?api_key=' +API_KEY + q)
    if r.status_code >= 400:
        while r.status_code == 429:#Codigo para limite da API excedido
            print('Esperando: %ss'%r.headers['Retry-After'])
            t = time.time()
            time.sleep(int(r.headers['Retry-After'])+1)
            print('esperou ', time.time()-t, 'segundos...')
            r = requests.get(INITIAL_URL + SERVER + URL + search_type  + '?api_key=' +API_KEY + q)
            if r.status_code >= 400:
                print(r.text)
    return r.json()