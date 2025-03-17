import time

# Forward and Backward A*
def repeated_forward_astar(grid, start, goal, tie_breaking='larger_g'):
    return repeated_astar(grid, start, goal, tie_breaking)

def repeated_backward_astar(grid, start, goal, tie_breaking='larger_g'):
    return repeated_astar(grid, goal, start, tie_breaking)

# Generates 50 grids using list comprehension and stores them in environmentGrids
environmentGrids = []
allPaths = []
saveGrids(environmentGrids)
environmentGrids = [mazeGeneration() for _ in range(numGridWorlds)]

firstGrid, _, firstStartingPoint, firstGoal = environmentGrids[0]

# Single grid visualization using Repeated Forward A*
start_time = time.time()
cost, firstPath, closedSet = repeated_forward_astar(firstGrid, firstStartingPoint, firstGoal)
end_time = time.time()
A_rf_time = end_time - start_time
print("Repeated Forward A star")
visualizeGrid(firstGrid, firstStartingPoint, firstGoal, firstPath, closedSet)
print(f'Runtime: {A_rf_time}')

# Single grid visualization using Repeated Backward A*
start_time = time.time()
cost2, firstPath2, closedSet2 = repeated_backward_astar(firstGrid, firstStartingPoint, firstGoal)
end_time = time.time()
A_bf_time = end_time - start_time
print("\n\nRepeated Backward A star")
visualizeGrid(firstGrid, firstStartingPoint, firstGoal, firstPath2, closedSet2)
print(f'Runtime: {A_bf_time}')
