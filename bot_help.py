#!/usr/bin/env python3

import requests


URL = 'http://127.0.0.1:9080'
GAME_ID = 40
def start_game(playerId):
    path = '/train/random'
    data = {'playerId': playerId}
    print(URL + path)
    r = requests.get(URL+path, params=data)
    return r.json()

def join_game(gameId, playerId):
    path = '/game/play'
    data = {'playerId' : playerId,
            'gameId' : gameId}
    r = requests.get(URL+path, params=data)
    return r.json()

def do_action(playerId, gameId, action):
    path = '/doAction'
    data = {'gameId' :gameId,
            'playerId' :playerId,
            'action' : action}
    r = requests.get(URL+path, params=data)
    return r.json()

def create_game(gameId,playerOne,playerTwo,mapConFig):
    path = '/admin/createGame'
    data = {'gameId': gameId,
            'playerOne': playerOne,
            'playerTwo': playerTwo,
            'map_name' : mapConFig}
    r = requests.get(URL+path, params=data)
    return r.json()