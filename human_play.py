#!/usr/bin/env python3
import bot_help as bh

bh.join_game(bh.GAME_ID, 2)
print('[+] human has joined the match')

for i in range(10):
    action = input('make your move')
    bh.do_action(2, bh.GAME_ID, action)