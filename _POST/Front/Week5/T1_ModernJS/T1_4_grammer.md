# 🌽 js 문법 🌽

#### Week5 모던 자바스크립트 / Topic 1 모던 자바스크립트 / 4. js 문법

> 목차
>
> >

1. 문장과 표현식
2. 조건을 다루는 표현식
3. spread 구문
4. 모던한 프로퍼티 표기법
5. 옵셔널 체이닝
6. 구조 분해
7. 함수와 구조 분해
8. 에러와 에러 객체
9. try catch
10. finally

<br><br>

## 1. 문장과 표현식

- 문장: statements. 어떤 동작이 일어나도록 작성된 최소한의 코드 덩어리.

```js
let x; // 문장 1
x = 3; // 문장 2
```

- 표현식: expression. 결과적으로 하나의 값이 되는 모든 ㅗ드.

```js
const title = "JavaScript"; // 표현식 1
const codeit = {
  name: "Codeit",
}; // 표현식 2.
```

문장은 표현식인 문장과 표현식이 아닌 문장으로 나뉘는데, 변수에 문장이 할당되면 표현식이다.

```js
// 변수에 할당하려면 에러가 나므로 표현식이 아니다.
const someloop = for (let i = 0; i < 5; i++) {console.log(i);};
```

간단하게 생각하면 표현식 문장은 세미콜론, 표현식 아닌 문장은 블록으로 나뉜다고 생각할 수도 있다!!

<br>

## 2. 조건을 다루는 표현식

2015년 이전에는 if, switch 문 두개 뿐이다.

그러나 2015년 이후 블록으로 굳이 묵지 말고 조건 연산자로 조건을 다룰 수도 있게 되었다!! 이 조건연산자는 삼항 연산자로도 불린다.

**조건 ? truthy 표현식 : falsy 표현식**

```js
const LEAST = 80;
function pass(score) {
  return score > LEAST ? "합격" : "불합격";
}
```

단, 조건 연산자는 표현식이기 때문에 if문을 완전히 대체할 수는 없다. 내부에 변수를 선언하거나 내부에 반복문을 실행하는 것은 불가능.

<br>

## 3. spread 구문

spread는 2015년 이후 등장한 신 문법으로, 배열을 다룰 때에 유용하다.

spread는 하나의 배열을 다시 각각의 값으로 펼치는 문법이다.

```js
const nums = [1, 2, 3];
// [1,2,3] 출력
console.log(nums);
// 1 2 3 따로 출력
console.log(...nums);
```

1. 이것을 활용해서 새 배열을 만들 수 있다.

```js
const num = [1, 2, 3, 4];
// 메소드를 활용해 복사하기
const num1 = num.splice();
// spread를 이용해 복사하기
const num2 = [...num];

// 복사하는 동시에 값을 추가할 수도 있다.
const num3 = [...num, 5];

// 두 배열을 합친 새로운 배열을 만들 수도 있다.
const num4 = [...num1, ...num2];

// 배열 모든 값에 for 문 안쓰고 함수 적용하기.
printHi(...name);
```

2. 객체를 만들 수도 있다.

```js
// 자동으로 인덱스가 프로퍼티 네임이 된다.
const name = ["a","b","c"];
const newObject = (...name);

// {0:"a", 1:"b", 2:"c"} 출력.
```

**주의할 점!! spread 자체는 값이 아니라 값들 목록이다.**

```js
const nums = [1]
const num = ...nums; // 에러 발생!!!
```

또한 객체에 적용한 spread 구문을 함수 인자로 전달할 수는 없고, 객체에 spread를 적용해 새 배열을 만들 수도 없다.

```js
const hongjw = {
    first : "hong";
    second: "jw";
}
const user = {
    ...hongjw, // 이건 가능.
    id: "hellen";
}
[...hongjw] //에러 발생
greetings(...hongjw); // 이것도 에러

const nums = [1,2,3];
greetings(...nums) // 이건 가능. 객체 아니고 배열에 적용된 spread라서.
```

<br>

## 4. 모던한 프로퍼티 표기법

<br>

## 5. 옵셔널 체이닝

<br>

## 6. 구조 분해

<br>

## 7. 함수와 구조 분해

<br>

## 8. 에러와 에러 객체

<br>

## 9. try catch

<br>

## 10. finally

<br>
