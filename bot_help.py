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

def find(json_res, item):
    if item is 'w' or item is 'wood':
          item = 'WOOD'

    if item is 's' or item is 'stone':
          item = 'STONE'

    if item is 'm' or item is 'metal':
          item = 'METAL'

    tiles = json_res['result']['map']['tiles']
    x = 1000
    y = 1000

    for i in range(json_res['result']['map']['height']):
        for j in range(json_res['result']['map']['width']):
            if tiles[i][j]['item']['itemType'] is item+'_SHOP':
                if abs(POSX-x)+abs(POSY-y) > abs(POSX-i)+abs(POSY-j):
                    x=i
                    y=j

   return x,y

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
