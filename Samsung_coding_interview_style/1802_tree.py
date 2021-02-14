import copy, sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
App = [list(map(int,input().split())) for _ in range(n)]
A = [[5]*n for _ in range(n)]
trees = dict()

for _ in range(m):
    x,y,z = map(int,input().split())
    trees.setdefault((x-1, y-1),deque()).append(z)

direction = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

def spring_summer():
    global trees, A
    next_trees = copy.deepcopy(trees)

    for x,y in next_trees.keys(): # 나무들 있는 각 좌표
        yangbun = copy.deepcopy(A[x][y]) # 현재 양분
        dead = 0

        for idx, age in enumerate(next_trees[(x,y)]): # 좌표에 있는 나무 나이
            if age <= yangbun:
                yangbun -= age
                trees[(x,y)][idx] += 1

            else:
                trees[(x,y)].pop()
                dead += age // 2

        A[x][y] = yangbun + dead


def autumn_winter():
    global trees, A
    next = copy.deepcopy(trees)

    for tree in next.keys():
        x, y = tree[0], tree[1]
        for i in next[tree]:
            if (i % 5) == 0:  # 5배수이면 번식
                for r, c in direction:
                    if x + r >= 0 and y + c >= 0 and x + r < n and y + c < n:
                        trees.setdefault((x+r, y+c), deque()).appendleft(1)

    # A[r][c] 만큼 양분 추가
    for i in range(n):
        for j in range(n):
            A[i][j] += App[i][j]


for _ in range(k):
    spring_summer()
    autumn_winter()
sum = 0
for t in trees.keys():
    sum += len(trees[t])
print(sum)