# 🥥 제어문 🥥
#### Week3 JS 기초 / Topic 3 JS 핵심 / 3. 제어문

>목차 
>>[1. if 문](#1-if-문)<br>
[2. switch 문](#2-switch-문)<br>
[3. for 문](#3-for-문)<br>
[4. while 문](#4-while-문)<br>
[5. break와 continue](#5-break와-continue)<br>


<br><br>

## 1. if 문
조건에 따라 코드를 실행할지 말지 결정하는 제어문.
```js
if(조건){
    동작
}

let temperature = 10
if(temperature <=> 0){
    console.log('물이 업니다.');
}else{
    console.log('물이 얼지 않는다!');
}
```

조건을 여러 개 주기 위해선 else if 문을 사용하자.
```js
if(temperatore >= 100){
    console.log('물이 끓습니다.');
}else if (temperature > 0){
    console.log('물이 그대로입니다.');
}else{
    console.log('물이 업니다.');
}

```

## 2. switch 문
if와 비슷하게 조건에 따라 작동할 코드를 선택한다.
```js
switch(비교할 변수){
    case 값1:
        동작
        break;
    case 값2:
        동작
        break;
    case 값3:
        동작
        break;
    case 값4:
        동작
        break;
    default:
        동작
}
```
여기서 default는 비교할 변수가 모든 값과 맞지 않을 경우에 실행된다. **필요에 따라 default도 생략 가능!**

break가 없다면 일치 조건 아래에 있는 모든 case를 다 실행해버림. 

범위를 만족하는 조건식에서는 if, 특정 값을 만족하는 조건식에서는 switch가 좋다.


**주의할 점!! switch 문에서는 반드시 자료형을 맞춰야 함.**
```js
let num = '2';
switch(num){
    case 1: ...
    case 2: ...
    case 3: ...
    default: ...
}

// 위에서는 default가 실행된다.
// 문자열 2라서 case 통과를 못하기 때문. 
```

<br>

## 3. for 문
일정횟수만큼 동작을 반복하게 해주는 제어문이다.
```js
for( 초기화부분 ; 조건 ; 추가동작){
    동작하기
}

// 초기화부분은 딱 한번 맨 처음에만 실행되므로, let i 라고 초기화부분에 선언해줘도 반복선언되지 않는다!
// 단, 초기화부분의 변수는 for문의 로컬 변수기때문에 전역변수처럼 쓰려면 오류가 난다.
for(let i=1; i<=10; i++){
    console.log(i);
}
```

추가 동작 부분을 꼭 채울 필요는 없다.
```js
for(let i=1; i<=10; ){
    console.log(i);
    i++;
}
```

초기화 부분도 꼭 채우지 않아도 된다.
```js
let i = 1;
for(; i<=10; ){
    console.log(i);
    i++;
}
```
<br>

## 4. while 문
for과 비슷하게 반복을 담당하는 제어문이다.
```js
while(조건){
    동작
}

let i= 1;
while(i<=10){
    console.log(i);
    i++;
}
```

while 문은 조건에 비교할 값을 글로벌 변수로 만들 때에 주로 잘 사용함. for문으로도 가능하지만 상황에 따라 while도 쓴다!! 

<br>

## 5. break와 continue
break는 switch 말고도 while이나 for에서도 쓸 수 있다.
```js
while(i<=10){
    console.log(i);
    if(i==7){
        break;
    }
}
```

continue는 해당 조건일 때 동작을 건너뛰고 다음 조건으로 넘어간다.
```js
while(i<=10){
    if(i==7){
        continue;
    }
    console.log(i);
}
```