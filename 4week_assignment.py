# your code 부분에 코딩하여 문제를 풀이해주세요.
# print 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 4주차 과제에는 출력을 요구하는 문제가 없습니다.
# input 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 4주차 과제에는 입력을 요구하는 문제가 없습니다.
# answer 변수를 사용하여 문제를 풀이하세요. 반환값은 answer 변수입니다.
# 함수 내에서 컴파일 에러, 런타임 에러가 발생하면 해당 문제 점수 0점 처리하겠습니다.
# 함수명 변경하지 마세요. 변경 시 해당 문제 점수 0점 처리하겠습니다.
# 제출 기한: 2022년 4월 5일 23시 59분.
# 지각 제출 기한: 2022년 4월 6일 23시 59분. 주차 점수에서 20% 감점

# 문제 1번
from ast import NotIn


def intervention(queue):
    # your code
    i = queue.index("성은")
    if i<4:
        queue.append("승호")
    elif i>=4:
        queue.insert(i+1,"승호")
    answer = list(queue)
    return answer

# 문제 2번
def pascal(n):
    answer = list()
    # your code
    return answer

# 문제 3번
def auto_complete(entry, searchWords):
    # your code
    n = len(searchWords)
    ans_list = []
    for i in range(n):
        if entry in searchWords[i-1]:
            ans_list.append(searchWords[i-1])
        else:
            continue
    ans_list.sort()
    answer = list(ans_list)    
    return answer

# 문제 4번
def stock_price(stockChart):
    # your code
    answer = str()    
    return answer

# 문제 5번
def decryption(letter):
    # your code
    n = len(letter)
    ans_list = []
    ans_str = ""
    for i in letter:
        if  96<ord(i)<120: 
            ans_list.append(chr(ord(i)+3))
        elif 119<ord(i):
            ans_list.append(chr(ord(i) - 23))
        else: 
            ans_list.append(i)
            continue
    ans_str = "".join(ans_list)
    answer = str(ans_str)    
    return answer