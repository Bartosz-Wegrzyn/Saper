'''
    I am tying to make clasic Saper Game. Just for practice.


    Pseudo code:

        Grid Class:

            s:  H:9, W:9, Bombs: 10,
            m:  H:16, W:16, Bombs: 40,
            l:  H:16, W:30, Bombs: 40,

            every field format: (bombsAround, isItBomb, Status)
                Number of bombs around: -> bombsAround
                    int
                Value:
                    0 - no Bomb
                    1 - Bomb
                Status:
                    0 - no clicked
                    1 - flag
                    2 - question mark
                    1 - clicked


                1. Make array witch size H and W
                2. put Bombs in random places on grid (0, 1, 0)
                3. For every no_bomb field:
                    no_bomb == (check_how_many_bombs_is_around(), 0, 0)

        # Check_how_many_bombs_is_around(indexX, indexY):   in Progress
        #     # sum_of_bombs = 0
        #     #     if indexY-1 !< 0:
        #     #             if is_bomb(grid(indexY -1 , indexX)) == True:
        #     #                 sum_of_bombs += 1
        #     #
        #     #     (indexY -1 , indexX -1)
        #     #
        #     #
        #     #
        #     #
        #     #     (indexY -1 , indexX +1)
        #     #
        #     #                     top:
        #     #                     (indexY +1, indexX -1)
        #     #                     (indexY +1, indexX)
        #     #                     (indexY +1, indexX +1)
        #     #
        #     #
        #     #                     (indexY, indexX-1)
        #     #                     (indexY, indexX+1)

            for X, Y in range(if indexY-1 !< 0: 0 else 0,



        Game logic:
            Before first move:
                1. Open a app.
                2. Auto open Saper game with grid 10x10
                3. Show counter with number of mins left.

            After fitst click:
                1. Change the
                1. Clock start.

            During turn:

                Right click:
                    0. Make flag:
                        if bomb counter == 0 -> do nothing
                         else -> Make Flag, bomb counter -1
                    0. Make question mark



                1. Click on field
                    if file have a flag or question mark -> do noting
                        else  If under clicked field is bomb - > show all grid, clock stop,  Game over window.
                                else -> show that field
                                    if undiscovered fields == bombs on a map ->show all grid, clock stop, You Win!! window.
                                        else -> continue




'''


import numpy as np
import random


def make_grid(grid_size):

    if grid_size == "s": grid_meta = {"H":9, "W": 9, "Bombs": 10}
    if grid_size == "m": grid_meta = {"H":16, "W": 16, "Bombs": 40}
    if grid_size == "l": grid_meta = {"H":16, "W": 30, "Bombs": 99}

    field_status = np.zeros((grid_meta["H"], grid_meta["W"]), dtype=int)
    bombs_map = np.zeros((grid_meta["H"], grid_meta["W"]), dtype=int)
    for i in range(grid_meta["Bombs"]):
        while True:
            a = random.randint(0, grid_meta["H"]-1)
            b = random.randint(0, grid_meta["W"]-1)

            if bombs_map[a][b] == 0:
                bombs_map[a][b] = 1
                break
            else: continue

    full_board = bomb_map_to_full_board(bombs_map, grid_meta)

    return full_board, field_status

def bomb_map_to_full_board(bombs_map, grid_meta):
    full_board = np.zeros((grid_meta["H"], grid_meta["W"]), dtype=int)


    for row in range(grid_meta["H"]):
        for colum in range(grid_meta["W"]):
            if bombs_map[row][colum]==1:
                full_board[row][colum]=-1
            else:

                # field
                if grid_meta["H"]-1 > row > 0 and grid_meta["W"]-1 > colum > 0: # center fields
                    full_board[row][colum] = bombs_map[row-1][colum-1]+\
                                            bombs_map[row-1][colum]+\
                                            bombs_map[row-1][colum+1]+\
                                            bombs_map[row][colum-1]+\
                                            bombs_map[row][colum+1]+\
                                            bombs_map[row+1][colum-1]+\
                                            bombs_map[row+1][colum]+\
                                            bombs_map[row+1][colum+1]
                #Corners
                elif row == 0 and colum == 0: # left top corner
                    full_board[row][colum] = bombs_map[row][colum+1]+\
                                            bombs_map[row+1][colum+1]+\
                                            bombs_map[row+1][colum]

                elif row == grid_meta["H"]-1 and colum == 0:  # bottom left corner
                    full_board[row][colum] = bombs_map[row-1][colum] + \
                                            bombs_map[row-1][colum+1] + \
                                            bombs_map[row][colum+1]

                elif row == grid_meta["H"]-1 and colum == grid_meta["W"]-1:  # bottom right corner
                    full_board[row][colum] = bombs_map[row][colum-1] + \
                                            bombs_map[row-1][colum-1] + \
                                            bombs_map[row-1][colum]

                elif row == 0 and colum == grid_meta["W"]-1: # right top corner
                    full_board[row][colum] = bombs_map[row][colum-1]+\
                                            bombs_map[row+1][colum-1]+\
                                            bombs_map[row+1][colum]

                # Rows and Columns on sides
                elif row == 0 and  grid_meta["W"]-1 > colum > 0 : # top row

                    full_board[row][colum] = bombs_map[row][colum+1]+\
                                            bombs_map[row+1][colum+1]+\
                                            bombs_map[row+1][colum]+\
                                            bombs_map[row][colum-1] + \
                                            bombs_map[row+1][colum-1]

                elif 0 < row < grid_meta["H"]-1 and colum == 0: # left column
                    full_board[row][colum] = bombs_map[row-1][colum] + \
                                            bombs_map[row-1][colum+1] + \
                                            bombs_map[row][colum+1]+\
                                            bombs_map[row+1][colum+1] + \
                                            bombs_map[row+1][colum]

                elif 0 < row < grid_meta["H"]-1 and colum == grid_meta["W"]-1:  # right column
                    full_board[row][colum] = bombs_map[row][colum-1]+\
                                            bombs_map[row+1][colum-1]+\
                                            bombs_map[row+1][colum]+\
                                            bombs_map[row-1][colum-1] + \
                                            bombs_map[row-1][colum]


                elif row == grid_meta["H"]-1 and grid_meta["W"]-1 > colum > 0:  # bottom row
                    full_board[row][colum] = bombs_map[row-1][colum] + \
                                            bombs_map[row-1][colum+1] + \
                                            bombs_map[row][colum+1]+\
                                            bombs_map[row][colum-1] + \
                                            bombs_map[row-1][colum-1]
                else:
                    print("Error!!!!1")
                    print("Operacja: ", row, colum)
                    print("row: ", row)
                    print("col: ", colum)

    return full_board


# def make_guess(full_board, hight, width):
#     guess =
#     print(guess)



def game_loop():
    full_board, field_status = make_grid("s")
    print(full_board)
    while True:
        r=int(input("Row: "))
        c=int(input("Col: "))
        m=input("Move: ") #lc, (?, F, C)

        if m == "lc":
            if field_status[r][c] == 0:
                if full_board[r][c] == -1:
                    print("game over!")
                    exit()
                else:
                    field_status[r][c] = full_board[r][c]


        if m == "?":
            if field_status[r][c] == 0 or "F" or "C":
                field_status[r][c] = -2


        if m == "F":
            pass
        if m == "C":
            pass
        print(field_status)


game_loop()
