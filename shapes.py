import numpy as np

def addGlider(i, j, grid):
    '''
    https://www.geeksforgeeks.org/conways-game-life-python-implementation/
    '''
    glider = np.array([[0, 1, 0],
                       [0, 0, 1],
                       [1, 1, 1]], dtype=np.float32)
    grid[i:i+3, j:j+3] = glider
    return grid

def addGosperGliderGun(i, j, grid):
    '''
    https://www.geeksforgeeks.org/conways-game-life-python-implementation/
    '''
    gun = np.zeros(11*38).reshape(11, 38)

    gun[5][1] = gun[5][2] = 1
    gun[6][1] = gun[6][2] = 1

    gun[3][13] = gun[3][14] = 1
    gun[4][12] = gun[4][16] = 1
    gun[5][11] = gun[5][17] = 1
    gun[6][11] = gun[6][15] = gun[6][17] = gun[6][18] = 1
    gun[7][11] = gun[7][17] = 1
    gun[8][12] = gun[8][16] = 1
    gun[9][13] = gun[9][14] = 1

    gun[1][25] = 1
    gun[2][23] = gun[2][25] = 1
    gun[3][21] = gun[3][22] = 1
    gun[4][21] = gun[4][22] = 1
    gun[5][21] = gun[5][22] = 1
    gun[6][23] = gun[6][25] = 1
    gun[7][25] = 1

    gun[3][35] = gun[3][36] = 1
    gun[4][35] = gun[4][36] = 1
    grid[i:i+11, j:j+38] = gun
    return grid
