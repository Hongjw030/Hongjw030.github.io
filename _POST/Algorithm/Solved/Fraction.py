# 프로그래머스 Lv 0 분수의 덧셈
#
# 파라미터 4개 중 numer1 denom1 은 첫 분수의 분자 분모
# numer2 denom2 는 두번째 분수의 분자 분모이다.
# 두 분수를 더한 값을 기약 분수로 나타내야 하므로
# 1. 분모가 같으면 그대로 덧셈한다.
# 2. 분모가 다르면 둘의 최소공배수로 만들어 덧셈한다
# 3. 분모 분자의 최대 공약수를 구해 나눈다.
# math.gcd 함수는 시간 복잡도가 O(logN)이다.

import math

def solution(numer1, denom1, numer2, denom2):
    answer = []

    totalDenom = denom1
    lessDenom = math.gcd(denom1, denom2)
    if denom1 != denom2:
        totalDenom = lessDenom * (denom1//lessDenom) * (denom2 // lessDenom)
        numer1 *= totalDenom//denom1
        numer2 *= totalDenom//denom2

    totalNumer = numer1 + numer2

    less = math.gcd(totalDenom, totalNumer)
    answer.append(totalNumer//less)
    answer.append(totalDenom//less)
    return answer

