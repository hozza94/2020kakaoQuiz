### 2020.09.02 15:30 pm 시작
### 가사검색
### 키워드 포함,, 와일드카드 "?" 존재
### ex fro?? = fro'do' fro'nt' fro'st'
### ex fro?? != fr'ame' fro'zen'

# 단어들의 배열 words
# 키워드의 배열 queries

##### 고려해야할 문제
# words 개수 2~100,000 이하
# 가사의 길이 1~10,000 이하 빈문자 x
# 가사에 동일 단어 여러번 나올경우 중복 제거 words엔 하나로만 제공
# 가사는 오직 알파벳 소문자로 구성, 특수문자 숫자 포함 x

# queries 길이 2~100,000 이하
# 검색 키워드의 길이 1~10,000 이하 빈문자 x
# 전체검색 키워드 길이의 합은 2~1,000,000이하
# 검색 키워드는 중복될수 있다.
# 알파벳 소문자와 와일드카드인 ?로만 이루어져있음
# 검색키워드는 와일드카드 문자인 ?가 하나이상 포함되어있고,
# ?는 접두사 or 접미사 하나로만 주어진다.
# ex ??odo, fro??, ????? 는 가능
# ex frodo, fr?do, ?ro?? 는 불가

#####

##### 요구사항
# 키워드별로 매치된 단어가 몇개인지 "순서대로" 배열에 담아 반환
## 효율성 개선에 관한 고민 필요..
#####

##### 사용예정인 함수
# checkmatch


#####


def solution(words, queries):
    answer = []

    for query in queries:
        count = 0
        for word in words:
            if checkmatch(word, query):
                count += 1
        answer.append(count)

    return answer


def checkmatch(word, query):
    check = True
    if len(word) == len(query):
        for n in range(len(word)):
            if word[n] == query[n]:
                continue
            elif query[n] == '?':
                continue
            else:
                check = False
                break
    else:
        check = False
    return check


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words, queries))
result = [3, 2, 4, 1, 0]
