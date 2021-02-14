import copy

R, C, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]
dx, dy = (0,1,0,-1), (1,0,-1,0)
zero_map = [[0]*(C) for _ in range(R)]

cleaner_up = 0 # 공기청정기 윗부분 좌
for a in range(len(A)):
    if A[a][0] == -1:
        cleaner_up = a
        break
# 공기청정기 좌표 [cleaner_up][0], [cleaner_up+1][0]

def spread():
    global A
    draw = copy.deepcopy(zero_map)

    for r in range(R):
        for c in range(C):
            if A[r][c]!=0 and A[r][c]!=-1: # 공기청정기 좌표, 벽처리 -> 개수 파악 k개
                dust = A[r][c]//5
                k = 0
                for x,y in zip(dx,dy):
                    if r+x>=0 and r+x<R and c+y>=0 and c+y<C: # 바운더리 안에
                        if A[r+x][c+y] != -1: # 공기청정기 아니면
                            k+=1
                            draw[r+x][c+y] += dust
                draw[r][c] -= k*dust

    # k개의 Arc//5를 빼주고 인접에 더해주기

    for r in range(R):
        for c in range(C):
            A[r][c] += draw[r][c]


def clean():
    global A

    #윗방향 반시계방향 돌기

    init = 0
    r,c = cleaner_up, 1
    clock_dr, clock_dc = 0,1

    while (r,c) != (cleaner_up,0):
        init, A[r][c] = A[r][c], init
        if (r,c) == (cleaner_up, C-1):  clock_dr, clock_dc = -1, 0
        elif (r,c) == (0, C-1):         clock_dr , clock_dc= 0, -1
        elif (r,c) == (0, 0):           clock_dr, clock_dc = 1, 0
        r,c = r+clock_dr, c+clock_dc


    # 아랫방향 시계방향 돌기
    init = 0

    cleaner_down = cleaner_up+1
    r, c = cleaner_down, 1
    clock_dr, clock_dc = 0,1

    while (r, c) != (cleaner_down, 0):
        init, A[r][c] = A[r][c], init
        if (r, c) == (cleaner_down, C - 1): clock_dr, clock_dc = 1, 0
        elif (r, c) == (R-1, C - 1):        clock_dr, clock_dc = 0, -1
        elif (r, c) == (R-1, 0):            clock_dr, clock_dc = -1, 0
        r, c = r + clock_dr, c + clock_dc


def main():
    for _ in range(T): # T초간
        spread() # 확산
        clean() # 공기청정

    sumA = 0
    for i in range(R):  sumA += sum(A[i])
    print(sumA+2) # 전체 합


if __name__ == "__main__":
    main()