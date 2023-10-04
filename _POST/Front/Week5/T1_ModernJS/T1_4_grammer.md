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

2015년 이후 문법으로, 객체의 프로퍼티를 좀 더 간결하게 표기하는 문법이다.

```js
// 기존 문법
const title = "hellen";
const birth = 2016;
const job = "programmer";
function getName() {
  return `${this.title}: ${this.job}`;
}
const user = {
  title: title,
  birth: birth,
  job: job,
  getName: getName,
};

// 2015년 이후론 변수 이름과 프로퍼티 이름이 같다면 하나만 써도 된다!!
const user = {
  title,
  birth,
  job,
  getName,
};

// 객체 내부에 함수를 생성할 때에도 콜론과 function 키워드를 생략할 수 있다.
const user2 = {
  title,
  birth,
  job,
  getName2() {
    return "getName2";
  },
};
console.log(user2.getName2());

// 계산된 값을 속성이름으로 활용하는 computed property name
// 이렇게 표현식을 대괄호로 감싸서 속성을 표현하는 방식도 있다!
const user3 = {
  // [표현식]: 속성 값
  ["hellen" + "hong"]: 26,
};
```

**중요한 점!!! 대괄호로 감싸서 속성을 부를 때랑 점으로 속성 부를 때가 다르다.**

```js
const propertyName = "birth";
const getJob = () => "job";

const codeit = {
  ["topic" + "Name"]: "Modern JavaScript",
  [propertyName]: 2017,
  [getJob()]: "프로그래밍 강사",
};

console.log(codeit[propertyName]); // 2017 출력
console.log(codeit.birth); // 2017 출력

console.log(codeit.job); // 강사 출력
console.log(codeit[getJob()]); // 강사 출력

console.log(codeit.propertyName); // undefined 출력
```

<br>

## 5. 옵셔널 체이닝

안전하게 속성 값에 접근하는 방법. 2020 년에 등장한 문법이다.

일반적으로는 점 표기법을 통해 객체에 접근하는데, 중첩된 객체를 다루다보면 헷갈려서 예상치 못한 오류가 날 수도 있다.

따라서 중첩된 객체 내부의 속성 값에 접근하기 위해 옵셔널 체이닝 방법을 쓰자!!

```js
// 일반적인 호출 방식
function printCatName(user) {
  console.log(user.cat.name);
}

const user1 = {
  name: "Captain",
  cat: {
    name: "Crew",
    breed: "British Shorthair",
  },
};
const user2 = {
  name: "Young",
};

printCatName(user1); // Crew 출력
printCatName(user2); // undefined.name에 접근하면서 에러 발생

// 옵셔널 체이닝을 안 쓰면 AND 연산자나 if 문으로 해결할 수는 있지만 속성이나 객체 이름이 길어질 수록 가독성이 나빠진다.
function printCatName2(user) {
  console.log(user.cat && user.cat.name);
}

// 옵셔널 체이닝을 쓴 경우!
function printCatName3(user) {
  // ? 왼쪽 값이 undefined나 null이 아니라면 오른쪽 속성 값을 리턴하고, 그렇지 않으면 undefined 출력.
  console.log(user.cat?.name);
}
```

<br>

## 6. 구조 분해

배열과 객체를 다룰 때 사용하는 2015년 이후 문법. 배열이나 개체의 구조를 분해하는 문법이다.

구조분해는 객체와 배열 각각에 적용되는 방식이 다르다!!

1. 배열에 적용되는 구조 분해

```js
const rank = ["a", "b", "c", "d", "e"];

// rank 같은 배열을 꼭 할당해야 한다. 아예 할당을 안하거나 배열이 아닌 것을 할당하면 에러 발생!
const [first, second, third] = rank;
// first 변수에 'a' 값 할당됨 ... d, e 는 넘쳐서 할당 안됨!

// ... 을 통해 나머지 넘친 값들은 rest 배열에 넣어준다.
const [first, second, third, ...rest_param] = rank;

// 만약 배열 길이가 선언된 변수보다 적으면 남은 변수에는 undefined 할당됨.
// 아래에선 sixth에 undefined 값 할당됨.
const [first, second, third, fourth, fifth, sixth] = rank;

// 여기서도 기본값을 넣을 수 있다!!
const [first, second, third, fourth, fifth, sixth = "no value"] = rank;

// 구조분해로 두 개의 값을 바꿔줄 수도 있다.
// 기존 문법에선 temp 변수로 옮겨줘야 하지만... 구조분해는 파이썬처럼 가능!
[first, second] = [second, first];

console.log(first);
```

2. 객체에서의 구조 분해

- 점 표기법으로 계속 객체 이름 작성하지 말고 간단하게 프로퍼티 네임 자체를 변수처럼 활용할 때 쓴다.

```js
const myComputer = {
  title: "ASUS",
  price: 1000,
  memory: "16GB",
  "serial-num": "asdf",
};

// 기본적인 속성 접근
const title = myComputer.title;
const price = myComputer.price;

// 구조분해로 속성 접근하기
// 속성이 순서대로 값이 넣어지는 게 아니라 프로퍼티 이름을 통해 분해가 된다!
// 그래서 color 변수에는 undefined 값 할당됨.
const { title, price, color } = myComputer;

// 얘도 기본값을 설정할 수 있다.
const { title, price, color = "black" } = myComputer;

// rest parameter도 사용 가능.
const { title, ...rest } = myComputer;

// 속성 이름 말고 다른 변수 이름을 선언하고 싶다면 콜론을 쓰자.
// 이제 name이라는 변수에 myComputer.title 값이 담긴다.
const { title: name, ...rest } = myComputer;

// 만약 속성 이름에 하이픈이 들어간다면 위에처럼 다른 변수 이름을 선언해야 한다! 변수 이름에 하이픈을 넣을 수는 없으니까.
const { title, "serial-num": serialNum } = myComputer;

// 대괄호로 computed property name도 쓸 수 있다.
const propName = "title";
const { [propName]: product } = myComputer;
```

<br>

## 7. 함수와 구조 분해

구조분해를 함수를 쓸 때 어떻게 활용할 수 있을까?

1. 구조분해 변수명 리턴하는 함수

```js
function getArr() {
  return ["a", "b", "c"];
}
const [e1, e2, e3] = getArr();
console.log(e1); // a 출력
```

2. 파라미터에 쓰기

```js
function printName(a, b, c, ...rest) {
  console.log(a);
}
const ranks = ["a", "b", "c", "d"];
printName(ranks); // a 출력됨.
```

3. 객체를 함수 내부에서 구조분해하기

```js
const obj = {
  title: "aaa",
  age: 16,
};
function printObj(object) {
  const { title, age } = object;
  console.log(title);
  console.log(age);
}

// 아래처럼 파라미터에 바로 구조분해도 가능.
function printObj({ title, age, price = 1000 }) {
  console.log(title);
  console.log(age);
}
printObj(obj);
```

4. 실제로 활용해본다면

```js
// event.target을 target 변수에 넣어서 쓰기.
const btn = document.querySelector("#btn");
btn.addEventListener("click", ({ target }) => {
  target.classList.toggle("chcked");
});

// 중첩 객체 구조 분해, nested object destructure도 있다. 이건 때에 따라 비효율적일 수도 있음.
btn.addEventListener("click", ({ target: { classList } }) => {
  classList.toggle("chcked");
});

// 굳이 중첩 객체 구조분해를 쓰지 않아도 이렇게 활용할 수도 있다.
btn.addEventListener("click", ({ target }) => {
  const { classList } = target;
  classList.toggle("chcked");
});
```

**배열에 구조분해 쓸 때엔 [] 객체에 구조분해 쓸 때엔 {}**

배열에 {} 쓰면 에러 난다.

<br>

## 8. 에러와 에러 객체

에러가 발생한 순간 프로그램이 멈추기 때문에 에러를 잘 처리하는 게 중요하다.

js는 에러가 발생하면 자동으로 그 에러가 담긴 에러 객체를 생성한다. 에러 객체에는 공통적으로 name과 message 속성을 갖고 있다.

1. 에러 객체 직접 만들어보기

```js
// 그냥 에러 객체 만든 거지 에러를 의도적으로 발생시킨 건 아니다.
const error = new TypeError("타입 에러 발생!");
console.log(error.name);
console.log(error.message);

// 에러를 발생시키는 건 throw 키워드를 쓰자.
throw error;
```

<br>

## 9. try catch

에러가 발생하는 예외 상황을 처리하기 위해 try catch 문을 사용하자.

```js
try {
  //일반 코드
} catch (error) {
  // 에러가 발생했을 때 동작할 코드
}

// 예시
try {
  const codeit = "code";
  console.log(codeit);
  codeit = "it"; //에러 발생
  console.log(codeit); //실행 안됨!!
} catch (e) {
  console.log("에러 발생"); // 에러 발생 이후 실행됨.
  console.error(e); // 빨간 메세지로 표시됨.
  console.log(e.name);
  console.log(e.message);
}
```

아예 프로그램 실행조차 되지 않는 syntax error은 잡지 못하고, 실행 가능한 코드에서 발생하는 에러인 type error, reference error 같은 경우에만 가능. 이런 실행 가능 에러를 exception이라 한다!!

그리고 이 exception을 처리하는 것을 예외 처리, exception handling이라고도 한다!!
<br>

## 10. finally

try catch 다음 finally 키워드도 붙일 수 있다.

1. 에러가 없는 경우: try 문 실행, catch 건너뛰고 finally 실행
2. 에러가 있는 경우: try 실행하다 도중에 catch 실행, 그 이후 finally 실행.

finally에서 에러가 발생해도 그 위에 있는 catch 문으로 넘어가지 않기 때문에, finally 블록 안에 중첩으로 try catch 문을 만들 수 있다!!

```js
try {
  // 실행할 코드
} catch (err) {
  // 에러가 발생했을 때 실행할 코드
} finally {
  // 항상 실행할 코드
}
```

```js
// 중첩 try catch

try {
  try {
    // 실행할 코드
  } catch (err) {
    // 에러가 발생했을 때 실행할 코드
  } finally {
    // 항상 실행할 코드
  }
} catch (err) {
  // finally문에서 에러가 발생했을 때 실행할 코드
}
```

<br>
