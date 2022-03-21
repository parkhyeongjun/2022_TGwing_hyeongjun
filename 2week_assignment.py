# 문제 1번
from re import U


def sum(a,b):
    answer = a + b 
    # your code
    return answer

# 문제 2번
def sub(a,b):
    answer = a - b 
# your code
    return answer

# 문제 3번
def mul(a,b):
    answer = a * b 
    # your code
    return answer

# 문제 4번
def div(a,b):
    answer = a / b 
   # your code
    return answer

# 문제 5번
def distance(x1,y1,x2,y2):
    pow_x = (x2 - x1)  ** 2
    pow_y = (y2 - y1) ** 2
    answer = (pow_x + pow_y) ** 0.5# your code
    return answer

# 문제 6번
def short():
    lylic = "life is short art is long"
    ans = (lylic[8:13])# your code
    return ans

# 문제 7번
def myReverse(string):
    ans = (string[::-1])# your code
    return ans

# 문제 8번
def letMeIntroduceMyself():
    name = input("이름을 입력하세요: ")
    hobby = input("취미를 입력하세요: ")
    university = input("재학 중인 대학을 입력하세요: ")
    birthday = input("생일을 입력하세요: ")
    birth_month = (birthday[2:4] + "월")
    birth_date = (birthday[4,6] + "일")
    ans = ("제 이름은 " + name +"입니다. 제 취미는 " + hobby + "이구요. 저는 " + university + "를 다니고 있습니다. 제 생일은 " + birth_month + birth_date + "입니다.")
    # your code
    return ans

# 문제 9번
def calcAI():
    first_num = int(input("첫번째 숫자를 입력하세요: "))
    sec_num = int(input("두번째 숫자를 입력하세요: "))
    sum = (first_num + sec_num)
    ans = ("두 수의 합은 " + str(sum) + " 입니다.")
    # your code
    return ans

