#
# - Responsible for handling user input and maintaining the current game state
#

import pygame as p
import chess_Engine

p.init()
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


def main():
    p.init()
    screen = p.display.set_mode((Width, Height))
    clock = p.time.Clock()
    screen.fill(p.Color('#00653f'))
    gs = chess_Engine.gameState()
    load_Images()
    running = True

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        draw_Gamestate(screen, gs)
        clock.tick(max_FPS)
        p.display.flip()

def draw_Gamestate(screen, gs):
    draw_Board(screen)
    draw_Pieces(screen, ps.board)

def draw_Board(screen):


def draw_Pieces(screen, board):
    ...


if __name__ == '__main__':
    main()







