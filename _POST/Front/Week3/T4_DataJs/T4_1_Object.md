# 🍊 객체 🍊

#### Week3 JS 기초 / Topic 4 JS와 Data / 1. 객체

> 목차
>
> > [1. 객체와 프로퍼티](#1-객체와-프로퍼티)<br>
> > [2. 객체 다루기](#2-객체-다루기)<br>
> > [3. 객체와 메소드](#3-객체와-메소드)<br>
> > [4. for in 반복문](#4-for-in-반복문)<br>
> > [5. data 객체](#5-data-객체)<br>

<br><br>

## 1. 객체와 프로퍼티

변수가 하나의 값을 담는 상자라면, 객체란 하나의 큰 상자다!! 이 안에 여러 값을 넣을 수 있다.

```js
// 중괄호 하나가 객체 하나.
{
    brandName: '코드잇',
    bornYear: 2017,
    isVeryNice: true,
    worstCourse: null,
    bestCourse:{
        title: 'JS',
        language: 'js'
    }
}
```

여기서 brandName 같은 걸 key, 코드잇 같은 걸 value 라고 하며 이렇게 **키와 밸류 한 쌍을 객체의 속성** 이라고 한다!!

키는 반드시 문자열 string 형이어야 하지만, js가 자동으로 형변환 해주기때문에 따옴표를 생략해도 된다.

그래서 키를 프로퍼티 이름, 밸류를 프로퍼티 값이라고도 한다.

- 속성 이름을 지을 때, 첫 글자는 반드시 문자, 밑줄, 달러 기호 중 하나로 시작하자. **숫자는 맨 앞에 못 옴!!**
- 속성 이름을 지을 때, 띄어쓰기나 하이픈은 금지.
- 만약 따옴표로 속성 이름을 묶어준다면 띄어쓰기 쓸 수는 있다.
- 만약 따옴표로 속성 이름을 묶어준다면 숫자를 맨 앞에 쓸 수는 있다.

객체 안에는 객체가 또 속성값으로 들어갈 수 있다.

<br>

## 2. 객체 다루기

객체를 다루기 위해 객체에 이름을 줘야 한다.

```js
let codeit = {
  brandName: "코드잇",
  bornYear: 2017,
  isVeryNice: true,
  worstCourse: null,
  bestCourse: {
    title: "JS",
    language: "js",
  },
};
```

이제 객체에서부터 속성 값을 가져오려면 두 가지 방법이 있다.

1. 점 표기법: 그러나 속성 이름에 띄어쓰기 등이 있어서 따옴표로 묶었을 때는 못 쓴다.

```js
let codeit = {
  brandName: "코드잇",
  bornYear: 2017,
  isVeryNice: true,
  worstCourse: null,
  bestCourse: {
    title: "JS",
    language: "js",
  },
};
console.log(codeit.brandName);
console.log(codeit.bestCourse.title);
```

2. 대괄호 표기법: 점 표기법보단 귀찮아도 속성 이름을 유연하게 짤 수 있다는 장점이 있다.

```js
let codeit = {
  brandName: "코드잇",
  bornYear: 2017,
  isVeryNice: true,
  worstCourse: null,
  bestCourse: {
    title: "JS",
    language: "js",
  },
};
console.log(codeit["brandName"]);
let name = "brandName";
console.log(codeit[name]);
```

3. 점과 대괄호 표기법을 섞을 수도 있다.

```js
let codeit = {
  brandName: "코드잇",
  bornYear: 2017,
  isVeryNice: true,
  worstCourse: null,
  bestCourse: {
    title: "JS",
    language: "js",
  },
};
console.log(codeit.bestCourse["title"]);
```

상황에 맞게 유연하게 쓰자.

**만약 존재하지 않는 속성의 값을 가져오려 하면 에러는 안 나고 undefined가 출력됨.**

**참고로 변수 속성이름에는 let이나 function 같은 예약어를 써도 된다. 특수 예외 케이스가 있긴 한데 일단은 쓸 수 있음..**

객체의 프로퍼티 값을 수정하려면 그냥 다시 삽입하면 된다.

```js
let codeit = {
  brandName: "코드잇",
  bornYear: 2017,
  isVeryNice: true,
  worstCourse: null,
  bestCourse: {
    title: "JS",
    language: "js",
  },
};

codeit.brandName = "codeit"; // 값 수정
codeit.ceo = "강영훈"; // 새로운 속성 삽입
delete codeit.worstCourse; // 속성 삭제
```

객체 안에 내가 찾는 프로퍼티가 있는지 확인하려면?

```js
// 값이 있다면 undefined가 아니니까 참으로 나올 것!!
console.log(codeit.name !== undefined);

// in 키워드를 써서도 확인할 수 있다. 값이 있으면 참으로 나온다!
console.log("name" in codeit);
```

객체 안의 프로퍼티 유무를 확인할 때엔 in 키워드를 쓰는 게 더 낫다. 내가 실수로 undefined 값을 할당할 수도 있으니까.

<br>

## 3. 객체와 메소드

여러 비슷한 메소드를 하나로 묶을 때에도 객체에 다 집어넣으면 된다. 프로퍼티 값으로 함수를 넣으면 됨!!

**이런 함수를 객체의 메소드라고 부른다.**

```js
let greetings = {
  sayHello: function (name) {
    console.log(name);
  },
  sayHi: function (name) {
    console.log(name);
  },
  sayBye: function (name) {
    console.log(name);
  },
};

greetings.sayHello("hellen");
greetings["sayHi"]("hellen");
```

이렇게 객체 안에 함수를 만들면 함수 이름 중복도 피할 수 있고 객체에 집중해서 고유 동작을 만들 수도 있고 코드가 의미있어진다.!!

<br>

## 4. for in 반복문

for in은 객체 안의 프로퍼티를 가지고 반복적인 일을 하기 때문에, 일반 for 문으론 짜기 복잡한 코드를 좀 더 쉽게 짜게 해준다.

```js
let codeit = {
  brandName: "코드잇",
  bornYear: 2017,
  isVeryNice: true,
  worstCourse: null,
  bestCourse: {
    title: "JS",
    language: "js",
  },
};

for (let key in codeit) {
  console.log(key);
  console.log(codeit[key]);
}
```

#### 주의할 점!!!

일반적으로 객체에 추가되는 프로퍼티 순으로 for in 문이 실행되지만, 프로퍼티 네임 중 정수형이 있을 땐 정수를 오름차순으로 번저 정렬한 후 나머지 프로퍼티를 추가로 읽는다!! (굳이 for in 안 써도 그냥 자동으로 정렬된 채로 추가됨.)

이는 정수형으로 프로퍼티 이름 짓고 따옴표로 묶어서 string 처리해도 그렇다.

```js
let object = {};
object["2"] = "나";
object["1"] = "가";

// 이렇게 하면 2를 먼저 넣었는데도 1이 먼저 출력됨.
```

따라서 정수형 프로퍼티 이름은 거의 쓰지 않는다.

## 5. data 객체

js가 미리 가지고 있는 객체를 (ex. console 같은 거...) **내장 객체, standard built-in object라고 한다.**

```js
// 내장객체 예시 1. Date
let myDate = new Date();
console.log(myDate);

let myDate1 = new Date("1998-05-30");
console.log(myDate1);

// 타임스탬프. 객체 소환하고 난 이후로 얼마나 시간이 지났는지.
console.log(myDate.getTime());
```

내장 객체에 줄 수 있는 인자로는 겁나 많으니까 찾아보고 적절히 사용하자.

이런 내장 객체를 이용해서 간단한 프로그램도 만들 수 있다.

Date 객체로 D-day 계산기를 만들어보자.

```js
let today = new Date(2112, 7, 24);
let jaeSangStart = new Date(2109, 6, 1);

function workDayCalc(startDate) {
  // 여기에 코드를 작성하세요
  let timeDiff = (today - jaeSangStart) / 1000 / 60 / 60 / 24;
  console.log(`오늘은 입사한 지 ${timeDiff + 1}일째 되는 날 입니다.`);
}

workDayCalc(jaeSangStart);
```
