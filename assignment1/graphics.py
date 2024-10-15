import os
import shutil


BOARD_WIDTH   = 37
BOARD_HEIGHT  = 19

SCREEN_HEIGHT = shutil.get_terminal_size().lines
SCREEN_WIDTH  = shutil.get_terminal_size().columns
SCREEN_CENTER = (SCREEN_WIDTH // 2 , SCREEN_HEIGHT // 2)

COLOR_A = "\u001b[32m"    # green 
COLOR_B = "\u001b[36m"    # cyan
COLOR_C = "\u001b[31m"    # red

class position:
    x: int
    y: int

def move_cursor_to(x, y):
    print(f"\033[{x};{y}H", end="")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_board(board, original):
    cursor_x = SCREEN_CENTER[0] - BOARD_WIDTH//2, 
    cursor_y = SCREEN_CENTER[1] - BOARD_HEIGHT//2
    move_cursor_to(cursor_x, cursor_y)
    
    print(COLOR_B + "╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗")

    for i in range(9):
        cursor_y += 1
        move_cursor_to(cursor_x, cursor_y)

        row = "║"
        for j in range(9):
            if original and board[i][j] > 0 and original[i][j] <= 0:
                row += " " + COLOR_C + str(board[i][j]) + COLOR_B
            elif board[i][j] > 0:
                row += " " + COLOR_A + str(board[i][j]) + COLOR_B
            else: 
                row += "  " 

            if (j+1) % 3:
                row += " │"
            else:
                row += " ║"

        print(row)

        if (i+1) % 3 :
            print("╟───┼───┼───╫───┼───┼───╫───┼───┼───╢")
        elif i != 8 :
            print("╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣")


    print("╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝")

    

