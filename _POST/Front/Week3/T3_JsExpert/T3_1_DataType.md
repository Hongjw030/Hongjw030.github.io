# 🥑 자료형 🥑
#### Week3 JS 기초 / Topic 3 JS 핵심 / 1. DataType

>목차 
>>[1. 숫자형](#1-숫자형)<br>
[2. 문자열](#2-문자열)<br>
[3. 불 대수와 불린형](#3-불-대수와-불린형)<br>
[4. typeof 연산자](#4-typeof-연산자)<br>
[5. 연산자 우선순위](#5-연산자-우선순위)<br>
[6. 형 변환](#6-형-변환)<br>
[7. 템플릿 문자열](#7-템플릿-문자열)<br>
[8. null과 undefined](#8-null과-undefined)<br>

<br><br>

## 1. 숫자형
숫자형을 계산해보자. 파이썬이랑 비슷한 느낌이다. **신기한 건 정수, 실수형으로 나뉘지 않고 2나 2.0이나 둘 다 number 형이라고 나오는 것이다!!**
```js
// 거듭제곱.
console.log(2**3);

// 나머지 연산.
console.log(7%3);

// 나눗셈. 소수형으로 출력된다.
console.log(5/2);
```
<br>

## 2. 문자열
따옴표, 쌍따옴표 안에 들어있는 문자들의 나열. 
```js
console.log("코드잇");
```
신기하게도 쌍따옴표 내부에선 \ 없이도 따옴표 하나는 그냥 문자로 포함된다.
```js
console.log("I'm Iron man");
```
그치만 여러 개의 따옴표와 쌍따옴표가 있으면 역시 \를 써야 하니, 그냥 \를 쓰는 걸 습관으로 들이자.
```js
console.log("I\'m Iron man");
```
신기한 거 하나 더!! js에서는 백틱 표시도 문자열로 취급한다.
```js
console.log(`I'm'''' Iron man`);
// 이 백틱 ` 표시로 감싸면 역슬래시 없이 따옴표 남발도 가능!
```

문자열간의 덧셈도 가능하다.
```js
console.log("hello " + "Mr.H!");
```

참고로 작은 따옴표든 큰 따옴표든 내용이 같다면 같은 문자열이다.
```js
console.log("hello" === 'hello');
```

<br>

## 3. 불 대수와 불린형
일상적인 논리를 수학적으로 표현한 것을 불 대수라고 한다. 
* 불 대수의 값: true, false
* 불 대수 연산: AND, OR, NOT

명제란, 참과 거짓이 확실한 문장으로 참인 명제와 거짓인 명제가 있다.

그렇다면 불린형은 뭘까?

**js에서 참과 거짓을 표현할 때 나타내는 자료형** 이다!! true, false 두 가지 값만 있다. 

```js
// js는 참거짓 등호로 === 이렇게 3개를 쓴다.
console.log(3 ===3 );

// 거짓 등호로는 !== 을 쓴다.
console.log(3 !== 3);

// 다른 연산들은 파이썬과 같다.
console.log(2 > 1);
console.log(2 >= 1);

// And 연산은 &&
console.log(true && false);

// OR 연산은 ||
console.log(true || false);

// NOT 연산은 ! 그리고 중첩해서 쓸 수도 있다.
console.log(!false);
console.log(!!false);
//not not false니까 결국은 false.
```

등호 중 == 와 === 둘 다 쓸 수 있는데, 
* == 는 값만 비교하고
* === 는 데이터 타입까지 비교한다.
```js
// 아래 문장 모두 참.
console.log(5 == '5');
console.log(5 === 5);
```

<br>

## 4. typeof 연산자
이 데이터가 무슨 자료형인지 알게 해주는 연산자이다.
```js
// number
console.log(typeof 1);
console.log(typeof 3.14);

// string
console.log(typeof "1");
console.log(typeof `1`);

// function
function hello(){
    console.log('hello');
};
console.log(typeof hello);

// NaN not a number!! 에러.
// typeof 가 - 보다 먼저 연산이 되어 에러가 난다. 
console.log(typeof 8 - 3);
```

<br>

## 5. 연산자 우선순위
연산자들이 여러 개 있고, 각 우선순위가 조금씩 다르니 헷갈리면 괄호로 묶어서 처리하자.


## 6. 형 변환
Type Conversion 이라고도 한다. 

Number, String, Boolean 함수를 쓰면 된다.

```js
conlone.log(Number('10') + Number('5'));
conlone.log(String(10) + String(5));
```
그런데 "hello" 같이 숫자로 바꿀 수 없는 문자열을 숫자로 바꾸려면 NaN 이라고 출력된다. ***근데 typeof 로 형을 체크하면 숫자형으로 바뀌긴 했다!!**

```js
//  NaN 출력된다.
conlone.log(Number("hello"));
// Number 출력된다. 
conlone.log(typeof Number("hello"));
```
그리고 불린도 숫자로 바꿀 수 있다.
```js
//  1 출력
console.log(Number(true));
// 0 출력된다. 
console.log(Number(false));
```
문자나 숫자를 불린으로 바꿀 수도 있다.
```js
// 0이 아닌 숫자는 true로 출력
console.log(Boolean(154));
// 문자가 있는 문자열은 true로 출력
console.log(Boolean('hello'));

// 숫자 0과 NaN,  '' 문자열은 false
// 0이 아닌 숫자는 true로 출력
console.log(Boolean(0));
console.log(Boolean(NaN));
console.log(Boolean(''));
```
* 참고로 이렇게 불린으로 형변환했을 때 false가 나오는 0, NaN, '' 값을 falsy 값이라고도 부른다. 

<br>

Js에선 자동으로 형변환을 하기도 해준다. 
```js
// 일반적으로 산술연산자는 데이터를 자동으로 숫자로 형변환해준다. 단, 덧셈은 문자열 연결 기능도 있으니 주의하자!!

// 이 두개는 잘 출력됨.
console.log(4 + '2');
console.log(4 + true);
// 얘는 NaN 출력.
console.log(4 % 'two');

// 비교할 수 없는 형에서도 false 출력함.
console.log('two' >= 1);
```

앞에서 배웠듯 ==는 동등, 부등 을 따지기 때문에 자동 형 변환이 일어나고,

===는 일치, 불일치를 따지기 때문에 자동 형변환이 일어나지 않는다. 
```js
// false
console.log(1 === '1');
// true
console.log(1 == true);
```

<br>


## 7. 템플릿 문자열
특별한 형식을 가진 문자열을 템플릿 문자열이라 한다.

단, 백틱으로 문자열을 묶어줘야 함!!

```js
console.log(`${age}살 ${height}cm ${weight}kg 입니다.`);
```


## 8. null과 undefined
자료형에는 숫자형, 문자형, 불형 뿐만 아니라 null 형, undefined 형이 있다.

* null : 의도적으로 표현할 때 사용하는 값. 값을 안 넣을 때 null로 선언한다.

* undefined : 값이 없다는 것을 확인하는 값. 기본적으로 선언된 변수는 딱히 값을 넣어주지 않으면 undefined 값을 가진다. 즉, 지정된 값이 없다는 것을 확인할 수 있다!!
```js
// 얘는 참인데
console.log(null == undefined);

// 얘는 또 거짓으로 나옴. 
console.log(null === undefined);
```
즉 변수 선언해서 의도적으로 let value = undefined; 하고 값을 넣어줄 수는 있지만, 그렇게 쓰면 의미가 퇴색되므로 null을 써주자. 

* NaN : 숫자가 아닌데 숫자형으로 나옴.