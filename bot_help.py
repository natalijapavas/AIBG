#!/usr/bin/env python3

import requests

URL = 'http://127.0.0.1:9080'
GAME_ID = 1
POSX = 0
POSY = 0
PLAYER_ID=2
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
            return 'a'
        else:
            return 'd'
    else:
        if POSY - y > 0:
            return 'w'
        else:
            return 's'

 

def obs_map(json_res):
    tiles = json_res['result']['map']['tiles']
    map = list()

    for i in range(json_res['result']['map']['height']):
        row = list()
        for j in range(json_res['result']['map']['width']):
            if tiles[i][j]['item'] is 'null':
                row[j] = 0
            else:
                row[j] = 1
        map.append(row)

    return map



def isValidMove(gameState, action):
    map=obs_map(gameState)

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
    return x, y

def build(json_res):
    wx,wy=find(json_res,'w')
    dist=move(wx,wy)
    while dist is not 1:
        dist = move(wx,wy)

    w=0
    while w is not 4:
        if wx - POSX > 0:
            res=do_action(2,10,'trd')
        if wx - POSX < 0:
            res=do_action(2,10,'tra')
        if wy - POSY > 0:
            res=do_action(2,10,'trs')
        if wy - POSY < 0:
            res=do_action(2,10,'trw')
        w=w+1

    sx,sy=find(res,'s')
    dist2=move(sx,sy)

    while dist2 is not 1:
          dist2 = move(sx,sy)

    if sx - POSX > 0:
        do_action(2,10,'trd')
    if sx - POSX < 0:
        do_action(2,10,'tra')
    if sy - POSY > 0:
        do_action(2,10,'trs')
    if sy - POSY < 0:
        do_action(2,10,'trw')

    do_action(2,10,'bha')

    s=0
    while s is not 3:
        if sx - POSX > 0:
            do_action(2,10,'trd')
            s=s+1
        if sx - POSX < 0:
            do_action(2,10,'tra')
            s=s+1
        if sy - POSY > 0:
            do_action(2,10,'trs')
            s=s+1
        if sy - POSY < 0:
            do_action(2,10,'trw')
            s=s+1

    return do_action(2,10,'bfa')

