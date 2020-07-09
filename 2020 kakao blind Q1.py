### 2020.07.09 00:01 시작
### 2020.07.09 01:48 채점 72점 ..
### 2020.07.09 02:02 채점 100점!!
### 문자열 압축 프로그램
### 문자열 슬라이싱, 리스트 활용 필요예상
### 입력받는 문자열 S 에 대해서 1<= s <= 1000


##### 사용예정인 변수
# 단어의 묶음 갯수 - (int) size // 1부터 시작
# 묶여진 단어 - unit 
# 묶여진 단어의 반복 횟수 - (int) count // 1부터 시작
# 현재 s 문자열에서 가르키고 있는 위치 - (int) pointer // 0부터 시작
# 현재 최소로 줄여진 문자열의 길이  - (int) minlen
# 중간 과정을 저장할 문자열 - temp
# 압축된 문자열 - zips
##### a = 2 / s = str(a) + s / print (s) 하면 count 와 temp를 연결 가능


##### 기본 알고리즘
# unit을 1부터 점점 늘려가며 총 len(zips)의 길이가 최소가 되는 지점을 찾는다?
# answer 의 값은 len(zips)가 될것?


#####


##### 고려사항
# minlen의 값이 한번 결정되면, 이보다 큰 unit을 가진경우는 제외한다. minlen보다 커지면 stop한다.
#####

# 풀어내는 함수
def solution(s):
    answer = 0
    minlen = len(s)
    size = 1
    
    # 특정 조건에서 break
    while True:
        point = 0
        count = 1
        temp = []
        zips = []

        for x in range(0,len(s),size) :
            unit = s[point : point+size] # 단위별로 s문자열에서 size갯수씩 끊어서 가져온다

            if x == 0:
                temp = unit
            elif temp == unit :  # 단위로 끊어진 문자열이 이전 문자열과 같다.
                count += 1
            elif temp != unit :
                if count > 1 :
                    for nu in list(str(count)):
                        zips.append(nu)
                for ch in temp:
                    zips.append(ch)
                count = 1
                temp = unit
            
            point = point + size
            if x+size >= len(s):
                if count > 1 :
                    for nu in list(str(count)): ## count가 10이 넘어갈경우 lsit에 [10,a] 가 아닌 [1,0,a]식으로 담겨야함
                        zips.append(nu)
                for ch in temp:
                    zips.append(ch)
                    
            if minlen < len(zips):  # 이미 구해진 압축값보다 큰경우
                break
        # for loop end

        if minlen > len(zips):
            minlen = len(zips)
 
        size += 1
        if size > minlen :
            break
    # while loop end
    
    answer = minlen
    return answer


# 예상 시나리오
s = input("자 영어 소문자로 입력해봐, 최대 길이는 1~1000 : ")

print(solution(s))

