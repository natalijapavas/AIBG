#!/usr/bin/env python3

import requests

URL = 'http://127.0.0.1:9080'
GAME_ID = 1
POSX = 0
POSY = 0

def start_game(playerId = PLAYERID):
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

def move(x,y):
    global POSX
    global POSY

    if POSX is x and POSY is y:
        return 0

    if abs(POSX - x) >= abs(POSY - y):
        if POSX - x > 0:
            do_action(2,10,'a')
        else:
            do_action(2,10,'d')
    else:
        if POSY - y > 0:
            do_action(2,10,'w')
        else:
            do_action(2,10,'s')

    return abs(POSX - x) + abs(POSY - y)

def obs_map(json_res):
    tiles = json_res['result']['map']['tiles']
    map = list()

    for i in range(json_res['result']['map']['height']):
        row = list()
        for j in range(json_res['result']['map']['width']):
            if tiles[i][j]['item'] is 'null':
                row[j] = 0
            else
                row[j] = 1
        map.append(row)

    return map

