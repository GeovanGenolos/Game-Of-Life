import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update(frameNum, img, grid, N):
    # Copy grid since we need 8 neighbors for calculation and we go line by line
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            # Compute 8-neighbor sum using toroidal boundary conditions - x and y wrap around
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                         grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                         grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N]))
            
            # Apply Conway's rules
            if grid[i, j] == 1: # Alive
                if (total < 2) or (total > 3):
                    newGrid[i, j] = 0
            else: # Dead
                if total == 3:
                    newGrid[i, j] = 1

    # Update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

def main():
    # Grid size
    N = 100

    # Initial grid with random values
    grid = np.random.choice([0, 1], N*N, p=[0.8, 0.2]).reshape(N, N)

    # Set up plot
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ),
                                  frames=10, interval=200, save_count=50)

    plt.show()

if __name__ == '__main__':
    main()
