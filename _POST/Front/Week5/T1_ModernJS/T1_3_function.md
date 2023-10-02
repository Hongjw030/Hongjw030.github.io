# 🍆 함수 🍆

#### Week5 모던 자바스크립트 / Topic 1 모던 자바스크립트 / 3. 함수

> 목차
>
> >

1. 함수 만들기
2. 이름 있는 함수 표현
3. 즉시 실행 함수
4. 값으로서의 함수
5. parameter
6. arguments
7. rest parameter
8. arrow function
9. this<br>

<br><br>

## 1. 함수 만들기

1. 함수를 function 키워드를 통해 선언하기

```js
function addNum(a, b) {
  return a + b;
}
```

2. 변수에 함수 선언하기: 함수 표현식, function expression이라 한다!! 굳이 변수 이름을 안 정해도 addEventListener할 때 익명 함수 쓰듯이 하는 방식도 함수 표현식이다.

- 이렇게 선언하는 함수는 변수 이름을 자동으로 name 프로퍼티에 변수 이름이 등록 된다.

```js
myBtn.addEventListener("click", function () {
  console.log("이것도 함수 표현식이다.");
});
// 이 함수의 myBtn.name = myBtn
const myBtn = function () {
  console.log("함수 표현식!!");
};
```

- 이렇게 함수 표현식으로 함수를 선언하면 const 특성 상 hoisting 문제가 일어나지 않는다. function으로 함수 선언하면 hoisting 발생!
- 또한 const 특성 상 함수 표현식을 코드 블록 내부에 쓰면 지역 함수처럼 쓸 수 있고 바깥에서는 못 쓴다.
- 함수 선언 방식은 자유롭게 선언 가능한 게 장점이지만 함수 표현식 방식은 코드에 일관성을 가질 수 있단 게 장점이다.

<br>

## 2. 이름 있는 함수 표현

Named function expression 기명 함수 표현식.

함수 표현식으로 함수를 만들 때 함수에 이름을 붙여줄 수도 있는데 이를 기명 함수 표현식이라 한다.

보통 변수의 name 프로퍼티에 변수 이름 그 자체를 갖지만,

```js
const sayHi = function () {
  console.log("Hi");
};

console.log(sayHi.name); // sayHi 출력
```

함수에 이름을 붙여주면 name 속성은 함수 이름을 문자열로 갖게 된다. 물론 이름을 붙여준다 해서 블록 외부에서 호출할 수 있다 이런 건 아님!!

```js
const sayHi = function printHiInConsole() {
  console.log("Hi");
};

console.log(sayHi.name); // printHiInConsole 호출됨.
```

이렇게 이름을 선언하는 것은

1. 함수 내부에서 자기 자신함수를 가리킬 때 사용된다. 즉, 재귀 함수 만들 때에 생긴다!
2. 함수를 복사할 때 사용된다!!

```js
// 재귀함수에서 기명 함수 표현식을 쓰자.
let countdown = function (n) {
  console.log(n);

  if (n === 0) {
    console.log("End!");
  } else {
    countdown(n - 1);
  }
};
countdown(5);

// 함수를 복사할 때 이름을 붙이자.
let countdown = function (n) {
  console.log(n);
  if (n === 0) {
    console.log("End!");
  } else {
    countdown(n - 1);
  }
};

let myFunction = countdown;

countdown = null;

myFunction(5); // TypeError

/////////
let countdown = function printCountdown(n) {
  console.log(n);
  if (n === 0) {
    console.log("End!");
  } else {
    printCountdown(n - 1);
  }
};

let myFunction = countdown;

countdown = null;

myFunction(5); // 정상 작동
```

<br>

## 3. 즉시 실행 함수

함수가 선언된 그 즉시 바로 실행하기. 이를 immediately invoked function expression, IIFE라고 부른다.

```js
(function () {
  console.log("hi");
})();

(function (x, y) {
  console.log(x + y);
})(3, 5);
```

IIFE는 함수에 이름을 지어주더라도 외부에선 사용 불가능하다. 그래서 보통 IIFE는 이름 없는 익명함수로 만들지만, 재귀함수 같은 걸 구현할 때엔 이름이 필요할 수도 있다.

```js
(function printHi() {
  console.log("hi");
})();
printHi(); // 에러 발생!!!

(function countdown(n) {
  // 재귀 함수에선 이름을 붙이자.
  console.log(n);
  if (n === 0) {
    console.log("End!");
  } else {
    countdown(n - 1);
  }
})(5);
```

1. 선언 동시에 실행되는 함수기 때문에 보통 프로그램 초기화 기능으로 실행된다.

```js
(function init() {
  // 프로그램이 실행 될 때 기본적으로 동작할 코드들..
})();
```

2. 재사용 하지 않을 일회성 함수로도 활용된다. 함수 내부 변수는 외부 전역변수로부터 조금은 자유로워지니 이걸 활용해 더 자유로운 코드를 짤 수도 있다.

```js
const firstName = "Young";
const lastName = "Kang";

const greetingMessage = (function () {
  const fullName = `${firstName} ${lastName} `;

  return `Hi! My name is ${fullName}`;
})();
```

<br>

## 4. 값으로서의 함수

함수를 변수처럼 활용할 수 있다.

객체 속성으로 넣거나, 값으로 넣거나, 다른 함수의 인자로 주는 등을 할 수 있다!!

(이렇게 다른 함수의 인자로 넘겨주는 함수를 callback 함수라고도 한다.)

**고차함수**

고차함수는 함수를 이중으로 쓸 수 있게 하는 방식이다.

```js
function getPrintHi() {
  return function () {
    console.log("hi");
  };
}

// hi 출력됨.
const hi = getPrintHi();
console.log(getPrintHi());
console.log(hi);

// 얘도 hi 출력됨.고차함수로 리턴되는 함수를 바로 호출하려면 소괄호를 두 번 쓰자.
getPrintHi()();
```

이렇게 함수를 다양하게 활용할 수 있는 것을 일급 함수라 하고, 그래서 js는 일급 함수 언어라고도 불린다!!

<br>

## 5. parameter

파라미터란 함수에 값을 전달하기 위해 사용하는 변수. **외부로 부터 값을 전달받기 위해 함수를 선언할 때 작성하는 것이 파라미터, 함수를 호출 할 때 파라미터로 전달하는 값이 인자이다!!**

```js
// name이 파라미터
function print(name) {
  console.log(name);
}

// hongjw이 아규먼트이다!
print("hongjw");
```

함수 파라미터에 옵셔널 값을 줄 수도 있다. 단, 옵셔널 파라미터는 오른쪽으로 주자.

```js
function greeting(name = "hong") {
  console.log(name);
}
```

옵셔널 값을 여러 개 쓰고 싶다면 undefined를 의도적으로 주고 옵셔널 값을 발동시킬 수도 있다.

```js
function greeting(name = "hong", age=20, interest){
    console.log(name);
    console.log(age);
    console.log(interest);
}

// 25 js undefined가 출력됨.
greeting(25 "js");

// hong 25 js 출력됨.
greeetings(undefined, 25, "js");
```

옵셔널 값으로 특이한 함수를 만들 수도 있다.

```js
function default(x, y=x+3){
    console.log(x);
    console.log(y);
}

// x에 2, y에 7 할당됨.
default(2, 7);

// x에 2, y에 5 할당됨
default(2);
```

<br>

## 6. arguments

함수를 만들 때 인자 개수를 정하지 않고 1개나 여러 개나 맘대로 주고 싶다면 어떻게 해야 할까?

**함수 내부에서 arguments라는 특별한 객체를 쓰자!**

```js
function printArg(a, b) {
  console.log(arguments);
  console.log(arguments.length);
  console.log(arguments[0]);

  for (let arg of arguments) {
    console.log(arg);
  }
}
```

이렇게 하면 인자를 몇 개를 받든 활용 가능하다.

단, arguments는 유사배열이라 배열 메소드를 쓸 수 없다. splice 같이 인덱스 기준으로 자르기가 불가능한 것.

```js
// 활용 예시
function firstWords() {
  let word = "";
  for (let i of arguments) {
    word += i[0];
  }
  console.log(word);
}

firstWords("나만", "없어", "고양이");
firstWords("아니", "바나나말고", "라면먹어");
firstWords("만두", "반으로", "잘라먹네", "부지런하다");
firstWords("결국", "자바스크립트가", "해피한", "지름길");
firstWords("빨간색", "주황색", "노란색", "초록색", "파란색", "남색", "보라색");
```

<br>

## 7. rest parameter

arguments 객체로는 쓰기 귀찮은 작업들이 있어서, 2015년 이후 rest parameter이라는 문법이 등장했다.

```js
function printArg(...args) {
  for (const arg of args) {
    console.log(arg);
  }
}
```

rest parameter은 배열이라 배열 메소드를 쓸 수 있다!! splice로 인덱싱 접근이 가능하다.

**rest parameter은 인자 여러 개를 받으면 필수 인자 이외의 것들을 배열로 묶는 역할이므로 꼭 파라미터 맨 마지막에 써야 한다.**

```js
function printArg(first, second, ...others) {
  console.log(first);
  console.log(second);
  for (const arg of others) {
    console.log(arg);
  }
}
```

이젠 rest parameter만 기억하고 쓰면 되지만, 2015년 문법 이전에는 arguments도 자주 썼으니 arguments도 알아두자.

<br>

## 8. arrow function

2015 이후에 새롭게 등장한 문법이다!

arrow function은 기존 함수 선언을 좀 더 간결하게 만들어준다. arrow function으로 만든 함수는 이름이 없는 익명 함수기 때문에 보통 다른 함수의 아규먼트를 선언할 때나 함수 표현식을 쓸 때 많이 사용한다.

```js
// 일반 함수표현식
const double = function (num) {
  return num * 2;
};
myBtn.addEventListener("click", function () {
  console.log(e.target);
});

// arrow function
const double = (num) => {
  return num * 2;
};
myBtn.addEventListener("click", () => {
  console.log(e.target);
});
```

특정 상황에서는 arrow function을 더 간결하게 쓸 수도 있다.

```js
// 1. 파라미터가 1개 뿐일 때엔 소괄호 생략 가능. 근데 가독성 문제로 그냥 소괄호 다 쓰는 게 좋다.
//const double = num => {
//  return num * 2;
//};

// 2. 함수가 return 문만 있다면 중괄호와 리턴 생략 가능.
const double = (num) => num * 2;
```

리턴 값이 객체인 경우 소괄호를 쓰면 가능하다.

```js
//위 아래는 같은 함수.
const getPrint = function () {
  return { name: "print" };
};
const getPrint = () => {
  (
    // 이 소괄호 없어지면 에러.
    name: "print";
  )
};
```

arrow function은 arguments 못 쓴다. 대신 rest parameter은 사용 가능!! 또한 옵셔널 파라미터를 줄 수 있다.

**모든 화살표 함수는 익명 함수이다!!** 이름을 따로 줄 수는 없고 변수에 할당하거나 다른 함수를 호출할 때 아규먼트로 사용 가능.

<br>

## 9. this

this는 기본적으로 전역 객체인 window를 가리킨다.

그런데 객체의 메소드로 this가 쓰이는 경우엔 this는 메소드를 호출한 해당 객체를 가리킨다.

```js
function getName() {
  return `$(this.first) $(this.last)`;
}

const user = {};
const admin = {};
// user의 name 출력
console.log(user.getName);
// admin의 name 출력
console.log(admin.getName);
```

**단, arrow function은 this 값을 가질 수 없다!!**

정확히 말하자면 arrow 함수 내부에 선언되는 this 키워드는 객체에 따라 값이 바뀌지 않고, 직전에 사용됐던 객체의 값만 담기 때문에 this를 활용하기 어렵다.

이런 점 때문에 일반 함수가 arrow보다 더 권장되기도 한다.

<br>
