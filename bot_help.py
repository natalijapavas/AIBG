#!/usr/bin/env python3

import requests
import json
import random

URL = 'http://127.0.0.1:9080'
GAME_ID = 125
POSX = 0
POSY = 0
PLAYER_ID=2
OBS_MAP = list()

MOVE = [ 'w', 's', 'a', 'd']
TAKE_RESOURCES = ['trw', 'tws', 'twa', 'twd']
TAKE_WEAPONS = ['tww', 'tws', 'twa', 'twd']
LEAVE = ['lw', 'ls', 'lm']
BUILD = ['bhw', 'bhs', 'bha', 'bhd',
         'bfw', 'bfs', 'bfa', 'bfd',
         'bshfw', 'bshfs', 'bshfa', 'bshfd',
         'bsfw', 'bsfs', 'bsfa', 'bsfd',
         'bafw', 'bafs', 'bafa', 'bafd']
ATTACK = ['saw', 'sas', 'saa', 'sad',
         'aaw', 'aas', 'aaa', 'aad', 'aawa', 'aawd', 'aasa', 'aasd']
DROP = ['dsh']

def start_game(playerId = PLAYER_ID):
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

def get_player_info(game_data):
    global PLAYER_INDEX 
    PLAYER_INDEX = game_data['playerIndex'] 
    player_data  = game_data['result']['player'+str(PLAYER_INDEX)]
    return player_data

def get_coords(player_data):
    posx = player_data['x']
    posy = player_data['y']
    return posx, posy


def move(x,y):
    global POSX
    global POSY
    global OBS_MAP

    if POSX is x and POSY is y:
        return 0

    if abs(POSX - x) >= abs(POSY - y):
        if POSX - x > 0:
            if OBS_MAP[POSX-1][POSY] is 1:
                if POSY is y:
                    if POSX - x is 1:
                        return 1
                    if y is 0:
                        return move(POSX,POSY+1)
                    else:
                        return move(POSX,POSY-1)
                else:
                    return move(POSX,y)
            return 'a'
        else:
            if OBS_MAP[POSX+1][POSY] is 1:
                if POSY is y:
                    if POSX + x is 1:
                        return 1
                    if y is 0:
                        return move(POSX,POSY+1)
                    else:
                        return move(POSX,POSY-1)
                else:
                    return move(POSX,y)
            return 'd'
    else:
        if POSY - y > 0:
            if OBS_MAP[POSX][POSY-1] is 1:
                if POSX is x:
                    if POSY - y is 1:
                        return 1
                    if x is 0:
                        return move(POSX+1,POSY)
                    else:
                        return move(POSX-1,POSY)
                else:
                    return move(x,POSY)
            return 'w'
        else:
            if OBS_MAP[POSX][POSY+1] is 1:
                if POSX is x:
                    if POSY + y is 1:
                        return 1
                    if x is 0:
                        return move(POSX+1,POSY)
                    else:
                        return move(POSX-1,POSY)
                else:
                    return move(x,POSY)
            return 's'

def obs_map(json_res):
    print(json_res.keys())
    tiles = json_res['result']['map']['tiles']
    map = list()
    for i in range(25):
        row = list()
        for j in range(20):
            if tiles[i][j]['item'] is 'null':
                row[j] = 0
            else:
                row[j] = 1
        map.append(row)
    return map

def calc_next_action(game_state):
    return random.choice(MOVE)

def get_tile_info(x,y, game_state):
    tiles = game_state['result']['map']['tiles']
    width = int(game_state['result']['map']['width'])
    height = int(game_state['result']['map']['height'])
    tile = tiles[y][x]
    tile_item = tile['item']
    if tile['item'] == None:
        return True 
    else:
        return False

def isValidMove(gameState, action):
    p_data = get_player_info(gameState)
    width = int(gameState['result']['map']['width'])
    height = int(gameState['result']['map']['height'])
    px, py = get_coords(p_data)
    
    if action == 'd':
        return False if px + 1 > width else True
    if action == 'a':
        return False if px - 1 < 0 else True
    if action == 'w':
        return False if py + 1 > height else True
    if action == 's':
        return False if py - 1 < 0 else True


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
    # Izmeni da vracas stringove umesto da zoves do_action
    # Nemoj da zoves do_action iz pod funkcija odatle!!1111!! x
    # Prebaci ovu funkciju u bot.py
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

if __name__ == '__main__':
    print('testing')
    gid = 1
    connResp = create_game(gid, 1,2,'mapConfig')
    while connResp['success'] == False:
        print(connResp['success'])
        gid += 1
        connResp = create_game(gid, 1, 2, 'mapConfig')
    print('[+] game created')
    # testing stuff
    OBS_MAP = obs_map(connResp)
    while move(5,5) is not 1 or move(5,5) is not 0:
        obs_map(do_action(gid,PLAYER_ID,move(5,5)))
    # free zone
    tmp = join_game(60, 2)
    p_data = get_player_info(tmp)
    x, y= get_coords(p_data)
    print(get_tile_info( x, y, tmp))
