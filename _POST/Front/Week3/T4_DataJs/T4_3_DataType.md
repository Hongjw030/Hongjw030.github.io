# 🍙 DataType 🍙

#### Week3 JS 기초 / Topic 4 JS와 Data / 3. 자료형

> 목차
>
> >

1. 숫자 표기법
2. 숫자형 메소드
3. Math 객체
4. 바보 자바스크립트
5. 문자열 심화
6. 기본형과 참조형
7. 참조형 복사하기
8. const, 변수, 상수
9. const와 참조형
10. 변수

<br><br>

## 1. 숫자 표기법

10억을 표현하려면?

```js
// 1 뒤에 0이 9개 붙는다.
let milli = 1e9;
```

16진법을 쓰려면?

```js
// 0x 붙이기
let hex1 = 0xff;
let hex2 = 0xff;
```

8진법은?

```js
// 0o 붙이기
let octal = 0o377;
```

2진법은?

```js
// 0b 붙이기
let binary = 0b1101;
```

## 2. 숫자형 메소드

Number 도 일종의 객체이기에, 메소드가 있다.

1. **toFixed()** 는 소수점을 n번째 자리까지 살리고 반올림하는 것. 주의할 건 **number.toFixed() 해서 나온 값은 string이라 덧셈연산할 경우엔 형변환을 해야 한다!!**

```js
//0.1592에서 0.159가 된다.
console.log(myNumber.toFixed(3));
```

하나 그냥 팁!! string을 number로 바꿀 때 number 함수를 써도 되지만 그냥 + 기호만 붙여도 형변환 됨.

```js
// 341이 문자열 말고 숫자로 출력된다.
console.log(+"341");
```

2. **toString()** 은 n진수로 수를 바꿔준다.

```js
// ff 출력됨.
let number = 255;
console.log(number.toString(16));

// 아예 숫자에 toString 적용하려면 숫자에 괄호 치거나 .을 두 개 써서 할 수도 있다!!
console.log((255).toString(16));
console.log((255).toString(16));
```

<br>

## 3. Math 객체

연산에 도움 되는 객체이다.

1. 절댓값 리턴하기.

```js
console.log(Math.abs(-10));
```

2. 최댓값 최솟값 리턴하기.

```js
console.log(Math.max(2, -1, 4, 5, 0));
console.log(Math.min(2, -1, 4, 5, 0));
```

3. 거듭제곱 리턴하기

```js
console.log(Math.pow(2, 3));
```

4. 제곱근 리턴하기

```js
console.log(Math.sqrt(25));
```

5. 반올림 리턴하기

```js
// toFixed는 string 반환, round는 number 반환.
console.log(Math.round(2.462));
```

6. 버림과 올림 리턴하기

```js
// 버림
console.log(Math.floor(2.5));
// 올림
console.log(Math.ceil(2.5));
```

7. 난수 리턴하기 (랜덤)

```js
// 0~1 사이 값이 랜덤 리턴.
console.log(Math.random());
```

<br>

## 4. 문자열 심화

number처럼 string도 객체이다. 특히 배열과 비슷함. 그렇제만 typeof로 비교하면 string과 object 구분되어 분류된다.

### 배열과 비슷한 점.

```js
// 1. 문자열 길이 리턴할 때 length 쓴다.
console.log(str.length);

// 2. 요소 찾을 때 대괄호 표기법이나 메소드.
console.log(str[3]);
console.log(str.charAt(3));

// 3. 요소 위치 찾을 때 indexOf 사용.
console.log(str.indexOf("i"));
console.log(str.lastIndexOf("i"));
// 신기한 점. indexOf로 문자열도 찾을 수 있다. 이 경우 a의 인덱스를 리턴함.
console.log(str.indexOf("abc"));
```

### 문자열만의 함수

1. 대문자화 소문자화.

```js
console.log(str.toUpperCase());
console.log(str.toUpperCase());
```

2. 문자열 맨 양 끝의 공백을 삭제. (가운데 공백은 살림.)

```js
console.log(str.trim());
```

3. 부분 문자열 가져오기

```js
// 문자열 0, 1번 가져옴.
console.log(str.slice(0, 2));
// 문자열 1번부터 끝까지 가져옴
console.log(str.slice(1));
// 문자열 모두 가져옴.
console.log(str.slice());
```

**주의하자!! 배열과 문자열은 엄연히 다르다**

```js
// 모두 false로 출력됨.
let myString = "Codeit";
let myArray = ["C", "o", "d", "e", "i", "t"];

console.log(myString === myArray);
console.log(myString == myArray);
```

왜냐면 배열은 원소를 바꿀 수 있는 mutable, 문자열은 바꿀 수 없는 immutable 자료형이기 때문이다.

**따라서 문자열에는 splice 같은 메소드는 사용할 수 없다!!**

<br>

## 5. 기본형과 참조형

- 기본형: Number, string, undefined, null, boolean
- 참조형: object 배열

참조형이란 변수에 값 그자체가 아니라 값을 가리키는 주소의 값을 담는 자료형.

```js
let x ={...};
let y = x;
```

위의 코드에서 x는 참조형 변수기 때문에 object를 가리키는 주소값을 담고 있다 >> 즉, y에게도 object를 가리키는 주소가 할당되므로 x에서 프로퍼티를 수정하면 y에도 반영된다.

#### 그렇다면 참조형 변수를 주소가 아니라 값만 복사하려면 어떻게 해야 할까?

```js
// 배열 복사하기
let number11 = [1, 2, 3];
let number2 = number1.slice();
```

```js
// 객체 복사하기
// 이렇게 Object의 메소드를 사용하면 된다.
let obj1 = { ... };
let obj2 = Object.assign({}, obj1);

// for in 문을 사용해서 객체를 복사할 수도 있다.
// 이 코드로 객체를 복사하는 함수를 직접 만들 수도 있다.
let obj3 = {}
for (let key in obj1){
    obj3[key] = obj1[key];
}
```

**객체 안의 객체, 객체 안의 배열이 포함된 경우** 객체 복사하기로 for 문을 사용하면 또다시 내부의 주소값이 복사되면서 원점으로 될 수 있다. 참조형 안의 참조형 변수가 있을 때엔 주의해서 사용하자.

<br>

## 6. const, 변수, 상수

let 말고 const로 변수를 선언하라고 권장하기도 한다.

1. 변수가 자꾸 재할당될 수록 코드가 불안정해짐.
2. 코드를 안전하게, 일관되게 짜는 데엔 const가 더욱 좋다.

우리가 회원가입 폼에서도 아이디나 비밀번호를 입력하고 제출 버튼을 누르면, 해당 값들은 절대 바뀌지 않는 상수로서 웹사이트에서 동작하기 때문에 const로 값을 받아 쓰는 것이 더욱 안정적!

따라서 변수를 선언할 때에도 const를 쓰되, 네이밍은 변수 이름 그대로 쓰자. (소문자, 카멜체)

진짜 상수는 const로 선언하면서 대문자, 언더바를 사용해 네이밍을 하자.

**단, 객체나 배열 같이 참조형 변수를 const로 선언해도 프로퍼티의 값을 수정할 수 있다.**

참조형 변수는 객체 값이 아니라 주소를 가리키고 있기 때문에, 내부 프로퍼티는 수정할 수 있다.

#### 옛날에는 var 키워드를 썼었다!!

var도 let과 같이 변수를 선언할 때 썼지만, 다음과 같은 문제점으로 이젠 거의 쓰지 않는다.

1. 중복 선언 허용

   - var 키워드로 똑같은 이름의 변수를 한 번 더 선언하면 에러가 나지 않고 그냥 기존의 변수를 덮어써버린다. 이는 코드의 불안정성을 높임!

2. scope 문제

   - let, const는 중괄호에 따라 지역인지, 전역변수인지의 기준이 나뉘지만 var은 함수의 내부에 있는지, 바깥에 있는지에 따라 scope가 나뉜다. 때문에 if, for 문 등 여러 블록문에서 자칫하면 전역변수처럼 작동할 수 있다.

3. hoisting 문제
   - hoisting이란 변수가 끌어올려지는 현상이다. let으로 선언한 변수는 선언되기 이전엔 쓸 수 없지만 var 변수는 선언되기 전에도 접근 가능하다. 이는 코드의 흐름을 방해함!!
