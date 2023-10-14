# 프로그래머스 Lv 0 평행
#
# xy 좌표 4개가 있을 때 평행한 두 직선이 만들어지는지 확인하기.
# 평행은 기울기가 같은 두 선을 말하므로
# 4C2/2 = 3개의 경우 중 평행이 있는지를 찾아야 한다.

def solution(dots):
    # d0 d1 / d2 d3
    d01 = abs((dots[1][0] - dots[0][0]) / (dots[1][1] - dots[0][1]))
    d23 = abs((dots[3][0] - dots[2][0]) / (dots[3][1] - dots[2][1]))

    # d0 d2 / d1 d3
    d02 = abs((dots[2][0] - dots[0][0]) / (dots[2][1] - dots[0][1]))
    d13 = abs((dots[3][0] - dots[1][0]) / (dots[3][1] - dots[1][1]))

    # d0 d3 / d1 d2
    d03 = abs((dots[3][0] - dots[0][0]) / (dots[3][1] - dots[0][1]))
    d12 = abs((dots[2][0] - dots[1][0]) / (dots[2][1] - dots[1][1]))

    if (d01==d23) or (d02==d13) or (d03==d12):
        return 1
    return 0
