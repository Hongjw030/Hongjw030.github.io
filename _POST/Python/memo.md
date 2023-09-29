# 파이썬 메모장

### 다른 건 다 필요 없고 걍 헷갈리는 것만 가볍게 메모.

## 요약

ternary expression, minmax sum, list comprehension, 연산, 포맷팅, 

**자주 쓰는 함수**
```python
print(max(2,5))
print(min(2,5))

my_list = [1,2,3,5]
my_tuple = (1,2,3,6)
my_dict = {1:"one", 2:"two", 3:"three"}
print(sum(my_list))
print(sum(my_tuple))
# dict sum은 모든 key의 합을 리턴.
print(sum(my_dict))
```

**ternary expression**

불린 값에 따라 다른 값을 리턴하는 구문. 
```python
# 기존 if else문을 쓰면...
condition = True
if condition:
    my_string = "nice"
else:
    my_string = "not nice"
print(my_string)

# ternary expression을 쓰면...
condition = True
my_string = "nice" if condition else "not nice"
print(my_string)
```


**list comprehension**

새로운 리스트 복사해서 만들기
```python
origin = [1,2,3,4]
# 똑같은 리스트 복사
rep1 = [x for x in origin]
# [2,4,6,8] 생성
rep2 = [x*2 for x in origin]

```

**zfil**

문자열 길이 맞추기
```python
print("1".zfil(2)) #01 출력
print("333".zfil(2)) #그냥 그대로 333 출ㄹ력
print("a".zfil(4)) #000a 출력
print("abc".zfil(6)) #000abc 출력
```


**연산**
* 4 ** 2 = 16. 별 두개는 거듭제곱임. 
* 5 / 2 = 2.5 
* 5 // 2 = 2 몫 연산.
* 5 % 2 = 1 나머지 연산.
* 4 + 3 = 7
* 4.0 + 3 = 7.0 이렇게 소수가 합해지면 소수형으로 나온다.
* 6 / 3 = 2.0
* 6.0 / 3 = 2.0 나눗셈은 무조건 소수형으로 나와서 형변환 해야 함.
* 5//2 = 2지만, 5.0//2 = 2.0 이다. 소수가 들어가면 결과에도 무조건 소수!!


**숫자 함수**
* round(3.14) = 3 round함수는 반올림 함수이다.
* round(3.141592, 2) = 3.14 round함수는 두번째 인자로 몇 번째 소수점까지 살릴지 알아낸다. 


**문자 다루기**
* 파이썬에서는 문자열끼리의 덧셈, 곱셈 가능.
* 형변환은 int(3.6) , int(”5”) float(3)  str(3)
* 파이썬에서 int와 문자열을 연결할 수 없다.
* print( age + “살 입니다.”) >> 오류
* print(str(age) + “살 입니다.”) 이렇게 하자!!! 


**포멧팅**
* print(”{}살 {}cm {}kg 입니다.”.format(age, height, weight))
* my_string = ”{}살 {}cm {}kg 입니다.”
* print(my_string.format(age, height, weight))


type(True) >> boolean이 출력됨

type(3) >> Integer이 출력됨.

옵셔널 파라미터는 맨 마지막에 꼭 써줘야 함.

def myself(name, nationality="한국", age): >> 에러!!!

def myself(name, age, nationality="한국"): >> 일케 쓰자. 

값을 절대 바꾸지 않을 상수 변수는 대문자로 쓰자.

PI = 3.14

파이썬에서 이름은 언더바 형식으로 짓자. 낙타체 쓰지 마!!

