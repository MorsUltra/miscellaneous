import itertools


def show_grid(grid):
    for row in grid:
        print(f"| {row[0]} | {row[1]} | {row[2]} |")

    print("\n\n\n")


def move(player):
    player += 1
    return player % 2


def check_win(grid):
    pass


grid = [list(range(row * 3, row * 3 + 3)) for row in range(3)]

perms = map(list, set(itertools.permutations([False, False, True])))

templates = [[line] * 3 for line in perms] + \
            [[[line] * 3 for line in combination] for combination in perms]

player = move(0)
pos = 0

while not check_win(grid):
    show_grid(grid)
    player = move(player)
    piece = "x" if player else "o"

    pos = int(input(f"Player:{player}\nWhere do you want to put your piece"))

    while not isinstance(grid[pos // 3][pos % 3], int):
        pos = int(input(f"That's an invalid move\nPlayer:{player}\nWhere do you want to put your piece"))

    grid[pos // 3][pos % 3] = piece

# is this working? Can you type and see shit?
