# 🍓 js 동작 원리 🍓

#### Week5 모던 자바스크립트 / Topic 1 모던 자바스크립트 / 1. 동작 원리

> 목차
>
> > [1. 데이터 타입](#1-데이터-타입)<br> > > [2. typeof 연산자](#2-typeof-연산자)<br> > > [3. 불린](#3-불린)<br> > > [4. ANd OR 연산](#4-and-or-연산)<br> > > [5. null 병합 연산자](#5-null-병합-연산자)<br> > > [6. 변수와 스코프](#6-변수와-스코프)<br>

<br><br>

## 1. 데이터 타입

- js는 다른 언어에 비해 데이터 타입이 유연하다. 이 때 유연하다는 것은, **상황에 따라 데이터 타입이 바뀔 수도 있다는 것이다.**

JS의 데이터 타입

1. 기본형: Number, String, Boolean,, Null, Undefined 와 더불어 새로 2020년에 추가된 Symbol, BigInt 타입.
2. 참조형: Object

### symbol 타입

심볼은 코드 내에서 유일한 값을 가진 변수 이름을 만들 때에 사용한다. 이렇게 만들어진 변수는 어떤 값과 비교하든 무조건 false가 되는 고유 변수가 된다.

```js
const user1 = Symbol("this is a user");
const user2 = Symbol("this is a user");

console.log(user1 === user2);
console.log(user1 === "this is a user");
```

### BigInt 타입

아주 큰 정수를 표현하기 위해 사용한다.

- 소수 표현 사용 불가.
- 정수를 더 안전하게 표현 가능
- int와 BigInt 간의 계산 불가.
- 숫자 뒤에 n을 붙이거나 BigInt 함수를 써서 나타낸다.

```js
console.log(124134532453453n);
console.log(BigInt(14232425434663));

// 에러 남!
3n + 2;
// 정상
Numer(3n) + 2;
```

<br>

## 2. typeof 연산자

- 함수에 typeof 를 쓰면 object가 아니라 function을 리턴한다.
- null의 타입은 null이 아니라 object이다.

```js
typeof "Codeit";
```

<br>

## 3. 불린

if 나 while 같은 조건문 안에 boolean을 넣지 않고 다른 걸 넣어도 컴퓨터가 자동 형변환하여 처리할 수 있다.

```js
// 예시
if ("yes") {
  console.log("yes");
}
```

이렇게 불린형이 아니지만 false로 자동 형변환되는 값을 falsy 값이라 한다.

falsy 값: false, null, undefined, NaN, 0 ''
truthy 값: falsy 아닌 그 외 모든 것.

**참고로 빈 배열이나 빈 객체 [] {} 도 truthy 값이다!!!**

<br>

## 4. ANd OR 연산

js에서 AND 연산은 특이한 방식으로 진행된다.

```js
// && 연산자는 왼쪽이 false인 경우 왼쪽 값을 그대로 리턴하고 왼쪽이 true라면 오른쪽 값을 그대로 리턴한다.
console.log(true && false);
console.log(false && true);

// 왼쪽이 true니까 오른쪽 javascript 출력!!
console.log("codeit" && "javascript");
```

or 연산에서도 마찬가지이다.

```js
// || 연산자는 왼쪽이 false인 경우 오른쪽 값을 그대로 리턴하고 왼쪽이 true라면 왼쪽 값을 바로 리턴한다.
console.log(true || false);
console.log(false || true);

// 왼쪽이 true니까 왼쪽 codeit 출력!!
console.log("codeit" && "javascript");
```

예제

```js
console.log(nul && undefined);
console.log(0 || true);
console.log("0" && NaN);
console.log({} || 123);
```

위의 답은 각각 undefined, true, NaN, {} 이다.

**이를 활용해서 조건식처럼 활용하는 것.**

```js
function print(value) {
  const message = value || "codeit";
  console.log(message);
}
// value에 아무 값도 주지 않으면 codeit이 출력된다.
print();
print("javascript");
```

참고로 AND 연산자가 OR 연산자보다 우선순위가 높다! 불린 연산자를 여러 번 쓸 경우 계산이 어그러질 수 있으니 괄호로 꼭 우선순위를 묶어주자.

<br>

## 5. null 병합 연산자

ES2020에 새로 추가된 null 병합 연산자. nullish coalescing operator 이라고 불린다!!

null 병합 연산자는 물음표 두개 ?? 를 사용해 null 혹은 undefined 값을 가려낸다.

```js
// ?? 연산자 왼쪽이 null 혹은 undefined라면 오른쪽 값이 리턴되고 그렇지 않다면 연산자 왼쪽 값이 리턴된다.
const ex1 = null ?? "a";
const ex2 = undefined ?? "love";
const ex3 = "codeit" ?? "javascript";
// 위의 코드에선 a love codeit 출력됨.
```

or 연산자와 null 연산자의 동작 순서는 비슷해보이지만 null 연산자는 왼편 값이 null이나 undefined 인지를 확인하기 때문에, null undefined가 아닌 falsy 값을 활용하려면 or 연산자를 쓰자!!

```js
const width1 = 0 || 150;
const width2 = 0 ?? 150;

console.log(width1); // 150
console.log(width2); // 0
```

<br>

## 6. 변수와 스코프

변수는 let과 const를 사용해 선언한다.

**원래는 var을 사용했는데, 왜 요즘에는 안 쓰는 것일까?**

1. 변수가 유효한 시점의 차이. var은 변수 선언 이전에도 변수를 사용 가능한 호이스팅 문제가 발생.
2. 중복 선언. var은 중복 선언이 가능함.
3. 변수 범위. var은 함수 단위로만 지역 변수가 선언되므로 중괄호 안에(코드 블록) 변수를 만들어도 전역변수처럼 쓰인다.

   <br>
