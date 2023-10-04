# 🌽 js 내부 기능 🌽

#### Week5 모던 자바스크립트 / Topic 1 모던 자바스크립트 / 5. js 내부 기능

> 목차
>
> > 1. for each와 map
> > 2. filter와 find
> > 3. some과 every
> > 4. reduce
> > 5. sort, reverse
> > 6. Map, SEt

<br><br>

## 1. 배열 메소드: for each와 map

- 객체 내 프로퍼티 순회할 때엔 for of
- 배열 내 요소 순회할 때에 for each
- for each는 return 값이 없다!!

```js
const members = ["a", "b", "c", "d"];

// for of로 배열 순회하기
for (let member of members) {
  console.log(member);
}

// forEach 배열 메소드. 첫 인자로 반드시 배열 원소를 줘야 한다.
members.forEach(function (member) {
  console.log(member);
});

// for each 메소드 arrow function으로 쓰면?
members.forEach((member) => {
  console.log(member);
});

// for each 메소드 두번째 인자로 index를 줄 수도 있다.
members.forEach((member, ind) => {
  console.log(`${ind} : ${member}`);
});

// for each 세번째 인자로 배열 자체를 줄 수도 있다.
members
  .forEach((members, ind, arr) => {
    console.log(arr);
  })

  [
    // 세번째 인자로 함수 내부에 배열 이름 붙이기!!
    ("a", "b", "c")
  ].forEach((members, ind, arr) => {
    // 이 배열은 함수 내부에서 arr이란 이름을 갖는다.
  });
```

- map도 foreach와 거의 비슷하다.
- forEach 이름을 map으로 바꾸기만 하면 쓸 수 있다!
- forEach와 다른 점은 map은 새로운 배열을 리턴한다는 것.

```js
const names = ["a", "b", "c"];
const users = names.map((name, i) => {
  return `${i}: ${name}`;
});

console.log(users); // 배열 출력됨.
```

**주의할 점!! forEach map 둘다 반복문 돌 때 맨 처음 선언된 배열의 길이만큼 반복한다!!**

```js
// e가 4번만 추가됨!! e 추가된다고 foreach를 5, 6... 계속 돌지 않음.
const users = ["a", "b", "c", "d"];
users.forEach((user) => {
  console.log(user);
  members.push("e");
});

// 그치만 요소 개수가 줄어들면 반복문 횟수도 줄어든다. a b 만 출력됨.
const users = ["a", "b", "c", "d"];
users.forEach((user) => {
  console.log(user);
  members.pop();
});
```

<br>

## 2. 배열 메소드: filter와 find

foreach와 map 처럼 반복적인 일을 하는 배열 메소드.

1. filter은 특정 조건에 맞는 요소만 가져오는 것. filter의 리턴 값은 항상 배열이기 때문에 spread를 사용해 배열을 벗겨내는 작업이 따로 필요하다.

```js
const devices = [
  { name: "a1", brand: "a" },
  { name: "a2", brand: "a" },
  { name: "a3", brand: "a" },
  { name: "b1", brand: "b" },
  { name: "b2", brand: "b" },
];

const As = devices.filter((el) => el.brand === "a");
```

2. find는 조건에 맞는 요소 하나를 바로 가져오는 것. 그래서 filter은 모든 요소를 돌면서 값들을 찾아 배열로 반환하는 반면에 find는 조건에 맞는 요소를 하나 찾자마자 그 값을 바로 리턴한다. 만약 없는 값을 찾으려면 undefined가 출력됨!

```js
const devices = [
  { name: "a1", brand: "a" },
  { name: "a2", brand: "a" },
  { name: "a3", brand: "a" },
  { name: "b1", brand: "b" },
  { name: "b2", brand: "b" },
];

const As = devices.find((el) => el.brand === "a");
```

**주의할 점!!! 중괄호로 함수 쓸 때엔 return을 써야 한다.**

```js
// 아무것도 리턴 안됨.
const As = devices.find((el) => {
  el.brand === "a";
});

// 이렇게 해야 함!
const As = devices.find((el) => {
  return el.brand === "a";
});
```

<br>

## 3. 배열 메소드: some과 every

1. some은 조건을 만족하는 요소가 적어도 1개 이상 있는지 true 혹은 false 리턴.

```js
// 조건을 만족하는 요소 만나면 바로 함수 중단!
const numbers = [1, 2, 3, 5, 7];
const someReturn = numbers.some((el) => el > 5);
```

2. every는 모든 요소가 조건을 만족하는지 확인하여 true 혹은 false 리턴.

```js
// 조건을 만족하지 않는 요소 만나면 그대로 함수 중단!
const numbers = [1, 2, 3, 5, 7];
const someReturn = numbers.every((el) => el > 5);
```

만약 빈 배열 []에 대해 some, every를 실행하면 some은 무조건 false, every는 무조건 true를 출력한다.

<br>

## 4. 배열 메소드: reduce

형태는 아래와 같다.

배열.reduce((누산기acc, 원소el, 원소인덱스i, 배열자체arr)=> {
return nextAccValue;
}, initialAccValue);

- acc 누산기: 함수가 호출되면 직전에 동작한 콜백함수가 리턴한 값을 전달 받는 파라미터이다.
- 최초 콜백 함수에서 누산기는 initialAccValue 이다.
- 만약 최초 누산기 initialAccValue값을 안 주면 그냥 배열의 0번 인덱스가 최초 값으로 들어간다.

```js
const numers = [1, 2, 3, 4];

const sumAll = numbers.reduce((acc, el, i) => {
  console.log(`${i}번 원소 콜백 함수 작동: `);
  console.log(`acc: `, acc);
  console.log(`el: `, el);
  console.log();
  return acc + el;
}, 0);

// 1. 0번 원소의 콜백 함수를 작동할 때 acc = 0 이므로 0 + 1 = 1을 리턴.
// 2. 1번 원소 콜백함수 작동할 때 acc는 1이므로 1 + 2 = 3
// 3. 2번 원소 콜백 함수 작동할 때 acc 는 3...
```

<br>

## 5. 배열 메소드 sort, reverse

**sort, reverse는 원본을 훼손하니 원본 배열이 필요하다면 어딘가에 복사해두자.**

**배열 복사는 얕은 복사를 해야 하니 splice나 spread를 쓰는 것도 잊지 말자!**

1. sort 메소드는 배열을 정렬하는 메소드다.

```js
// 메소드에 아무 인자도 없다면 기본적으로 유니코드 순 정렬을 한다.
const nums = [1, 3, 4, 2, 6];
nums.sort();
console.log(nums);

// 유니코드 정렬은 숫자 오름차순이나 내림차순 정렬과 다르다!!!
// 오름차순 정렬하려면
nums.sort((a, b) => a - b);

// 내림차순 정렬은
nums.sort((a, b) => b - a);
```

2. reverse 메소드는 배열 순서를 뒤집어준다. 별도의 파라미터가 없다.

```js
const nums = [1, 5, 2, 4, 6];
nums.reverse();
console.log(nums);
```

<br>

## 6. Map, SEt

기존에 쓴 데이터 구조는 객체와 배열이다.

2015년 이후 새로 등장한 데이터 구조, Map 과 Set이 있다!!

1. Map

- 이름이 있는 데이터를 저장하는 건 객체와 비슷하다.
- 할당 연산자 = 가 아니라 메소드를 통해 값을 추가하고 접근할 수 있다!.
- 객체는 문자열과 심볼 값만 프로퍼티 이름으로 쓸 수 있지만, map은 다양한 자료형을 key로 활용할 수 있다.

```js
const myMap = new Map();

// map.set(key, value) 는 map에 key value 쌍을 추가해준다.
myMap.set("title", "문자열 key");
myMap.set(2017, "숫자형 key");
myMap.set(true, "불린형 key");

// map.get(key) 는 key에 해당하는 value 값을 반환하고, key가 존재하지 않으면 undefined 반환.
console.log(myMap.get(2017));

// map.has(key) 는 key가 있으면 true, 없으면 false 반환.
console.log(myMap.has("title"));

// map.delete(key) 는 key value 쌍 삭제.
myMap.delete(2017);

// map.clear() 은 map 내 모든 요소 제거
map.clear();

// map.size 는 요소의 개수 반환 프로퍼티. 메소드 아님!!
console.log(map.size);
```

2. Set

- 요소를 순서대로 저장하는 게 배열과 비슷하긴 하다.
- 배열의 메소드는 쓸 수 없다.
- set은 특이하게 개별 값에 index로든 get 메소드로든 접근이 불가능하다! 단지 for of 문을 통해 전체 요소를 한꺼번에 다루는 순간 개별 접근이 가능하다.
- set은 중복 값을 허용하지 않는다. 중복된 값을 추가하려면 그걸 그냥 무시!!

```js
const mySet = new Set();

// set.add(value) 값 추가하고 추가된 set 자신을 반환.
mySet.add("a");
mySet.add("b");
mySet.add("c");

// set.has(value) 값이 있으면 true, 없으면 false 반환
console.log(set.has("a"));

// set.delete(value) set 내에 값이 있으면 제거하고 true 반환 없으면 false 반환
console.log(set.delete("d"));

// set.clear() 요소 모두 제거
set.clear();

// set.size 얘도 메소드 아니고 요소 개수 반환 프로퍼티!
console.log(set.size);
```

중복 허용치 않는다는 특성을 이용해 중복을 제거한 값들의 묶음을 만들 때 set을 활용한다.

```js
const numbers = [1, 3, 4, 3, 3, 3, 2, 1, 1, 1, 5, 5, 3, 2, 1, 4];
const uniqNumbers = new Set(numbers);

console.log(uniqNumbers); // Set(5) {1, 3, 4, 2, 5}
```

<br>
