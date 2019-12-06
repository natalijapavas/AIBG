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
    data = {'playerId': playerId,
            'gameId': gameId}
    r = requests.get(URL+path, params=data)
    return r.json()

def do_action(playerId, gameId, action):
    path = '/doAction'
    data = {'gameId':gameId,
            'playerId':playerId,
            'action': action}
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


res = start_game('13')
create_game(10,1,2,'mapConfig')
input('game started, press any key...')

player1 = join_game(10, 1)
input('1 joined')
player2 = join_game(10, 2)
input('2 joined')
do_action(1, 10, 's')
input('action 1')
do_action(2, 10, 'w')
input('action 2')