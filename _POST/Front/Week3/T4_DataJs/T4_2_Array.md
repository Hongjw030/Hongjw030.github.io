# 🍍 배열 🍍
#### Week3 JS 기초 / Topic 4 JS와 Data  / 2. 배열

>목차 
>>[1. 배열](#1-배열)<br>
[2. 배열 메소드](#2-배열-메소드)<br>
[3. for of 반복문](#3-for-of-반복문)<br>
[4. 다차원 배열](#4-다차원-배열)<br>




<br><br>

## 1. 배열
객체는 여러 각기 다른 프로퍼티들이 있을 때 효과적이고, 만약 프로퍼티 자료형이 모두 같다면 , 그리고 각 요소의 순서가 중요하다면 배열이 낫다.
```js
let courseRanking = [
    'JS 기초',
    'Git',
    '컴퓨터 개론',
    '파이썬 기초'
];
```
배열은 객체와 달리 대괄호를 쓴다!

그리고 각자 순서가 붙어있다. **index**

```js
let courseRanking = [
    'JS 기초',
    'Git',
    '컴퓨터 개론',
    '파이썬 기초'
];
console.log(courseRanking[2]);
// 이러면 컴퓨터 개론이 출력된다. 
```

배열도 하나의 객체로, console.log(typeof courseRanking) 치면 object라고 출력된다. 따라서 배열에도 여러 내장 함수들이 있다!!!

```js
let courseRanking = [
    'JS 기초',
    'Git',
    '컴퓨터 개론',
    '파이썬 기초'
];

// 배열 길이 알려주는 length
console.log(courseRanking.length);
console.log(courseRanking['length']);


// 배열에 값 수정하거나 넣기
courseRanking[3] = "파이썬 핵심.";
courseRanking[4] = "배열 다루기";

// 배열에 값 삭제하려는데 delete 명령어를 쓰면 값만 삭제돼서 empty 요소로 그 자리 그대로 남아있다.
delete courseRanking[2]; 

```
만약 length가 5인데 갑자기 8번 원소를 넣는다면?

* 배열의 6, 7번 원소는 empty로 생성되면서 length도 8이 돼버림. 주의하자!!!


<br>

## 2. 배열 메소드
```js
// splice
let members = [0,1,2,3,4,5];

// 1 포함 1 인덱스 이후의 모든 값 삭제. 0만 남음. 
members.splice(1); 
// 1 포함 1 인덱스 이후의 2개 값 삭제. 0 3 4 5
members.splice(1,2);
// 1 삭제하고 그 자리에 6, 7 넣음. 0 6 7 3 4 5
members.splice(1,1, 6, 7);
// 삭제 안하고 1번 인덱스에 6 넣음. 0612345
members.splice(1,0, 6); 
// 1번 인덱스 값 6으로 수정
members.splice(1,1, 6);


// 배열 첫 요소 삭제
members.shift();


// 배열 마지막 놈 삭제
members.pop();

// 배열 맨 처음에 값 추가.
members.unshift("value");

// 배열 맨 마지막에 값 추가.
members.pop("value");

// 배열에서 특정 값 위치 찾기
members.indexOf('value'); // value의 위치를 알려줌.

// 배열에 중복 값들이 있다면 중복 중 가장 끝에 있는 원소 위치를 리턴.
members.lastIndexOf('value');

// 배열에 특정 값이 있는지 확인
members.includes('value');

// 배열 순서 뒤집기
members.reverse();
```

indexOf 함수로 특정 값을 찾을 때 값이 없다면 -1, 값이 여러 개라면 가장 먼저 있는 값의 인덱스를 리턴한다. 

indexOf는 해당 값의 위치를 리턴하고, includes는 그냥 값이 있는지 없는지만 체크.

<br>

## 3. for of 반복문
단순 for문으로도 가능하지만, for of로 더 간결한 코드를 짤 수 있다.

```js
for(변수 of 배열){
    동작 코드.
}

for (let element of members){
    console.log(element);
}
```
for in 도 배열에 쓸 수 있지만 for in은 객체같이 프로퍼티를 가지고 있는 경우에 쓰는 게 낫다. 

<br>

## 4. 다차원 배열
배열에도 객체처럼 안에 딱히 제한된 자료형이 없기 때문에, 배열 안에 배열을 넣을 수 있다. 이를 다차원배열이라 한다.
```js
// 이차원 배열
let twoDimension = [
    [1, 2],
    [3, 4]
]
```

값 하나하나의 의미가 중요하다면 객체를 활용하고, 의미가 아니라 위치나 순서가 중요하다면 배열을 쓰자. 