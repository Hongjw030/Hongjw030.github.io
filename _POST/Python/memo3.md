### 요약
클래스 만들기, 인스턴스 메소드, 던더 메소드, 클래스 변수, 데코레이터, 클래스 메소드, 정적 메소드, 모듈

### 객체

클래스를 통해 객체들을 만들 수 있다.

객체와 인스턴스는 다른 개념이지만 비슷하니 섞어 쓰기도 한다.

**파이썬은 순수 객체 지향 언어임**. 즉, 파이썬의 모든 것은 객체이다!! 

즉, 우리가 
* print(type(2)) 
* print(type(()))
* print(type([]))

이렇게 숫자나 문자열, 튜플 등 을 넣어보면 class의 객체라고 출력된다. 이렇게 우리가 정의하지 않은 클래스의 객체들은 파이썬 개발자들이 미리 만들어 둔 것이다!!

list.append(3) 이런 함수들도 파이썬 개발자들이 미리 만들어둔 클래스의 메소드들이다. 

### 파이썬의 객체는 2가지 종류가 있다.

각 종류의 특징이 다르기 때문에, 타입을 잘 아는 것이 중요하다. 

1. 가변 타입 객체

한 번 생성한 인스턴스의 속성은 변경 수정 가능함. 예를 들면 리스트, dict, 그리고 우리가 직접 만든 클래스는 모두 가변 타입이다!


2. 불변 타입 객체

한 번 생성한 인스턴스의 속성은 수정 불가능!! 예를 들면 튜플, string. int, float, bool

이런 객체는 값 수정은 불가능하지만 재할당은 가능함. 즉, 아예 새로운 인스턴스를 생성해서 그 인스턴스를 가리키게 해야 한다!! 


```python
# 클래스 이름 첫글자는 대문자로.
class User:
    # 쓸 내용이 없으면 pass라 적기
    pass

user1 = User()
user2 = User()

# 아래를 인스턴스 변수라고 한다.
# 인스턴스 이름.인스턴스변수이름 = 인스턴스변수값
user1.name="hellen"
user1.age=26
user1.id="hongjw"
```
메소드 3가지 종류
1. 인스턴스 메소드: 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 할당하는 함수.
2. 클래스 메소드
3. 정적 메소드

```python
class User:
    # 함수 인자에 self 말고 다른 이름 붙여도 되지만, 첫 인자에는 인스턴스 자기 자신이 자동으로 들어가기 때문에 self라고 이름 짓는 것이 암묵적인 룰이다!
    def say_hello(self):
        print("hello {}".format(self.name))
    def login(self, id, password):
        print("{} : {}".format(self.id, self.password))

user1 = User()
user1.name = "hellen"
# 클래스에서 메소드 호출
User.say_hello(user1)
# 인스턴스에서 메소드 호출. 인스턴스 메소드에선 인스턴스가 함수의 파라미터로 자동으로 전달됨. 
user1.say_hello()
user1.say_hello("id", "password")
```

#### 특수 메소드

특수 메소드도 일종의 인스턴스 메소드다.

클래스 메소드 중에 언더바 두개씩 양 옆으로 붙어있는 메소드를 매직 메소드(=특수메소드=스페셜메소드=던더메소드) 라 부른다.

특수 메소드는 특정 상황에서 자동으로 호출되는 메소드이다. 

1. ```__init__ 메소드```
```python
# __init__ 메소드는 인스턴스 생성 시 자동으로 호출되는 메소드이다.
# 클래스 만들 때 init 메소드를 쓰는 걸 권장!!
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

user1 = User('hellen', 'aaaa.namver.com', 1234)
```

2. ```__str__메소드```
```python
# 그냥 인스턴스를 출력하면 인스턴스 타입과 메모리 위치만 출력됨.
class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id

user1 = User('hellen', 'hellen35')
print(user1)

# __str__ 메소드는 print 함수가 호출될 때 자동으로 호출된다. 
class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def __str__(self):
        return ("{} {}".format(self.name, self.id))
        # 문자열을 리턴한다!!!

user1 = User('hellen', 'hellen35')
print(user1)
```


### 클래스 변수
클래스 변수란 여러 인스턴스들이 공유하는 하나의 값. 클래스 변수는 인스턴스를 통해 값을 읽을 수 있지만 값을 아예 새로 설정할 때엔 꼭 클래스 이름으로 호출해야 한다.

```python
class User:
    count = 0
    def __init__(self, name, id):
        self.name = name
        self.id = id
        count += 1

user1 = User("a", "a")
user2 = User("b", "b")
print(User.count) # 2가 출력된다!
```
클래스 변수에 값이 들어있으면, 인스턴스에 딱히 값을 안 정해줘도 그 값이 자동으로 다 들어가진다.
```python
# 아래 모두 2로 출력됨.
print(User.count)
print(user1.count)
print(user2.count)

# 클래스 변수가 바뀌는 게 아니라, user1 객체의 속성에 count라는 속성이 생기면서 그냥 클래스변수 count와 이름만 같은 count 인스턴스 변수가 생겨버린 것임!! 
user1.count = 5
print(User.count) # 2
print(user1.count) # 5
print(user2.count) # 2

# 클래스 메소드로 클래스 변수를 바꾸면 잘 적용됨
# 근데 같은 이름의 클래스변수와 인스턴스 변수가 있으면 인스턴스 변수를 우선으로 읽어서, user1.count=5 코드를 없애기 전까진 계속 user1.count는 5를 출력함. 
User.count = 6
print(User.count) # 6
print(user1.count) # 5
print(user2.count) # 6
```


### 데코레이터
기존의 함수를 꾸며서 새로운 함수를 만드는 것.

함수가 여러 개 있을 때, 중복되는 부분을 데코레이터 함수로 만들면 좋다! 

* 새 함수에 기존 함수를 파라미터로 넘겨준다
* 새 함수 내부에 wrapper 함수를 만들어 인자로 받은 기존 함수와 부가 코드를 묶어 리턴해준다. 

```python
def print_hello():
    print("hello!")

# add_print_to 함수는 인자로 받은 함수를 데코레이팅해주는 역할. 이런 함수를 데코레이터 함수라고 한다!!
def add_print_to(original):
    def wrapper():
        print('start')
        original()
        print('end')
    return wrapper

# 파라미터로 넘겨주는 함수는 함수 명만 적고 괄호 안 적는다!
add_print_to(print_hello)()

# 아예 print_hello 함수 재정의하기
print_hello = add_print_to(print_hello)
print_hello()
```

위에처럼 쓰는 건 이제 전통적인 방식!!

코드를 깔끔하게 쓰려면 아래처럼 쓰자.

```python
def add_print_to(original):
    def wrapper():
        print('start')
        original()
        print('end')
    return wrapper

# 골뱅이를 붙이면 이 print_hello 함수를 데코레이터 함수로 꾸며주라는 뜻이다. 
@add_print_to
def print_hello():
    print("hello!")

# 함수 재정의할 필요 없이 바로 꾸며진 함수 출력됨.
print_hello()
```


### 클래스 메소드 
인스턴스 메소드는 앞에서 배운 던더 메소드나 일반 메소드처럼 인스턴스 변수의 값을 읽거나 설정하는 메소드임.

**반면 클래스 메소드는 클래스 변수의 값을 읽거나 설정하는 메소드!!**

* 인스턴스 메소드는 첫 파라미터를 자동으로 자기 자신 객체를 받기 때문에 self라는 이름의 인자를 넣어줬었다.

* 클래스 메소드는 첫 파라미터를 자동으로 자기 자신 클래스를 받기 때문에 cls라는 이름의 인자를 넣자!! 물론 이름은 아무거나 써도 되지만, self와 cls은 그냥 암묵적인 룰이니까 지켜두자.

```python
class User:
    count = 0
    def __init__(self, name, id):
        self.name = name
        self.id = id
        User.count += 1

# 클래스 메소드 호출 시 인스턴스로 호출한다해도 자동으로 cls 인자에 클래스가 들어간다.
# 클래스 메소드는 메소드 위에 @classmethod 를 붙여야 한다.
@classmethod
def number_of_users(cls):
    print(cls.count)

user1 = User('a', 'a')
User.number_of_users()
user1.number_of_users()
```

주의할 점!!! 인스턴스 메소드와 클래스 메소드
```python
# 인스턴스 메소드 호출하려면 인스턴스를 넣어야 함.
User.say_hello(user1)
user1.say_hello()

# 클래스 메소드 호출하면 뭘로 호출해도 자동으로 클래스가 넣어짐. 단, classmethod 데코레이터 함수를 붙여준 경우에만!!!!
User.number_of_users()
user1.number_of_users()
```

인스턴스 변수를 사용하지 않는 메소드는 꼭 클래스 메소드로 만들자. 

1. 만약 인스턴스 변수, 클래스 변수 둘 다 쓴다면 인스턴스 메소드로 만들자!!

인스턴스 메소드는 self를 통해 인스턴스 변수를 가져오고, 클래스 이름으로 클래스 변수를 불러올 수 있기 때문이다. 

그러나 클래스 메소드는 인스턴스 변수 사용 불가. (사용 하려면 인자를 따로 받아야 하는데 그럼 클래스 메소드의 의미가 퇴색됨!!)

2. 인스턴스 없이도 그냥 초기 정보가 있다면? (ex. user 객체가 없어도 count 는 0 값으로 계속 존재향 함...)

이 경우에도 클래스 메소드로 만들자. 


### 정적 메소드
인스턴스 변수, 클래스 변수 둘 다 아예 안 다루는 메소드. 

즉 함수의 인자에 cls, self 둘 다 안 들어간다!!

**클래스메소드, 인스턴스메소드도 없고 속성도 하나도 없이 정적 메소드만 있는 클래스도 있다! 그냥 함수만 모아둔 클래스**

* 클래스 메소드는 @classmethod
* 정적 메소드는 @staticmethod 데코레이터 붙이기.
```python
class User:
    count = 0
    
    def __init__(self, name, email, pw):
        self.name = name
        self.email = email
        self.pw = pw
    
        User.count += 1
    
    def say_hello(self):
        print("안녕하세요! 저는 {}입니다!".format(self.name))
    
    def __str__(self):
        return "사용자: {}, 이메일: {}, 비밀번호: ******".format(self.name, self.email)
    
    @classmethod
    def number_of_users(cls):
        print("총 유저 수는: {}입니다".format(cls.count))
    
    @staticmethod
    def is_valid_email(email_address):
        return "@" in email_address
```



### 모듈
모듈은 변수, 함수, 클래스 등을 모아둔 파일로 import 해서 쓰면 된다. 

```python
# calculator.py 임포트하기

import calculator 
calculator.add(1,2)

import calculator as cacl
calc.add(1,2)

from calculator import add
add(1,2)
```