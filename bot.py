#!/usr/bin/env python3
import bot_help as bh
import random

GAME_ID = bh.GAME_ID
PLAYER_ID = 1
print('[+] bot is spawned')
last_game_state = bh.join_game(GAME_ID, PLAYER_ID)
print('[+] bot joined game {}'.format(GAME_ID))

for i in range(10):
    action = bh.calc_next_action(last_game_state)
    while not bh.isValidMove(last_game_state, action):
        action = bh.calc_next_action(last_game_state)
    print("[+] bot is doing {}".format(action))
    last_game_state = bh.do_action(PLAYER_ID, GAME_ID, action)

# building a house


GAME_ID = 10
PLAYER_ID = 2


