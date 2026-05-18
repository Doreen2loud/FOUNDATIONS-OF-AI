
# BREADTH FIRST SEARCH (BFS)


from collections import deque

# Graph representation
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': []
}

def bfs(graph, start, goal):

    # Queue for BFS
    queue = deque()

    # Store visited nodes
    visited = []

    # Add starting node
    queue.append(start)

    while queue:

        # Remove first node
        node = queue.popleft()

        # Check if visited
        if node not in visited:

            print("Visited:", node)

            visited.append(node)

            # Goal test
            if node == goal:
                print("\nGoal node found!")
                print("Search Path:", visited)
                return

            # Add neighbors
            for neighbor in graph[node]:
                queue.append(neighbor)

    print("Goal node not found")


# Run BFS
bfs(graph, 'A', 'H')