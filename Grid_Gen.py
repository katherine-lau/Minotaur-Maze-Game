import random
import numpy as np
import matplotlib.pyplot as plt

#constants based on the parameters in part 0
gridSize = 101
numGridWorlds = 50
#did not use as we ended up using a different method
blockedProb = 0.3
unblockedProb = 0.7

def initializeGrid():
    #intializing a grid of a given size where all the cells are set to unvisited (initialized as -1)
    return np.full((gridSize, gridSize), -1)

def getNeighbors(x, y, grid):
    #retrieves the unvisited neighbors of the current cell
    neighbors = []
    #creating corridor walls by moving by 2 units inbetween cells, valid directions are south, north, west, east
    directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy #defining neighbors
        if 0 <= nx < gridSize and 0 <= ny < gridSize and grid[nx, ny] == -1: #checking the coditions for the neighbor cells, if it in bounds and if it is unvisited
            neighbors.append((nx,ny))
    random.shuffle(neighbors) #random tie-breaking introduced by randomly shuffling the order of the neighbors
    return neighbors

def mazeGeneration():
    #this will generate a maze using iterative Randomized DFS (stack-based)
    #empty grid and stack for DFS
    grid = initializeGrid()
    stack = []

    #starting from a random cell (our start point)
    startingX, startingY = random.choice(range(1, gridSize, 2)), random.choice(range(1, gridSize, 2)) #stride of 2 to avoid walls
    grid[startingX, startingY] = 0 #marking as visited and unblocked as this is the starting point
    #starting point is pushed onto the stack for DFS traversal
    stack.append((startingX, startingY))

    #initialize goal state at the bottom-right corner
    goalState = (gridSize - 2, gridSize - 2)

    #keeping track of starting point
    startingPoint = (startingX, startingY)

    #storing the path
    path = [(startingX, startingY)]

    #DFS with stack continues until stack is empty-- meaning no unvisited cells
    while stack:
        x, y = stack[-1]
        #retrieving the unvisited nieghbors of the current cell
        neighbors = getNeighbors(x, y, grid)
        if neighbors:
            nx, ny = neighbors[0]
            #remove wall between current cell and chosen neighbor by marking it as unblocked
            grid[(x + nx)//2, (y + ny)//2] = 0  #open the wall
            if random.random() < unblockedProb:
                grid[nx, ny] = 0  #mark the neighbor as visited

            stack.append((nx, ny))  #neighbor is pushed onto the stack
            path.append((nx, ny))  #adding to path
        else:
            stack.pop()  #backtrack if no unvisited neighbors

    return grid, path, startingPoint, goalState

def saveGrids(grids):
  #saving grids a .npy files
    for i, (grid, _, _, _) in enumerate(grids):
        np.save(f'gridWorld{i}.npy', grid)

def visualizeGrid(grid, startingPoint, goal, path, closedSet): #used for testing if the structure of the maze is correct
#def visualizeGrid(grid, startingPoint, goal):
    plt.imshow(grid, cmap = 'gray')
    #unblocked is white and blocked is black

    #coloring for closedSet
    exp_x, exp_y = zip(*closedSet)
    plt.scatter(exp_y, exp_x, color = 'purple', s=1, linestyle = (1, (3,1)), linewidth = 2, alpha = 0.5)



    #coloring for path
    #for (x, y) in path:(this method takes wayyy too long)
            #plt.scatter(y, x, color='blue', s=5, marker='s', label='Path')
    path_x, path_y = zip(*path)
    plt.plot(path_y, path_x, color = 'blue', linestyle = (1, (3,1)), linewidth = 2)



    #coloring the start and end point
    plt.scatter(startingPoint[1], startingPoint[0], color='green', s=100, marker='o', label='Start Point')
    plt.scatter(goal[1], goal[0], color='red', s=100, marker='x', label='Goal Point')
    #maze title
    plt.title('Generated Grid')
    plt.show()

def visualizeAllGrids(grids, closedSets):
    #setting up the number of rows and columns for the subplots
    numCols = 5  #display 5 grids per row for layout purposes
    #calculating the number of rows needed for the total number of grids, using the values of True and False to determine is additional row is necessary
    numRows = len(grids)//numCols + (len(grids)%numCols > 0)


    #create the figure for subplots
    plt.figure(figsize=(50, 50))

    for i, (grid, path, startingPoint, goal) in enumerate(grids):
        plt.subplot(numRows, numCols, i + 1) #organizing individual grids in the subplot
        plt.imshow(grid, cmap='gray') #grids are in the gray colormap


        #for path colorization
        #for (x, y) in path:(this method takes wayyy too long)
            #plt.scatter(y, x, color='blue', s=5, marker='s', label='Path')
        path_x, path_y = zip(*path)
        plt.plot(path_y, path_x, color = 'blue', linestyle = (1, (3,1)), linewidth = 2)
    
        exp_x, exp_y = zip(*closedSets[i])
        plt.scatter(exp_y, exp_x, color = 'purple', s=1, linestyle = (1, (3,1)), linewidth = 2, alpha = 0.5)

        #marking start and end point
        plt.scatter(startingPoint[1], startingPoint[0], color='green', s=200, marker='o', label='Start Point')
        plt.scatter(goal[1], goal[0], color='red', s=200, marker='x', label='Goal Point')
        #numbering the grids
        plt.title(f'Grid {i + 1}') #title of each grid
        plt.axis('off')  #turns off the axis
        #plt.legend() #displaying the legend to show start and goal cells

    plt.tight_layout() #for spacing between subplots
    plt.show()
