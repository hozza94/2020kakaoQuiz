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

def solution(key, lock):
    lkey = len(key)
    llock = len(lock)
    keylist = spinList(key)
    
    answer = True
    return answer

def spinList (key):
    keylist = []
    lkey = len(key)
    slist = key

    # 정상, 90, 180, 270 4방향
    keylist.append(key)
    for m in range(3):
        temp = [[0 for col in range(lkey)] for row in range(lkey)]
        for i in range(lkey):
            for j in range(lkey):
                temp[j][lkey-1-i] = slist[i][j]
        keylist.append(temp)
        slist = temp
    return keylist

    
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock =  [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key,lock))
