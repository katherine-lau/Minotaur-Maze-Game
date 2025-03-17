import heapq

class State:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g = float('inf')   #Cost to reach goal
        self.h = 0  #Manhattan distance
        self.f = float('inf')   #f(s) = g(s) + h(s)
        self.parent = None

    def __lt__(self, other):
        return self.f < other.f

    def manhattan(self, goal):
        self.h = abs(self.x - goal.x) + abs(self.y - goal.y)
        self.f = self.g + self.h

    def update(self, goal, parent):
        self.h = abs(self.x - goal.x) + abs(self.y - goal.y) #Manhattan distance
        if parent:
            self.h = max(self.h, parent.h)
        self.f = self.g + self.h

def succ(state, a, grid):
    x = state.x + a[0]
    y = state.y + a[1]
    if not (0 <= x < len(grid)) or not (0 <= y < len(grid[0])):
        return None #out of bounds
    if (grid[x][y] == -1):
        return None
    return State(x,y)

def A():   #actions
    return [(1, 0), (0, 1), (-1, 0), (0, -1)]

def A_a_star(grid, start, goal):
    """Note: blocked cells = -1"""
    state_s = State(start[0], start[1])
    state_g = State(goal[0], goal[1])
    state_s.g = 0
    state_s.manhattan(state_g)

    openList = []
    heapq.heappush(openList, state_s)
    closedListA = set()

    gVals = {(start[0], start[1]): 0}

    count = 0
    while openList:
        current = heapq.heappop(openList)

        if (current.x == state_g.x) and (current.y == state_g.y):    #goal reached
            path = []
            while current:
                path.append((current.x, current.y)) #add current position to path
                current = current.parent
            path.reverse()
            #print("Iterations: ", count)    #iterations show how many times need to readjust path
            return path, closedListA
        closedListA.add((current.x, current.y))

        for action in A():
            neighbor = succ(current, action, grid)
            if neighbor is None or ((neighbor.x, neighbor.y) in closedListA):
                continue

            #make sure in bounds and not already crossed
            if not (0 <= neighbor.x < len(grid)) or not (0 <= neighbor.y < len(grid[0])) or (grid[neighbor.x][neighbor.y] == -1):
                continue

            newG = current.g + 1   #g for neighbor
            neighbor.update(state_g, current)

            if ((neighbor.x, neighbor.y) not in gVals) or (newG < gVals[(neighbor.x, neighbor.y)]):
                neighbor.g = newG
                neighbor.manhattan(state_g)
                neighbor.parent = current
                gVals[(neighbor.x, neighbor.y)] = newG

                heapq.heappush(openList, neighbor)
        count += 1
    #print("Iterations: ", count)    #iterations show how many times need to readjust path
    return None #if no viable path is found

"""
grid = [
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0]
]
start = (0, 0)
goal = (4, 4)

path = a_star(grid, start, goal)


if path:
    print("Path:", path)
else:
    print("No path found.")
"""

