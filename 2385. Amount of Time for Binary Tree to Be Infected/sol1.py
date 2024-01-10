# https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/description/

def amountOfTime(root, start):
    def fillGraph(curr, parent, g):
        if curr.val not in g:
            g[curr.val] = set()
        if parent != None:
            g[curr.val].add(parent.val)
        if curr.left != None:
            g[curr.val].add(curr.left.val)
            fillGraph(curr.left, curr, g)
        if curr.right != None:
            g[curr.val].add(curr.right.val)
            fillGraph(curr.right, curr, g)
    g = {}
    fillGraph(root, None, g)
    # BFS:
    visited = set()
    distances = {}
    distances[start] = 0
    q = [start]
    while q:
        curr = q.pop(0)
        visited.add(curr)
        neighbours = g[curr]
        for vertex in neighbours:
            if vertex not in visited:
                visited.add(vertex)
                distances[vertex] = distances[curr] + 1
                q.append(vertex)
    return max(distances.values())
