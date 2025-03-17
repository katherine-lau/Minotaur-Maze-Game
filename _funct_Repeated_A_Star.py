import random
import numpy as np
import matplotlib.pyplot as plt
import heapq

# Define the Manhattan distance heuristic function
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Define Repeated A* Search Algorithm
def repeated_astar(grid, start, goal, tie_breaking, max_iterations=10000):
    size = grid.shape[0] # int
    open_list = [] # heap implementation on list
    closed_set = set() # set
    g_values = {start: 0} # dict
    came_from = {} # dict
    heapq.heappush(open_list, (heuristic(start, goal), 0, start)) # Push the start node into the heap

    iteration = 0 # Max iterations are 10,000 (approximately 101x101)

    while open_list:
        iteration += 1

        if iteration > max_iterations:
            print("Search took too long, stopping.") # Make sure no infinite iterations
            return float('inf'), []

        _, g, current = heapq.heappop(open_list) # Get node with the lowest f-value from the priority queue (heuristic, g-value, current)

        if grid[current[0], current[1]] == 1:
            print(f"Error! Expanding a wall at {current}!") # Make sure not expanding a wall

        if current in closed_set: # Skip if it's already in the closed set, else add
            continue
        
        if grid[current[0], current[1]] == 0:
            closed_set.add(current)
        #print(f"Visiting: {current}, g-value: {g}")  # Debugging

        if current == goal:
            print(f"Goal reached in {iteration} iterations.")

            # Reconstruct the path we got from goal to start
            path = []

            while current in came_from:
                path.append(current)
                current = came_from[current] # came_from is a dict
            path.append(start)

            return g_values[goal], path[::-1], closed_set  # Return cost & our reconstructed path

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]: # All four possible directions of movement
            neighbor = (current[0] + dx, current[1] + dy) # Calculate neighbor coordinates

            if not (0 <= neighbor[0] < size and 0 <= neighbor[1] < size): # Must be within grid boundaries
                continue

            if grid[neighbor[0], neighbor[1]] == 1:
                print(f"Warning! Wall at {neighbor} is being considered.") # Make sure we're not considering walls as neighbors

            if 0 <= neighbor[0] < size and 0 <= neighbor[1] < size and grid[neighbor[0], neighbor[1]] == 0: # If within bounds and not a wall
                new_g = g_values[current] + 1 # Update our g-value for our neighbor

                if neighbor not in g_values or new_g < g_values[neighbor]: # If new neighbor or better path to neighbor, update
                    g_values[neighbor] = new_g
                    came_from[neighbor] = current
                    f = new_g + heuristic(neighbor, goal) # Compute f-value (priority)
                    priority = f - new_g if tie_breaking == 'larger_g' else f + new_g # Tie-breaking strategy f(n) = g(n) + h(n), total cost = current cost + predicted cost
                    heapq.heappush(open_list, (priority, new_g, neighbor)) # Push to open list (priority queue)

    print("Path not found.") # In case we don't find a path
    return float('inf'), []
