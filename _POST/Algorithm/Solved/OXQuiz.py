# 프로그래머스 Lv 0 OX 퀴즈
#
# 문자열 여러 개가 들어있는 배열 quiz에 대해,
# 옳은 수식은 O, 틀린 수식은 X를 배열에 담아 return한다.
# quiz 배열은 최대 길이가 10이고, 각 문장의 숫자는 int 범위 내이다.
# 따라서 for 문을 통해 quiz 배열 내 원소를 하나씩 체크하고,
# 각 문자열을 띄어쓰기 기준으로 split 하여 계산한다.


def solution(quiz):
    answer = []
    for i in quiz:
        my_list = i.split(" ")
        calc = 0
        if my_list[1] == "+":
            calc = int(my_list[0]) + int(my_list[2])
        else:
            calc = int(my_list[0]) - int(my_list[2])

        if int(my_list[4]) == calc:
            answer.append("O")
        else:
            answer.append("X")
    return answer

