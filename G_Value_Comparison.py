import time
# Define Repeated Forward A* Search Algorithm (smaller g-values)
def repeated_forward_astar_smaller_g(grid, start, goal, tie_breaking='larger_g'):
    return repeated_astar(grid, start, goal, tie_breaking)

# Define Repeated Forward A* Search Algorithm (larger g-values)
def repeated_forward_astar_larger_g(grid, start, goal, tie_breaking='smaller_g'):
    return repeated_astar(grid, start, goal, tie_breaking)

# Generates 50 grids using list comprehension and stores them in environmentGrids
environmentGrids = []
allPaths = []
saveGrids(environmentGrids)
environmentGrids = [mazeGeneration() for _ in range(numGridWorlds)]

# Values obtained from first grid
firstGrid, _, firstStartingPoint, firstGoal = environmentGrids[0]


# Forward A* with smaller g-values
forward_start_time = time.time()
forwardCost, forwardPath, closedSet = repeated_forward_astar_smaller_g(firstGrid, firstStartingPoint, firstGoal)
forward_end_time = time.time()
forward_elapsed_time = forward_end_time - forward_start_time

# Backward A* with larger g-values
forward2_start_time = time.time()
forward2Cost, forward2Path, closedSet2 = repeated_forward_astar_larger_g(firstGrid, firstStartingPoint, firstGoal)
forward2_end_time = time.time()
forward2_elapsed_time = forward2_end_time - forward2_start_time

print(f'Repeated Forward A* Runtime with smaller g-values: {forward_elapsed_time}')
print(f'Repeated Forward A* Runtime with larger g-values: {forward2_elapsed_time}')

visualizeGrid(firstGrid, firstStartingPoint, firstGoal, forwardPath, closedSet)
visualizeGrid(firstGrid, firstStartingPoint, firstGoal, forward2Path, closedSet2)

plt.show()
