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
Images = {}


def load_Images():
    pieces = ['wP', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bP', 'bR', 'bN', 'bB', 'bQ', 'bK']
    for ps in pieces:
        Images[ps] = p.transform.scale(p.image.load('images/' + ps + '.png'), (sq_Size-5, sq_Size-5))


def main():
    running = True
    screen = p.display.set_mode((Width, Height))
    clock = p.time.Clock()
    gs = chess_Engine.gameState()

    sqSelected = () # If no square is selected, keep track of the last click (tuple:(row, col))
    plyrClicks = [] # keep track of player clicks (two tuples)

    screen.fill(p.Color('#00653f'))
    load_Images()
    p.init()


    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0]//sq_Size
                row = location[1]//sq_Size
                if sqSelected == (row, col):
                    sqSelected = ()
                    plyrClicks = []
                else:
                    sqSelected = (row, col)
                    plyrClicks.append(sqSelected)
                if len(plyrClicks) == 2:


        draw_Gamestate(screen, gs)
        clock.tick(max_FPS)
        p.display.flip()


def draw_Gamestate(screen, gs):
    draw_Board(screen)
    draw_Pieces(screen, gs.board)


def draw_Board(screen):
    colours = [p.Color('#FFFFFF'), p.Color('#00653f')]
    for r in range(Dimension):
        for c in range(Dimension):
            colour = colours[(r + c) % 2]
            p.draw.rect(screen, colour, p.Rect(c * sq_Size, r * sq_Size, sq_Size, sq_Size))


def draw_Pieces(screen, board):
    for r in range(Dimension):
        for c in range(Dimension):
            piece = board[r][c]
            if piece != '--':
                screen.blit(Images[piece], p.Rect(c * sq_Size, r * sq_Size, sq_Size, sq_Size))


if __name__ == '__main__':
    main()
