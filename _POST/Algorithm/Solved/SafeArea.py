# 프로그래머스 Lv 0 안전 지대
#
# 지뢰에 대해, 위 아래 좌 우 대각선까지 총 8군데를 위험 지역이라 한다.
# 지뢰는 2차원 배열에서 1로 표시된다.
# 안전한 지역의 칸 수를 알아내기 위해, for 문으로 모든 칸을 접근한다.
# 지뢰를 만나면 그 근방 8칸 중 0이 있는 곳을 1로 표시하고, 만약 이미 1이 표시되었다면 넘어간다.
# 최악의 경우 총 칸은 10000 개이므로, for 문을 써도 시간 초과가 안 난다.
def check(i, j, arr):
    if arr[i][j]==0:
        arr[i][j] = 2

def checker(i, j, arr):
    #i, j는 지뢰의 위치
    # i1 i i2, j1 j j2
    n = len(arr)
    i1 = i-1 if i-1>=0 else 0
    i2 = i+1 if i+1<n else n-1
    j1 = j-1 if j-1>=0 else 0
    j2 = j+1 if j+1<n else n-1

    check(i1, j1, arr)
    check(i1, j, arr)
    check(i1, j2, arr)
    check(i, j1, arr)
    check(i, j2, arr)
    check(i2, j1, arr)
    check(i2, j, arr)
    check(i2, j2, arr)


def solution(board):
    answer = 0
    b_len = len(board)
    for i in range(b_len):
        for j in range(b_len):
            if board[i][j] == 1:
                checker(i, j, board)
    for line in board:
        for i in line:
            if i == 0:
                answer += 1
    return answer
