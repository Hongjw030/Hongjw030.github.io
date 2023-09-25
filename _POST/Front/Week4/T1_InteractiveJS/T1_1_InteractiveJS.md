# 🥧 인터랙티브 자바스크립트 시작 🥧
#### Week4 인터렉티브 자바스크립트 / Topic 1 인터렉티브 자바스크립트 / 1. 인터렉티브 자바스크립트 시작하기

>목차 
>>[1. js](#1-js)<br>
[2. id로 태그 선택](#2-id로-태그-선택)<br>
[3. class로 태그 선택](#3-class로-태그-선택)<br>
[4. 유사 배열](#4-태그-이름으로-태그-선택)<br>
[5. 태그 이름으로 태그 선택](#5-css-선택자로-태그-선택)<br>
[6. css 선택자로 태그 선택](#6-이벤트와-버튼-클릭)<br>
[7. 이벤트와 버튼 클릭](#7
)<br>



<br><br>

## 1. js
js는 하나의 프로그래밍 언어이다!!

웹을 더 다채롭게 쓸 수 있게 하려고 개발됐지만, 범용성이 좋아 여러 분야에서 활용된다.


<br> 

## 2. id로 태그 선택
documnet라는 객체에 getElementById() 라는 함수가 있다.
```javascript
document.getElementById("아이디이름");
```
html을 작성할 때 태그에 준 id 값을 적는다. 

```html
<div id ="myNumber"> 1 </div>
```
```js
const num = document.getElementById("myNumber");
console.log(num);
```
만약 없는 id에서 값을 가져오려 하면 null 값이 출력된다. (undefined 아님!)


<br> 

## 3. class로 태그 선택
id는 고유 태그 하나만 선택하기에, 여러 태그를 동시에 선택하려면 class를 활용하자.
```js
cont tags = documnet.getElementsByClassName('클래스이름');
console.log(tags);
```
class는 여러 개니까 class 값들을 가져와서 배열처럼 대괄호로 묶어 값을 출력한다.

**그치만!! 진짜 배열은 아니다!!**

배열 함수인 splice, push 등의 메소드는 못 쓰기 때문이다. 대신 for of 문이나 tags.length 를 쓰는 건 괜찮다. 

이렇게 class 이름을 통해 값을 가져오면, html에서 각 태그들이 어디 있든간에 무조건 위에 쓰인 놈이 0번이다. 
```js
for let tag of tags{
    console.log(tag);
}
console.log(tag[1]);
```

* 만약 class를 한 태그에만 주어졌다 해도 class로 js 호출하면 배열 형태로 들어온다.

* 만약 없는 class의 값을 불러오면 null, undefined도 아니고 그냥 비어있는 htmlCollection 배열이 출력된다. 이렇게 빈 배열은 null과 === 비교하면 false가 뜨고, .length를 보면 0이 출력된다.

* 이렇게 배열과 형태는 비슷하지만 배열은 아닌 것을 유사배열, array like object라고 한다.

<br> 

#### 유사 배열이란?
배열과 유사하지만 배열은 아닌 객체.

1. 숫자 형태의 indexing이 가능함. tags[0], tags[1] 이렇게 불러올 수 있음.
2. length 프로퍼티가 있음. tags.length 가능.
3. 배열의 기본 메소드인 push, splice 사용 불가!!
4. Array.isArray(tags) 출력시 false 값 나옴.

**유사배열은 생각보다 다양하며 어떤 유사배열은 for of 문도 못 쓸 수도 있으니 주의하자.**



<br> 

## 4. 태그 이름으로 태그 선택
클래스처럼 여러 태그가 선택되므로 html collection 형태로 리턴된다. 
```js
const btns = document.getElementsByTagName('button');
const allTags = document.getElementsByTagName('*');
```


<br> 

## 5. css 선택자로 태그 선택
위에서는 html 태그에 준 속성들로 값을 받아왔기 때문에 document.getElementBy... 함수를 썼다면, 그거보다 간단한 게 css 선택자다.

```html
<div id ="myNumber"> 1 </div>
```
```js
const num = document.querySelector('#mynumber');

// 클래스 선택하면 node list 형태로 반환.
document.querySelectorAll('.btn-class');

// 만약 클래스 이름으로 querySelector을 쓰면 가장 위에 있는 0번 인덱스의 요소만 반환하고 html collection 형태는 반환 안 함!!
document.querySelector('.btn-class');

// 이렇게도 활용 가능.
console.log(document.querySelectorAll('#list li'));
```

* document.querySelectorAll('.btnclass')[0] 과 document.querySelector('btnclass') 는 같은 거다.



* querySelectorAll로 없는 클래스를 불러오면 그냥 비어있는 node list가 반환되지, null이나 undefined가 반환되지 않는다!!

<br> 

## 6. 이벤트와 버튼 클릭
웹페이지에서 일어날 수 있는 일을 이벤트라 한다. 페이지 스크롤하기, 버튼 누르기, 마우스 클릭하기 등!

```html
<html>
    <head></head>
    <body>
        <button id = 'mybtn'>
            click
        </button>
        <script src="index.html"></script>
    </body>
</html>
```
```js index.js
const btn = document.querySelector('mybtn');
btn.onclick = function(){
    console.log('hello!');
}
```
**지금 이 코드는 js로 해당 객체의 onclick 프로퍼티에 함수를 등록한 것이다!!**

 이렇게 태그를 선택해서 프로퍼티 자체에 함수를 할당할 수 있다. 

 * 이렇게 무슨 이벤트에 뭘 할지 정하는 걸 이벤트 핸들링이라 한다.

 * 구체적으로 이벤트 핸들링이 일어나면 무슨 동작을 할지 코드로 나타낸 함수 부분이 이벤트 핸들러
<br> 

