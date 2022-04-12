# your code 부분에 코딩하여 문제를 풀이해주세요.
# print 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 5주차 과제에는 출력을 요구하는 문제가 없습니다.
# input 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 5주차 과제에는 입력을 요구하는 문제가 없습니다.
# result 변수를 사용하여 문제를 풀이하세요. 반환값은 result 변수입니다.
# 함수 내에서 컴파일 에러, 런타임 에러가 발생하면 해당 문제 점수 0점 처리하겠습니다.
# 함수명 변경하지 마세요. 변경 시 해당 문제 점수 0점 처리하겠습니다.
# 제출 기한: 2022년 4월 12일 23시 59분.
# 지각 제출 기한: 2022년 4월 13일 23시 59분. 주차 점수에서 20% 감점
import math
def calcCircleArea(r):
    r = float(r)
    area = math.pow(r,2)*math.pi
    ans = round(area,2)
    result = float(ans)
    return result
    '''[2]'''
def calcLog(a, b):
    if a == "e" or b == "e":
        if a == "e":
            a = math.e
            b = int(b)
        elif b == "e":
            a = int(a)
            b = math.e
        log = math.log(b,a)
        ans = round(log,2)        
    else: 
        a = float(a)
        b = float(b)
        log = math.log(b,a)
        ans = round(log, 2)
    result = float(ans)
    '''[3]'''
    return result
def calcSin(x):
    x = float(x)
    s = math.sin(x)
    ans = round(s,2)
    result = float(ans)
    '''[4]'''
    return result




def calcFactorial(x):
    x = int(x)
    ans = math.factorial(x)
    result = int(ans)
    '''[5]'''
    return result
def calcCombination(n, r):
    n = int(n)
    r = int(r)
    n_fact = calcFactorial(n)
    r_fact = calcFactorial(r)
    n_minus_r_fact = calcFactorial(n-r)
    ans = n_fact/(r_fact*n_minus_r_fact)
    result = int(ans)
    '''[6]'''
    return result

def calculator(order):
    answer = 0
    if "원넓이" in order:
        i = order.index(":")
        answer = calcCircleArea((order[i+1:]))
    elif "로그" in order:
        i = order.index(":")
        number = order[i+2:]
        split = number.split(' ')
        answer = calcLog((split[0]),(split[1]))
    elif "사인" in order:
        i = order.index(":")
        answer = calcSin((order[i+1:]))
    elif "팩토리얼" in order:
        i = order.index(":")
        number = order[i+1:]
        answer = calcFactorial((order[i+1:]))
    elif "조합" in order:
        i = order.index(":")
        number = order[i+2:]
        split = number.split(' ')
        answer = calcCombination((split[0]),(split[1]))        
    '''[1]'''
    return answer



print(calculator('원넓이: 10'))
print(calculator('로그: e 10'))
print(calculator('사인: 100'))
print(calculator('팩토리얼: 5'))
print(calculator('조합: 3 2'))