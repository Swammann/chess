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
        Images[ps] = p.transform.scale(p.image.load('images/' + ps + '.png'), (sq_Size, sq_Size))


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
