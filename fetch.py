# -*- coding: utf-8 -*-
"""
Created on Thu May 23 19:15:22 2019

@author: Tim
"""

import pysmash
import pickle

smash = pysmash.SmashGG()
crawlTourns = [
        ('evo-2018', 'super-smash-bros-for-wii-u'),
        ('smash-n-splash-4', 'smash4-singles'),
        ('king', 'ultimate-singles'),
        ('pound-2019', 'ultimate-singles'),
        ('frostbite-2019', 'super-smash-bros-ultimate-singles'),
        ('genesis-6', 'smash-for-switch-singles'),
        ('don-t-park-on-the-grass-2018-1', 'smash-ultimate-singles'),
        ('get-on-my-level-2019-canadian-fighting-game-championships', 'smash-bros-ultimate')
        ]

def crawlTags( tournaments, saving ):
    tags = []
    for tourney in crawlTourns:
        players = smash.tournament_show_players( tourney[0], tourney[1] )
        tags.extend( [x['tag'] for x in players] )
    
    if saving:
        with open('tags', 'wb') as fp:
            pickle.dump(tags, fp)
    else:
        return tags

#crawlTags( crawlTourns, True )
