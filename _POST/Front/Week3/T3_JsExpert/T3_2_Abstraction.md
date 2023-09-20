# 🧋 추상화 🧋
#### Week3 JS 기초 / Topic 3 JS 핵심 / 2. 추상화

>목차 
>>[1. 할당연산자](#1-할당연산자)<br>
[2. 함수 실행 순서](#2-함수-실행-순서)<br>
[3. return 문](#3-return-문)<br>
[4. 옵셔널 파라미터](#4-옵셔널-파라미터)<br>
[5. 변수의 범위](#5-변수의-범위)<br>
[6. 상수](#6-상수)<br>


<br><br>

## 1. 할당연산자
할당 연산자는 = 기호이다. assignment operator이라 부르며,

피연산자(오른쪽 연산되는 대상)를 왼쪽에 집어넣으라는 뜻이다. 
```js
let x = 32;
x = x + 2;
```

할당 연산자와 결합해서 연산자를 연달아 쓰는 것을 복합 할당 연산자, compound assignmnet operator 이라 한다.
```js
x += 1;
x *= 2;
x %= 3;
```
증가, 감소 연산자는 ++ 나 --를 쓰자.
```js
x++;
y--;
```
<br>

## 2. 함수 실행 순서
코드는 기본적으로 위에서 아래로 순서대로 실행된다. 


## 3. return 문
return은 함수에서 연산한 후 값을 output으로 내놓는 역할이자, 함수를 그대로 중단시키는 역할.

* return은 값을 돌려준다. 

* console.log 는 출력 함수이다.

return 문이 없는 함수를 출력하면 undefined 를 출력한다.

## 4. 옵셔널 파라미터
함수에게 파라미터로 값을 줄 수 있다.

* 만약 파라미터 인자를 줘야 하는 함수인데도 아무것도 안 주면, undefined 값을 출력한다.
```js
function hello(name){
    console.log(name);
}
// 정상 출력
hello('hellen');
// undefined 출력
hello(); 
```

파라미터 값에 디폴트 값을 정해주면, 우리가 굳이 인자를 주지 않고 파라미터 값을 생략하고 함수를 호출할 수 있다. 이를 **옵셔널 파라미터** 라고 한다!!
```js
function hello(name = 'hellen'){
    console.log(name);
}
// 정상 출력
hello('hellen');
// 정상 출력
hello();
```

단, 옵셔널 파라미터는 여러 개 써도 되지만 무조건 마지막에 써야 한다.
```js
// 오류!!!
function hello(age, name = 'hellen', height ){
    console.log(age);
    console.log(height);
    console.log(name);
}

// 이렇게 쓰자.
function hello(age, name = 'hellen', height = '160'){
    console.log(age);
    console.log(height);
    console.log(name);
}
```

### 진짜 주의할 거!!

옵셔널 파라미터를 여러 개 쓴다고 해도 함수 호출 시 특정 파라미터에만 값을 할당하는 식은 안된다. 이 점이 파이썬과는 다르다!!

```js
function hello(age, name = 'hellen', height = '160'){
    console.log(age);
    console.log(height);
    console.log(name);
}

// 아래처럼 호출하면 age에 24, name에 168 값이 들어간다. 
hello(24, 168);

// 아래처럼 호출해야 한다.
hello(24, undefined, 168);
```
<br>

## 5. 변수의 범위
각 변수에는 유효한 범위가 정해져있다. 
```js
function name(){
    // 이렇게 중괄호 안에 있는 코드들을
    // 블록문 block statement 라고 한다.
    let x = 3;
    // 블록문 내 변수를 local variable이라 한다.
};

let x = 3; 
// 위의 것은 글로벌, 전역 변수라고 한다.
```

정리하자면, **변수는 크게 지역변수와 전역변수로 나뉘며, 중괄호로 감싸진 블록문을 기준으로 이 둘을 나눈다.**

<br>


## 6. 상수
절대 변하지 않는 값을 담은 변수를 상수라 한다. 이런 변수는 let으로 선언해도 되지만 좀 더 의미를 정확하게 나타내기 위해 const 키워드를 쓰자.
```js
const PI = 3.14;

pi = 3.15; // 이렇게 재할당하려면 오류가 난다.

// 맨 처음 선언할 때에도
const pi;
// 이렇게 아무 값도 안 넣으면 오류가 난다. 
```

상수는 대문자와 언더바로만 이름을 쓰자.

만약 아직 값이 정해지지 않은 변수를 선언하려면, null을 넣는게 일반적이지만 변수의 자료형은 정해진 상태라면 0 이나 '' 를 쓰는 게 더 가시적으로 좋다.
```js
// rad의 값을 뭐로 정할진 아직 못 정했지만 일단 정수니까 0으로 놔둠.
let radius = 0;
```