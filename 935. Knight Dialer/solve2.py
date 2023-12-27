#https://leetcode.com/problems/knight-dialer/description/
def knightDialer(n):
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

    table = [[None] * (n + 1) for i in range(10)]
    for i in range(10):
        table[i][0] = 0
        table[i][1] = 1

    for steps in range(2, n + 1):
        for number in range(10):
            s = 0
            for accesable_from in moves[number]:
                s = (s + table[accesable_from][steps - 1]) % 1000000007
            table[number][steps] = s
    output = 0
    for i in range(10):
        output = (output + table[i][-1]) % 1000000007
    return output

print(knightDialer(4))
print(knightDialer(3131))
print(knightDialer(1))
