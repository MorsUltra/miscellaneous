import random

grid = [
    [0, 1, 2],  # integers
    [3, 4, 5],
    [6, 7, 8],
]


# | 0 | 1 | 2 |
# | 3 | 4 | 5 |
# | 6 | 7 | 8 |

def print_grid(grid):
    for row in grid:
        print(f"| {row[0]} | {row[1]} | {row[2]} |")


def check_win(grid):
    pass
#testing

win_conditions = [
    [[True, True, True],
     [False, False, False],
     [False, False, False]]
    ,
    [[False, False, False],
     [True, True, True],
     [False, False, False]]
    ,
    [[False, False, False],
     [False, False, False],
     [True, True, True]]
]
win = False
player = 0
piece = None

while not win:
    print_grid(grid)
    # Change the player
    player += 1
    player %= 2
    # Set the piece
    if player == 1:
        piece = "x"
    else:
        piece = "o"

    move_position = int(input("Where do you want to put your piece? "))
    row = move_position // 3
    column = move_position % 3
    grid[row][column] = piece  # check if this is already filled

    # | 0 | 1 | 2 |
    # | 3 | 4 | 5 |
    # | 6 | 7 | 8 |
    # grid[value] = new_value

    # put piece into grid here:
    # row //
    # column %
