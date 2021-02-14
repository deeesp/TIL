import copy, sys
input = sys.stdin.readline

R, C, M = map(int, input().split())
# 상어 정보: (r,c)를 키로 해주, 속력, 이동방향, 크기
sharks = dict()

for m in range(M):
    r,c,s,d,z = map(int, input().split())
    sharks[(r,c)] = [s,d,z]
sharks = sorted(sharks, key= lambda x:(sharks.keys[1],sharks.keys[0]))

def fish(): # 낚시
    global fisher, sum, sharks
    if not sharks:  return

    next_shark = copy.deepcopy(sharks)
    col_fish = 1000

    for k in sharks.keys():
        if k[1]<fisher and sharks[k][1]<=2:
            del next_shark[k]
        if k[1]==fisher:
            if col_fish>k[0]:
                col_fish=k[0]

    if col_fish!=1000:
        sum += sharks[(col_fish,fisher)][2]
        del next_shark[(col_fish,fisher)]
        sharks = copy.deepcopy(next_shark)


def shark_mov(): # 상어 움직임
    global sharks
    mov = dict()

    for shark in sharks.items():
        r, c, ss, d, z = shark[0][0], shark[0][1], shark[1][0], shark[1][1], shark[1][2]

        s = ss

        if d<=2: # 상하
            while s:
                if d == 1: # 상향
                    if r > 1:  r -= 1
                    else:
                        d = 2
                        r += 1
                else:      # 하향
                    if r < R:  r += 1
                    else:
                        d = 1
                        r -= 1
                s -= 1

        else: #좌우
            while s:
                if d == 3:
                    if c!=C:  c+=1
                    else:
                        d = 4
                        c -= 1
                else:
                    if c!=1:  c-=1
                    else:
                        d = 3
                        c += 1
                s -= 1

        if (r, c) not in mov.keys():
            mov[(r, c)] = [ss, d, z]
        else:
            if mov[(r, c)][2] < z:  # 더 큰놈 잡아먹기
                mov[(r, c)] = [ss, d, z]

    sharks = copy.deepcopy(mov)



sum = 0
for c in range(1, C+1): # 낚시왕이 끝에 다다를 때까지
    fisher = c
    fish() # 낚시왕 오른쪽 한칸 이동 후 제일 가까운 상어 낚시
    shark_mov() # 상어 이동

print(sum)