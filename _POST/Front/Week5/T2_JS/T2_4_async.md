# 🍝 async와 await 활용하기 🍝

#### Week5 모던 자바스크립트 / Topic 2 JS와 웹 / 4. async와 await 활용하기

> 목차
>
> > 1. async와 await
> > 2. 동기 실행 코드처럼 생긴 비동기 실행 코드
> > 3. catch, finally 문
> > 4. async 함수의 리턴값
> > 5. async 함수 내의 async
> > 6. async 함수 작성할 때 주의할 것.
> > 7. 두 가지 종류의 콜백.

<br><br>

## 1. async와 await

async와 await를 쓰면 우리가 앞에서 쓴 fetch then 문보다 더 간단하게 쓸 수 있다.

1. 우리가 이때껏 배운 코드

```js
fetch("url")
    .then((response)=>response.text());
    .then((result)=>{console.log(result);});
```

2. 위의 코드를 async await로 바꾸기

```js
async function fetchAndPrint() {
  const response = await fetch("url");
  const result = await response.text();
  console.log(result);
}
fetchAndPrint();
```

먼저 함수 안에 비동기적으로 실행될 부분이 있다면 function 키워드 앞에 async 키워드를 붙인다.

그다음 함수 내부에서 비동기적으로 실행되는 코드 앞에 await 키워드를 붙인다.

단, async 키워드가 없는 그냥 함수 안에 await 키워드를 쓸 수는 없다.

- await가 붙으면 해당 코드가 실행되고, 그 코드가 리턴하는 프로미스 객체가 settled될 때까지 기다려준다. settled되면 그 작업 결과를 response에 넣어준다.
- 이 때 settled 될때까지 기다리면서 function 외부 코드부터 실행하고, 외부 코드가 다 끝나면 그제야 다시 함수 안으로 들어온다!!!

함수 실행 순서 예시.

```js
async function fetchAndPrint() {
  console.log(2);
  const response = await fetch("url");
  console.log(6);
  const result = await response.text();
  console.log(result);
}
console.log(1);
fetchAndPrint();
console.log(3);
console.log(4);
console.log(5);
```

이렇게 async 구문을 쓰면 코드가 동기 실행되는 것처럼 보인다. 즉, 코드의 가독성이 높아지고 개발자가 더 편하게 작성할 수 있는 일종의 syntactic sugar이다.

즉, async 구문을 통해 then 메소드를 사용하지 않고도 편하게 쓸 수 있다는 점. 단, 동기 실행처럼 실행되지 않으니 비동기 실행되는 부분을 잘 예측해서 코드를 해석, 작성해야 한다!!

<br>

## 2. catch, finally 문

만약 async 구문을 썼을 때 promise 객체가 내부에서 rejected 상태가 된다면? 이걸 해결하기 위해 catch 문을 쓰자.

```js
async function print() {
  try {
    // ..
  } catch (error) {
    //...
  } finally {
    //...
  }
}
```

<br>

## 3. async 함수의 리턴값

async 함수는 promise 객체를 리턴한다.

```js
// 이 코드에서 print 함수는 3을 작업 성공 결과로 가진 promise 객체를 리턴
async function print() {
  return 3;
}
```

함수가 무엇을 리턴하는지에 따라 promise 객체가 달라진다.

1. promise 객체를 리턴하는 경우: 함수도 동일한 상태와 정보를 가진 promise 객체 리턴.
2. 객체 이외에 string, 숫자, 일반 객체를 리턴할 경우 fulfilled 상태에 해당 리턴 값을 작업 성공 결과로 가진 promise 객체를 리턴
3. 아무것도 리턴하지 않는 경우 undefined를 리턴한다고 간주하여 fulfilled 상태이면서 결과로 undefined를 가지는 객체 리턴.
4. 함수 내부에 에러가 발생하면 rejected 상태에 에러 객체를 실패 정보로 가진 promise 객체 리턴.

<br>

## 4. async 함수 내의 async

async 함수가 여러 개 있을때 한 함수 내에서 다른 async 함수를 호출해서 쓸 수도 있다. 어차피 async 함수는 promise 객체를 리턴하므로, 함수 호출문에 await 키워드를 붙이면 된다!!

```js
async function a1() {}
async function a2() {
  //...
  const a1 = await a1();
  // ...
}

a2().then(/*함수 작성..*/);
```

<br>

## 5. async 함수 작성할 때 주의할 것.

1. async 키워드는 어디에 붙일까?

- 일반적인 함수 선언에서는 앞에서 배운 대로 붙이자.
- 기명 함수 표현식이나 무기명 함수 표현식에서도 function 키워드 앞에 붙이면 된다.
- 화살표함수에서는 파라미터 앞에 붙인다.

```js
// 1) Function Declaration
async function example1(a, b) {
  return a + b;
}

// 2-1) Function Expression(Named)
const example2_1 = async function add(a, b) {
  return a + b;
};

// 2-2) Function Expression(Anonymous)
const example2_2 = async function (a, b) {
  return a + b;
};

// 3-1) Arrow Function
const example3_1 = async (a, b) => {
  return a + b;
};
```

즉시 실행함수에서 async는 다음과 같이 붙인다.

```js
(async function print(sentence) {
  console.log(sentence);
  return sentence;
})("I love JavaScript!");

(async function (a, b) {
  return a + b;
})(1, 2);

(async (a, b) => {
  return a + b;
})(1, 2);

(async (a, b) => a + b)(1, 2);
```

2. async를 쓸 때엔 성능을 주의하자.

for of문으로 여러 번 객체를 가져올 때 굳이 순서를 안 지키고 아무 순서로 객체를 받기만 하면 된다면 async 위치를 적절하게 쓰자.

<br>

## 6. 두 가지 종류의 콜백.

<br>
