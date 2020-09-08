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

##### 참고
# https://www.youtube.com/watch?v=yip5IObfAjI
# 주렁코드
#####

##### 요구사항
# 키워드별로 매치된 단어가 몇개인지 "순서대로" 배열에 담아 반환
## 효율성 개선에 관한 고민 필요.. -> trie(트라이 구조)
#####

##### 사용예정인 함수
# checkmatch
#####

class Node():
    def __init__(self, key):
        self.key = key  ## 시작값
        self.remain_length = {}  ## Terminal까지 남아있는 문자열의 길이
        self.children = {}  ## 자식노드


class Trie():
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head

        # 처음 들어오는 글자의 길이
        remain_length = len(string)

        if remain_length in curr_node.remain_length:
            curr_node.remain_length[remain_length] += 1
        else:
            curr_node.remain_length[remain_length] = 1

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            curr_node = curr_node.children[char]
            remain_length -= 1
            if remain_length in curr_node.remain_length:
                curr_node.remain_length[remain_length] += 1
            else:
                curr_node.remain_length[remain_length] = 1

    def search_count(self, string, check_length):
        curr_node = self.head
        # 찾아야할 "?"를 포함한 string의 길이가 없다면 return 0
        if check_length + len(string) not in curr_node.remain_length:
            return 0

        for char in string:
            ## 찾아야할 string이 없다면 return 0
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return 0

        ## string 은 존재하는데 check_length가 remain_length에 존재하는지 확인
        if check_length in curr_node.remain_length:
            return curr_node.remain_length[check_length]
        else:
            return 0


def solution(words, queries):
    t = Trie()
    inv_t = Trie()
    for word in words:
        t.insert(word)
        inv_t.insert(word[-1::-1])

    answer = []
    for i in range(len(queries)):
        query = queries[i]
        if query[0] == "?":
            query = query[-1::-1]
            chars = query.replace("?", "")
            check_length = len(query) - len(chars)
            answer.append(inv_t.search_count(chars, check_length))
        else:
            chars = query.replace("?", "")
            check_length = len(query) - len(chars)
            answer.append(t.search_count(chars, check_length))

    return answer


''' # 효율성.. ---
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
'''

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words, queries))
result = [3, 2, 4, 1, 0]
