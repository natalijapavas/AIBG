#!/usr/bin/env python3
import requests
import json

URL = 'http://127.0.0.1:9080'
GAME_ID = 1

def start_game(playerId):
    path = '/train/random'
    data = {'playerId': playerId}
    print(URL + path)
    r = requests.get(URL+path, params=data)
    return r.json()

def join_game(gameId, playerId):
    path = '/game/play'
    data = {'playerId', playerId,
            'gameId', gameId}
    r = requests.get(URL+path, params=data)
    return r.json()

res = start_game('13')
