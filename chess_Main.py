#
# - Responsible for handling user input and maintaining the current game state
#

import pygame as p
from chess import chess_Engine

Width = Height = 512
Dimension = 8
sq_Size = Height // Dimension
max_FPS = 15
Images = []

def load_Images():
    pieces = ['wP', 'wR', 'wN', 'wB', 'wQ', 'wK',
          'bP', 'bR', 'bN', 'bB', 'bQ', 'bK']
    for piece in pieces:
        Images[piece] = p.transform.scale(p.image.load('images/' + piece + '.png'), (sq_Size, sq_Size))
