import pygame
from os.path import join

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720 

SIZE = {'paddle': (40,100), 'ball': (30,30)}

POS = {'player': (WINDOW_WIDTH - 50, WINDOW_HEIGHT / 2), 'opponent': (50, WINDOW_HEIGHT / 2)}

SPEED = {'player': 500, 'opponent': 250, 'ball': 300}

COLORS = {
    'paddle': '#835945',
    'paddle shadow': '#b12521',
    'ball': '#6aa84f',
    'ball2' : '#271a14',
    'ball shadow': '#c14f24',
    'bg': '#C1aca2',
    'background' : '#f4e9e2'
}