graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B']),
         'F': set(['C'])}


def dfs(graph, start):
    visited, stack = set(), [start]
    # selama ada node di stack melakukan search
    while stack:
        print("kondisi stack skrg {}".format(stack))
        node = stack.pop()
        print("current node  {}".format(node))
        print("stack setelah node divisit {}".format(stack))
        print("visited node {}\n---------".format(visited))
        if node not in visited:
            visited.add(node)
            print("visited added with {}\n---------".format(visited))
            # masukan kedalam stack graph yang tersambung ke node
            stack.extend(graph[node] - visited)
    return visited

if __name__ == "__main__":
    print("dfs solution")
    vs = dfs(graph, 'A')
    print("visited graph: {}".format(vs))
