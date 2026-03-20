import pygame
import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
pygame.init()
pygame.display.set_caption("Chess")

screen = pygame.display.set_mode((512,512))

images = {
    "wP": pygame.image.load("pieces/Chess_plt60.png"),
    "wR": pygame.image.load("pieces/Chess_rlt60.png"),
    "wN": pygame.image.load("pieces/Chess_nlt60.png"),
    "wB": pygame.image.load("pieces/Chess_blt60.png"),
    "wQ": pygame.image.load("pieces/Chess_qlt60.png"),
    "wK": pygame.image.load("pieces/Chess_klt60.png"),
    "bP": pygame.image.load("pieces/Chess_pdt60.png"),
    "bR": pygame.image.load("pieces/Chess_rdt60.png"),
    "bN": pygame.image.load("pieces/Chess_ndt60.png"),
    "bB": pygame.image.load("pieces/Chess_bdt60.png"),
    "bQ": pygame.image.load("pieces/Chess_qdt60.png"),
    "bK": pygame.image.load("pieces/Chess_kdt60.png"),
}

board = [
    ["bR","bN","bB","bQ","bK","bB","bN","bR"],
    ["bP","bP","bP","bP","bP","bP","bP","bP"],
    [" "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "],
    ["wP","wP","wP","wP","wP","wP","wP","wP"],
    ["wR","wN","wB","wQ","wK","wB","wN","wR"],
]

selected = None


def get_moves(board, row, col):
    moves = []
    piece = board[row][col]

    if piece == "wP":
        if board[row-1][col] == " ":
            moves.append((row-1, col))
            if row == 6 and board[row-2][col] == " ":
                moves.append((row-2, col))
        if col > 0 and board[row-1][col-1].startswith("b"):
            moves.append((row-1, col-1))
        if col < 7 and board[row-1][col+1].startswith("b"):
            moves.append((row-1, col+1))

    if piece == "bP":
        if board[row+1][col] == " ":
            moves.append((row+1, col))
            if row == 1 and board[row+2][col] == " ":
                moves.append((row+2, col))
        if col > 0 and board[row+1][col-1].startswith("w"):
            moves.append((row+1, col-1))
        if col < 7 and board[row+1][col+1].startswith("w"):
            moves.append((row+1, col+1))

    if piece in ["wR", "bR"]:
        enemy = "b" if piece.startswith("w") else "w"
        for i in range(row-1, -1, -1):
            if board[i][col] == " ":
                moves.append((i, col))
            elif board[i][col].startswith(enemy):
                moves.append((i, col))
                break
            else:
                break
        for i in range(row+1, 8):
            if board[i][col] == " ":
                moves.append((i, col))
            elif board[i][col].startswith(enemy):
                moves.append((i, col))
                break
            else:
                break
        for i in range(col-1, -1, -1):
            if board[row][i] == " ":
                moves.append((row, i))
            elif board[row][i].startswith(enemy):
                moves.append((row, i))
                break
            else:
                break
        for i in range(col+1, 8):
            if board[row][i] == " ":
                moves.append((row, i))
            elif board[row][i].startswith(enemy):
                moves.append((row, i))
                break
            else:
                break

    return moves


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            col = x // 64
            row = y // 64
            if selected is None:
                if board[row][col] != " ":
                    selected = (row, col)
            else:
                old_row, old_col = selected
                moves = get_moves(board, old_row, old_col)
                if (row, col) in moves:
                    board[row][col] = board[old_row][old_col]
                    board[old_row][old_col] = " "
                selected = None

    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:
                color = (255, 206, 158)
            else:
                color = (111, 78, 55)
            pygame.draw.rect(screen, color, (col * 64, row * 64, 64, 64))
    if selected is not None:
        s_row, s_col = selected
        pygame.draw.rect(screen, (255, 255, 0), (s_col * 64, s_row * 64, 64, 64), 3)
                         
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece != " ":
                screen.blit(images[piece], (col * 64, row * 64))

    pygame.display.flip()