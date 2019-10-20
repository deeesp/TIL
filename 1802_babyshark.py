import sys, heapq
input = sys.stdin.readline

N = int(input())
grid = [list(map(int,input().split())) for _ in range(N)]
q = []
fishes = dict()

# 0: 빈칸
# 1,2,3,4,5,6: 물고기 크기
# 9: 아기상어 위치


def init():
    for i in range(N):  # baby shark 찾
        for j in range(N):
            if grid[i][j]==9:
                heapq.heappush(q, (0,i,j))        # heapq 의 역할은 우선순위큐!!
                grid[i][j] = 0
                return


def bfs():
    body, eat, ans = 2, 0, 0
    check = [[False]*N for _ in range(N)]      # 왔는지 체크할 것이 필요

    while q:
        d, x, y = heapq.heappop(q)
        check[x][y] = True

        if 0 < grid[x][y] < body: # 자기보다 작은놈 먹기
            #print(x, y, grid[x][y], body, eat, d, ans)
            eat += 1
            grid[x][y] = 0

            if eat == body: # 몸 커지기
                body+=1
                eat=0

            ans += d
            d = 0


            while q:
                q.pop()
            check = [[False]*N for _ in range(N)]

        for dx, dy in (-1,0),(0,-1),(1,0),(0,1):

            nd, nx, ny = d+1, x+dx, y+dy
            if nx<0 or  nx >=N or ny < 0 or ny >= N: # 범위 밖에면
                continue
            if 0 < grid[nx][ny] > body or check[nx][ny]: # 자기보다 크거나 들린 곳이면
                continue

            check[nx][ny] = True
            heapq.heappush(q, (nd, nx, ny))
        #print(q, check)

    print(ans)

init()
bfs()