#!/usr/bin/env python3
import bot_help as bh
import random
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
GAME_ID = bh.GAME_ID
PLAYER_ID = 1
print('[+] bot is spawned')
last_game_state = bh.join_game(GAME_ID, PLAYER_ID)
print('[+] bot joined game {}'.format(GAME_ID))

for i in range(10):
    action = calc_next_action(last_game_state)
    if isValid(last_game_state, action):
        last_game_state = bh.do_action(PLAYER_ID, GAME_ID, action)
    print("[+] bot is doing {}".format(action))
    last_game_state = bh.do_action(PLAYER_ID, GAME_ID, action)

# building a house


GAME_ID = 10
PLAYER_ID = 2


