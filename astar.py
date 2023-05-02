def astar(start, goal, h):
    open_list = [start] 
    closed_list = []
    g= {start: 0}
    f = {start: h(start, goal)}
    came_from= {}


    while open_list:
        current = min(open_list, key=lambda x: f[x]) 
        if current == goal: 
            return reconstruct_path(came_from, start, goal)
        open_list.remove(current) 
        closed_list.append(current)

        for neighbor in get_neighbors(current):
            tentative_g = g[current] + cost(current, neighbor)
            if neighbor in closed_list and tentative_g >= g[neighbor]: 
                continue
            if neighbor not in open_list or tentative_g < g[neighbor]:
                came_from[neighbor] = current
                g[neighbor] = tentative_g
                f[neighbor] = tentative_g + h(neighbor, goal)

                if neighbor not in open_list: 
                    open_list.append(neighbor)
    return None



def reconstruct_path(came_from, start, goal):
    path = [goal] 
    current = goal 
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

# define the graph and helper functions
# define the graph and helper functions
graph = {
    'A': [('B', 3), ('D', 2)],
    'B': [('A', 3), ('C', 4), ('D', 1)],
    'C': [('B', 4), ('D', 5), ('E', 6)],
    'D': [('A', 2), ('B', 1), ('C', 5), ('E', 7)],
    'E': [('C', 6), ('D', 7)],
    'F':[]
}

def get_neighbors(node):
    return [n[0] for n in graph[node]]

def cost(node1, node2):
    return next(n[1] for n in graph[node1] if n[0] == node2)

def heuristic(node, goal):
    return 0 # no heuristic, equivalent to Dijkstra's algorithm




start = input("Enter start node : ") 
goal = input("enter end node : ")
path = astar(start, goal, heuristic)


# display the output
if path:
    print("Shortest path from", start, "to", goal, ":", path) 
    total_cost = sum(cost(path[i], path[i+1]) for i in range(len(path)-1)) 
    print("Total cost:", total_cost) 
else:
    print("There is no path from", start, "to", goal)
