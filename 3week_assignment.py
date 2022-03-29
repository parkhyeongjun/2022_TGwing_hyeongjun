# 이번 주차부터는 컴파일 에러 등으로 프로그램 자체가 실행되지 않을 시에는 과제 점수 0점 처리합니다.
# 문제에서 요구하는 입출력 외에는 절대 포함해서 제출하지 마세요. 0점 처리합니다.
# 문제에서 요구하는 출력 형식, 반환 형식을 "모두" 지켜주세요. 지키지 않으면 오답처리 됩니다.
# 한 파일에 모든 문제를 풀이해서 제출하세요. 분리 제출 시 채점자 PC기준 최상위에 정렬되는 파일만 채점합니다.
# 제출 마감일: 2022-03-29 23:59, 지각 제출 시 점수에서 20% 감점입니다.

# 문제 1번
def question1():
    # your code
    return "next"

# 문제 2번
def leapYear(year):
    four = year % 4
    hundred = year % 100
    four_hund = year % 400
    if (four == 0 and hundred != 0):
        ans = "윤년입니다"
    elif four_hund == 0:
        ans = "윤년입니다"
    else:
        ans = "윤년이 아닙니다"
    # your code
    return ans

# 문제 3번
def alram(time):
    str_time = str(time)
    min = 0
    hour = 0
    status = "오전 "
    if len(str_time) == 3:
        hour = int(str_time[:1])
        min = int(str_time[1:]) -45
    elif len(str_time) == 4:
        hour = int(str_time[:2])
        min = int(str_time[2:]) -45
    if min < 0:
        hour = hour -1
        min = 60 + min
    if hour > 12:
        hour = hour - 12 
        status = "오후 "
    ans = status + str(hour) + "시 " + str(min) +"분"
    # your code
    return ans

# 문제 4번
def findDaesun(x1,y1,r1,x2,y2,r2):
    pow_x = (x2 - x1)  ** 2
    pow_y = (y2 - y1) ** 2
    center_distance = (pow_x + pow_y) ** 0.5
    sum_r1r2 = r1 + r2    
    is_inside = False
    r1r2_same = bool
    bigger_r = max(r1,r2)
    smaller_r = min(r1,r2)
    ans = 0
    if center_distance+smaller_r <= bigger_r:
        is_inside = True
    if r1 == r2:
        r1r2_same = True

    if center_distance > sum_r1r2 and is_inside == False:
        ans = 0
    elif (center_distance < sum_r1r2) and center_distance !=0 and is_inside == False:
        ans = 2
    elif center_distance == sum_r1r2 and is_inside == False:
        ans = 1
    elif (center_distance == 0) and r1r2_same == True:
        ans = "어딘지 모르겠다 오바"
    elif center_distance == 0 and r1r2_same == False and is_inside == True:
        ans = 0
    elif center_distance+smaller_r < bigger_r and is_inside ==True:
        ans = 0
    elif center_distance+smaller_r == bigger_r and is_inside == True:
        ans = 1
    elif center_distance+smaller_r > bigger_r and is_inside == True:
        ans=2
    
    # your code
    return ans

print(findDaesun())
