def solution(n):
    answer = [[0]*n for _ in range(n)]
    count = 1
    direction = 0
    start = 0
    end = n
    while(count<= (n*n)):
        if direction == 0:
            for i in range(start, end):
                answer[start][i] = count
                count += 1
            direction = 1

        if direction == 1:
            for i in range(start+1, end):
                answer[i][end-1] = count
                count += 1
            direction = 2

        if direction == 2:
            for i in range(start+1, end):
                answer[end-1][end-i-1] = count
                count += 1
            direction = 3

        if direction == 3:
            for i in range(start+1, end-1):
                answer[end - 1- i][start] = count
                count += 1
            direction = 0
            start += 1
            end -= 1
    return answer

def printArr(arr):
    num = len(arr)
    for i in range(num):
        print(arr[i])
printArr(solution(5))
