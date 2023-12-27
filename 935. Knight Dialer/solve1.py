#https://leetcode.com/problems/knight-dialer/description/
def knightDialer(n):
    def find_paths_iterative(graph, start_node, path_size):
        output = 0
        # paths = []
        stack = [(start_node, [start_node])]

        while stack:
            current_node, current_path = stack.pop()

            if len(current_path) == path_size:
                # paths.append(current_path)
                output = (output + 1) % 1000000007
                continue

            for neighbor in graph[current_node]:
                stack.append((neighbor, current_path + [neighbor]))
        return output

    moves = {0: [4, 6],
             1: [6, 8],
             2: [9, 7],
             3: [8, 4],
             4: [3, 9, 0],
             5: [],
             6: [1, 7, 0],
             7: [6, 2],
             8: [3, 1],
             9: [2, 4]}

    x = [find_paths_iterative(moves, i, n) for i in range(10)]
    print(x)
    # y = [len(i) for i in x]
    return sum(x)

print(knightDialer(3311))