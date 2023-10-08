# 프로그래머스 Lv 0 배열 조각하기
#
# for i in query:
# i가 짝수 인덱스에 있을 경우 arr[i+1], arr[i+2] ... 를 제거.
# i가 홀수 인덱스에 있을 경우 arr[i-1], arr[i-2] ... 를 제거.
# list에서 del 연산은 O(n) 시간복잡도이며,
# 최악의 경우 arr 100000개의 원소를 50000번 순회해야 하기에 시간 초과가 난다.
# 따라서 slice를 통해 새 list를 반환하는 식으로 풀어야 한다.

def solution(arr, query):
    q_len = len(query)
    a_len = len(arr)

    for i in range(q_len):
        if i%2==0:
            arr = arr[:query[i]+1]
        else:
            arr = arr[query[i]:]
    return arr