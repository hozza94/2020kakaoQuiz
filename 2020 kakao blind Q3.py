### 2020.07.13 11:33 am 시
### 자물쇠와 열쇠
### 돌기 = 1, 홈 = 0 // 전체를 합치는 경우엔 모두 1이 되는 경우
### 


##### 고려해야할 문제
# 회전 90, 180, 270도
# 윈도우 슬라이딩...

#####

##### 요구사항
# 3 <= N,M <= 20 의 2차원 배열 (nxn, mxm)
#####

##### 사용예정인 함수
# spin90 (횟수) x 123..
# move up down left right

##### 

'''
b = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1,]]
n b : print(cc)

[1, 1, 1, 1]
[1, 1, 1, 1]
[1, 1, 1, 1]
[1, 1, 1, 1]
for cc in b:
	for dd in cc:
		print (dd)
'''
import copy

def solution(key, lock):
    m = len(key)
    n = len(lock)
    t = n + 2*(m-1)

    # keylist = 4가지 회전 포함
    keylist = spinList(key)
    padd = windowpadd(m, n, lock)

    answer = True

    for arr in keylist:
        for x in range(n+m-1):
            for y in range(n+m-1):
                temp = copy.deepcopy(padd)
                for i in range(m):
                    for j in range(m):
                        temp[x+i][y+j] = temp[x+i][y+j] + arr[i][j]
                if checklock(m, n, temp):
                    return answer

    return False

def spinList (key):
    keylist = []
    m = len(key)
    slist = key

    # 정상, 90, 180, 270 4방향
    keylist.append(key)
    for k in range(3):
        temp = [[0 for col in range(m)] for row in range(m)]
        for i in range(m):
            for j in range(m):
                temp[j][m-1-i] = slist[i][j]
        keylist.append(temp)
        slist = temp
    return keylist

def windowpadd (m, n, lock):
    # t ,, window padding
    t = n + 2*(m-1)

    padd = [[0 for col in range(t)] for row in range(t)]
    for i in range(n):
        for j in range(n):
            padd[m-1+i][m-1+j] = lock[i][j]

    return padd

def checklock (m, n, padd):
    for i in range(n):
        for j in range(n):
            if padd[m-1+i][m-1+j] != 1 :
                return False
    return True


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))
