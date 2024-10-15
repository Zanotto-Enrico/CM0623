from graphics import *


########################################
############  CONSTRAINTS  #############
########################################

# FIRST CONSTRAINT: value in board[x][y] must not be already present in row x
def check_constaint_column(board, x,y):
    for i in range(9):
        if board[i][y] == board[x][y] and i != x: return False
    return True

# SECOND CONSTRAINT: value in board[x][y] must not be already present in column y
def check_constaint_row(board, x,y):
    for i in range(9):
        if board[x][i] == board[x][y] and i != y: return False
    return True

# THIRD CONSTRAINT: value in board[x][y] must not be already present in its 3x3 box
def check_constraint_box(board, x,y):
    x_vertex = (x // 3) * 3 
    y_vertex = (y // 3) * 3
    for i in range(x_vertex, x_vertex+3):
        for j in range(y_vertex,y_vertex+3):
            if board[x][y] == board[i][j] and (i,j) != (x,y): return False
    return True

########################################
#######  CONSTANT PROPAGATION   ########
########################################

# This function applies constraint propagation recursively to solve the Sudoku board.
# It tries to fill each empty cell with possible values (1-9) while ensuring that all Sudoku
# constraints (row, column, and 3x3 box) are satisfied. If a valid assignment is found, 
# it recursively attempts to solve the rest of the board. If no valid assignment is found, 
# it backtracks and tries a different value.
def recursive_constant_propagation(board):
    for i in range(9):
        for j in range(9):      
            if board[i][j] != 0:
                continue            # Skip filled cells

            for v in range(1, 10):  # Try possible values (1-9)
                board[i][j] = v
                                    # Check constraints

                if ( check_constaint_row(board, i, j) and 
                     check_constaint_column(board, i, j) and 
                     check_constraint_box(board, i, j) and 
                     recursive_constant_propagation(board)):     # recurse
                    return True  

            board[i][j] = 0         # If no valid assignment backtrack
            return False
    return True



########################################
###############   MAIN   ###############
########################################

board = []
def get_user_matrix():
    print("provide a matrix of 9x9 values:")
    for _ in range(9):
        row = input().strip()
        row = row.replace(".", "0")
        row = row.replace(" ", "")
        board.append([int(value)  for value in row[:9]])


get_user_matrix()
clear_screen()
print("          Original matrix:")
draw_board(board, None)
original = [row.copy() for row in board]
print("           Solved matrix:")
recursive_constant_propagation(board)
draw_board(board, original)
