from queue import PriorityQueue

# Graph representation
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 6)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 2,
    'G': 0
}

def astar(start, goal):
    open_set = PriorityQueue()
    open_set.put((0, start))

    came_from = {}
    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0

    while not open_set.empty():
        current = open_set.get()[1]

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)
            path.reverse()

            print("Optimal Path:", path)
            print("Total Cost:", g_cost[goal])
            return

        for neighbor, cost in graph[current]:
            temp_g = g_cost[current] + cost

            if temp_g < g_cost[neighbor]:
                came_from[neighbor] = current
                g_cost[neighbor] = temp_g

                f_cost = temp_g + heuristic[neighbor]
                open_set.put((f_cost, neighbor))

astar('A', 'G')