### 리스트
* 파이썬은 배열 대신 리스트를 쓴다.
```python
numbers = [1,2,3,5,7]
print(numbers)
print(numbers[0])
print(numbers[:3])

len(numbers)
numbers.append(6)
del numbers[4]  #4번 인덱스 삭제
numbers.insert(4, 37) #4번 인덱스에 37 삽입

numbers.sorted()
numbers.sorted(reverse = True)
new_list = sorted(numbers)
new_list = sorted(numbers, reverse=True)

# reverse 함수는 거꾸로 배치하기.
numbers.reverse()

print(37 in numbers)
print(37 not in numbers)


# 인덱스 값 리턴.
print(numbers.index(37))

numbers.remove(37)

# 리스트 두개 이어붙이기
a = [1,2,3]
b = [4,5,6]
c = a+b
```

### 사전
```python
dict = {
    1:1,
    2:4,
    3:9,
    4:16
}

print(dict)
print(dict[3])

# 값 추가.
dict[5] = 25

# value 전체 출력
print(dict.values())

# value 유무 확인
print(25 in dict.values())
for value in dict.values():
    print(Value)
for key in dict.keys():
    print(key)
for key, value in dict.items():
    print(key, value)
```

### aliasing
일종의 포인터... 
```python
x = [1,2,3]
y1 = x # y1는 x의 aliasing
y2 = list(x) # y2는 x의 aliasing이 아님. 새 객체임!!
```

### 문자열, 리스트.
* 문자열도 리스트처럼 slicing하면 된다. 
* 리스트는 mutable하지만 문자열은 immutable이다. 


### 모듈
```python
# calculator.py 임포트
import calculator
calculator.add(2,3)

# calculator.py 임포트
import calculator as calc
calc.add(2,3)

# 함수 골라서  임포트
from calculator import add, multiply
add(2,3)
multiply(2,3)
```

### math 모듈
```python
import math

print(math.log10(100)) # 2출력
print(math.cos(0)) # 1출력
print(math.pi) # 3.14.. 출력
```

### random 모듈
```python
import random

print(random.random()) #0~1 사이 소수 출력
print(random.randint(1,20)) #1~20사이 정수
print(random.uniform(0,5)) # 0~5 사이 소수
```

### input 넣기
```python
name = input("이름을 입력하세요: ")
print(name)

x = int(input("숫자 입력:"))
print(x+5)
```


### 파일 읽기
```python
with open('chicken.txt', 'r') as f:
    for line in f:
        print(line.strip())

my_string = "1. 2. 3. 4. 5"
print(my_string.split(". "))

# 공백 싹다 제거
my_string = "\n\n\n\n 2      \t 3 \n 5 7 \n\n".split()
```

### 파일 쓰기
```python
# 파일 덮어쓰기
with open('chicken.txt', 'w') as f:
    f.write("hello\n")

# 파일 이어서 쓰기
with open('chicken.txt', 'a') as f:
    f.write("hello\n")
```