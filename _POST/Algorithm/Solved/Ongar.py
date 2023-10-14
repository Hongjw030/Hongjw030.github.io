# 프로그래머스 Lv 0 옹알이
#
# 문자열 aya, ye, woo, ma 를 가지고
# babling 인자로 주어지는 문자열을 표현할 수 있는지 나타낸다.
# 문자열은 최대 100개 주어지고, 각 문자열 길이는 최대 15자이며
# aya, ye, woo, ma 는 최대 한 번씩만 쓸 수 있다.
# 따라서 만들 수 있는 단어는
# 1개만 쓰는 경우 4
# 2개만 쓰는 경우 4*3 = 12
# 3개만 쓰는 경우 4*3*2 = 24
# 4개 다 쓰는 경우 4*3*2*1 = 24 >> 총 64개이다.
# 만약 for 문으로 문자열을 찾으면 비효율적일 것이니
# 탐색 시간복잡도가 O(1) 인 set을 활용하자.


from itertools import permutations

def solution(babbling):
    count = 0
    ong = ["aya", "ye", "ma", "woo"]
    result = ong[:]


    return count