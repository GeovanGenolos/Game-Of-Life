import numpy as np
import matplotlib as plt
import matplotlib.animation as animation

def update(frameNum, img, grid, N):
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            total = int ((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                          grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                          grid[(i-1)%N, (i-1%N)] +  grid[(i-1)%N, (j+1)%N] +
                          grid[(i+1)%N, (i-1%N)] +  grid[(i-1)%N, (j+1)%N]))
            
            if grid[i, j] == 1:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = 0
                else: 
                    if total == 3:
                        newGrid[i, j] = 1