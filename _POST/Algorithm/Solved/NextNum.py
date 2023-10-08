# 프로그래머스 Lv 0 다음에 올 숫자
#
# 배열 common은 최대 1000개의 원소를 갖고,
# 각 원소는 최대 2000 값을 가지므로
# 그 다음의 원소도 int 범위를 넘어서지 않는다.
# 단, 항이 0이면서 등비수열인 경우엔 무조건 0을 리턴한다.

def solution(common):
    answer = 0
    degree1 = common[1] - common[0]
    degree2 = common[2] - common[1]
    if degree1 == degree2:
        # 등차 수열인가?
        return common[-1] + degree1
    else:
        if common[0] == 0:
            return 0
        else:
            # 등비 수열인가?
            answer = common[-1] * (common[1]//common[0])
    return answer

