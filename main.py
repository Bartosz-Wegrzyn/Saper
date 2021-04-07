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


def make_grid(size):
    s = {"H":9, "W": 9, "Bombs": 10}
    m = {"H":16, "W": 16, "Bombs": 40}
    l = {"H":16, "W": 30, "Bombs": 99}
    if size == "s": grid_meta = s
    if size == "m": grid_meta = m
    if size == "l": grid_meta = l

    arr = np.zeros((grid_meta["H"], grid_meta["W"]), dtype=int)



    for i in range(grid_meta["Bombs"]):
        while True:
            a = random.randint(0, grid_meta["H"]-1)
            b = random.randint(0, grid_meta["W"]-1)

            if arr[a][b] == 0:
                arr[a][b] = 1
                break
            else:
                continue
    return arr

print("Welcom in Sapper Game!")
size = input("Choose size ('s', 'm' or 'l'): ")

print(make_grid("l"))


