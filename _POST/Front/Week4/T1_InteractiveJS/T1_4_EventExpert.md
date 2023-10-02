# 🍳 이벤트 심화 🍳
#### Week4 인터렉티브 자바스크립트 / Topic 1 인터렉티브 자바스크립트 / 4. 이벤트 심화

>목차 
>>
1. 마우스 이벤트
2. 키보드 이벤트
3. input 태그 다루기
4. 스크롤 이벤트

<br><br>


## 0. 연습 문제
```css
* {
	box-sizing: border-box;
}

.map {
	display: flex;
	width: 690px;
	height: 500px;
	border: 5px solid #000000;
}

.balcony {
	position: relative;
	width: 120px;
	height: 100%;
	border-right: 5px solid #000000;
	background-color: #fcf3e2;	
}

.room {
	width: 260px;
	height: 100%;
	border-right: 5px solid #000000;
	background-color: #f9edc4;
}

.room-1 {
	position: relative;
	height: 270px;
	border-bottom: 5px solid #000000;
}

.room-1 .door {
	right: -5px;
	bottom: 5px;
	border-radius: 35px 0 0 0;
}

.room-2 {
	position: relative;
	height: 220px;
}

.room-2 .window-2 {
	left: unset;
	right: -6px;
	z-index: 1;
}

.other {
	display: flex;
	flex-flow: wrap;
	width: 300px;
}

.bathroom {
	position: relative;
	width: 155px;
	height: 220px;
	border-right: 5px solid #000000;
	border-bottom: 5px solid #000000;
	background-color: #e5f2f5;
}

.bathroom .door {
	bottom: -5px;
	left: 5px;
	border-radius: 0 35px 0 0;
}

.bath {
	position: relative;
	width: 100%;
	height: 60px;
	background-color: #ffffff;
	border-bottom: 1px solid #000000;
}

.bath::after {
	display: block;
	content: '';
	width: 80%;
	height: 75%;
	position: absolute;
	top: calc(50% - 1px);
	left: calc(50% - 2px);
	transform: translate(-50%, -50%);
	border: 1px solid #000000;
	border-top-left-radius: 30px;
	border-bottom-left-radius: 30px;
}

.bathroom-block {
	position: absolute;
	right: 0;
	bottom: 0;
	width: 25px;
	height: 155px;
	border-left: 1px solid #000000;
}

.bathroom-block::after {
	display: block;
	content: '';
	width: 100%;
	height: 100%;
	position: absolute;
	background-color: #FFFFFF;
}

.sink {
	position: absolute;
	top: 20px;
	right: 20px;
	width: 40px;
	height: 45px;
	background-color: #ffffff;
	border: 1px solid #000000;
	border-radius: 60px;
}

.sink::after {
	display: block;
	content: '';
	width: 70%;
	height: 70%;
	position: absolute;
	top: 50%;
	left: 50%;
	transform: translate(-50%, -50%);
	border: 1px solid #000000;
	border-radius: 30px;
}

.toilet {
	position: absolute;
	bottom: 20px;
	right: 15px;
	width: 60px;
	height: 40px;
	background-color: #ffffff;
	border: 1px solid #000000;
	border-radius: 50%;
}

.utility-room {
	position: relative;
	width: 145px;
	height: 220px;
	border-bottom: 5px solid #000000;
	background-color: #e5e5e5;
}

.utility-room .door {
	bottom: -5px;
	left: 5px;
	border-radius: 0 35px 0 0;
}

.entrance {
	position: relative;
	width: 300px;
	height: 130px;
	background: linear-gradient(90deg, #dfa24d 150px, #fdfbfd 150px);
}

.entrance .door {
	top: 15px;
	right: -35px;
	border-radius: 0 0 35px 0;
}

.entrance .wall {
	right: 0;
	bottom: 0px;
}

.kitchen {
	position: relative;
	width: 330px;
	height: 140px;
	background-color: #dfa24d;
}

.kitchen-block {
	display: flex;
	justify-content: space-around;
	align-items: center;
	width: 190px;
	height: 60px;
	position: absolute;
	right: 0;
	bottom: 0;
	border-top: 1px solid #000000;
	border-left: 1px solid #000000;
	background-color: #ffffff;
}

.kitchen-sink {
	width: 60px;
	height: 40px;
	border: 1px solid #000000;
	border-radius: 10px;
	background-color: #ffffff;
}

.stoves {
	display: flex;
	justify-content: space-around;
	align-items: center;
	width: 70px;
	height: 40px;
	border: 1px solid #000000;
	border-radius: 10px;
	background-color: #ffffff;
}

.stove {
	width: 25px;
	height: 25px;
	border-radius: 50%;
	border: 1px solid #000000;
}

.door {
	width: 35px;
	height: 35px;
	position: absolute;
	border: 1px solid #000000;
	background-color: white;
}

.window {
	display: flex;
	flex-flow: wrap;
	width: 7px;
	height: 150px;
	position: absolute;
	left: -6px;
	top: 50%;
	transform: translateY(-50%);
	background-color: white;
	border-top: 1px solid #000000;
	border-right: 1px solid #000000;
}

.window span {
	display: block;
	width: 50%;
	height: 50%;
	border-bottom: 1px solid #000000;
	border-left: 1px solid #000000;
}

.wall {
	width: 150px;
	height: 5px;
	position: absolute;
	background-color: #000000;
}

span.title {
	position: absolute;
	top: 50%;
	left: 50%;
	transform: translate(-50%, -50%);
	font-size: 20px;
	font-weight: 600;
}
```
```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>효준이네 집</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="map">
    <div class="balcony" data-title="발코니"></div>
    <div class="room">
      <div class="room-1" data-title="침실">
        <div class="door"></div>
        <div class="window">
          <span></span>
          <span></span>
          <span></span>
          <span></span>
        </div>
      </div>
      <div class="room-2" data-title="침실/거실">
        <div class="window">
          <span></span>
          <span></span>
          <span></span>
          <span></span>
        </div>
        <div class="window window-2">
          <span></span>
          <span></span>
          <span></span>
          <span></span>
        </div>
      </div>
    </div>
    <div class="other">
      <div class="bathroom" data-title="욕실">
        <div class="door"></div>
        <div class="bath"></div>
        <div class="bathroom-block">
          <div class="sink"></div>
          <div class="toilet"></div>
        </div>
      </div>
      <div class="utility-room" data-title="다용도실">
        <div class="door"></div>
      </div>
      <div class="entrance" data-title="현관/입구">
        <div class="door"></div>
        <div class="wall"></div>
      </div>
      <div class="kitchen" data-title="주방/식당">
        <div class="kitchen-block">
          <div class="kitchen-sink"></div>
          <div class="stoves">
            <div class="stove"></div>
            <div class="stove"></div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <script src="index.js"></script>
</body>
</html>
```
```js
function showTitle(e) {
	// 비표준 속성 접근법. 
	if(e.target.dataset.title){
		const name = e.target.dataset.title;
		let tag = document.createElement('span');
		tag.setAttribute('class', 'title');
		tag.textContent = name;
		e.target.append(tag);
	} 
}

function removeTitle(e) {
	if(e.target.dataset.title){
		e.target.children[e.target.childElementCount -1 ].remove();
		// e.target.lastElementChild.remove() 해도 된다.
	}
}

const map = document.querySelector('.map');

map.addEventListener('mouseover', showTitle);
map.addEventListener('mouseout', removeTitle);
```


<br>

## 1. 마우스 이벤트

#### 마우스 클릭 이벤트

e.button
* 마우스 왼쪽 버튼: 0
* 마우스 가운데 휠: 1
* 마우스 오른쪽 버튼: 2

마우스 버튼을 클릭한다면
* mousedown mouseup mouseclick 이렇게 3개 이벤트 발생.

마우스 버튼을 빠르게 2번 클릭한다면
* mousedown mouseup mouseclick mousedown mouseup mouseclick mousedbclick 이렇게 7개 이벤트 발생. 

운영체제 별로 함수 호출 순서가 달라질 수 있다. 

```js
function flagUp(e) {
  if(e.button == 0){
    flagBlue.classList.add('up');
  }
  if (e.button == 2){
    flagWhite.classList.add('up');
  }

  // 500 밀리초 뒤에 reset함수를 실행
  setTimeout(reset, 500);

    // 더블클릭할 때
  if (e.type === 'dblclick') {
	btns.className = 'dblclick';
  }
}



// 마우스 우클릭 막기
document.addEventListener('contextmenu', function (event) {
  event.preventDefault();
});
```


#### 마우스 이동 이벤트
* mousemove: 마우스 포인터가 이동할 때
* mouseover: 마우스 포인터가 요소 밖에서 안으로 이동할 때
* mouseout: 마우스 포인터가 요소 안에서 밖으로 이동할 때.
```js
const box = document.querySelector('#box');
function onMouseMove(e){
    console.log('mose is moving');
    console.log(`client: (${e.clientX}, ${e.clientY})`);
    console.log(`page: (${e.pageX}, ${e.pageY})`);
    console.log(`offset: (${e.offsetX}, ${e.offsetY})`);
    
}

// box 내부에서 mousemove 발생 시 onMouseMove 함수 실행.
// 이 때 onMouseMove 함수의 파라미터 e는 마우스이동 이벤트 객체.
box.addEventListener('mousemove', onMouseMove);
```
마우스 이벤트의 속성 중
1. clientX, Y 는 브라우저 내에서 마우스 커서의 xy 좌표를 출력한다. 맨 위, 왼쪽 모서리를 (0,0)이라 한다.

2. pageX, Y는 한 페이지 내에서의 마우스 커서 좌표를 출력한다. client와 엄연히 다르다!


3. offsetX, Y는 이벤트가 발생한 타겟을 기준으로 나타낸다. 타겟의 맨 위 왼쪽 모서리를 (0,0)으로 둔다.

그다음 mouseover과 mouseout은 역시 이벤트 위임이 발생하니 주의하자!
```js
const box = document.querySelector('#box');

function printEventData(e){
    if(e.target.classList.contains('cell')){
        e.target.classList.toggle('on');
    }
}

box.addEventListener('mouseover', printEventData);
box.addEventListener('mouseout', printEventData);
```
참고로
* target: 이벤트 발생한 요소 자체.
* currentTarget: target과 연관하여 같이 이벤트 버블링 캡처링으로 이벤트 발생한 요소들
* relatedTarget: target 직전, 직후 이벤트 발생 요소.

예를 들어 
```js
box.addEventListener('mousevoer', function(e){
    console.log(e.relatedTarget);
    console.log(e.target);
});
```
 target은 box2, relatedTarget은 body라면 body 태그에서  box2 태그로 마우스 커서가 이동함. 

* mouseover과 mouseenter 은 둘다 요소 밖에서 안으로 들어가는 건데, mouseenter은 버블링 안 일어남!!

* mouseout과 mouseleave는 둘다 요소 안에서 밖으로 나가는 건데, mouseleave는 버블링 안 일어남!!

* 즉, mouseenter, mouseleave는 
    * 버블링이 안 일어난다.
    * 자식 요소의 영역을 계산하지 않는다. 자식 안으로 들어가도 이벤트 핸들러가 동작하지 않는다. 

<br>

## 2. 키보드 이벤트

#### 키보드 이벤트 종류
* keydown: 키 누른 순간
* keypress: 키 누른 순간 (단, shift, esc 같은 기능 키에서는 작동 안함.)
* keyup: 키 눌렀다 뗀 순간

* 키 하나만 꾸욱 누르고 있으면 keydown만 연속 발생하고 keypress는 작동 안함. 가끔 한글 키에선 keypress가 발생 안할 수도 있고 문제가 있으니 keydown이 더 선호된다!! 
* 그치만 keypress가 더 선호되는 상황도 있다.

#### 키보드 이벤트의 속성
* e.key: 키 값
* e.code: 키보드에서 물리적 위치

예를 들어 t를 누를 때와 T를 누를 때 key 값은 달라도 code 값은 같다!! 

```js
function sendText(e){
	if(!e.shiftKey && (e.key === 'Enter')){
		sendMyText();
		e.preventDefault();
	}
}

```

<br>

## 3. input 태그 다루기
checkbox, text, radio 등 여러 input이 있고 그 인풋에 관련된 여러 이벤트가 있다.


1. focus와 관련된 이벤트
* 사용자의 키보드나 마우스 동작에 반응하는 특징. 
* 일반 div 태그같은 곳에는 없는 이벤트.

```js
// focusin: 요소에 포커스 되었을 때
// focusout: 요소에 포커스 빠져나갈 때
// focus: 요소에 포커스 될 때 (버블링 없다!!)
// blur: 요소에 포커스 빠져나갈 때 (버블링 없다!!)

const el = document.querySelector('#username');
function printEventType(e){
	console.log("type: ", e.type);
	console.log("target: ", e.target);
	console.log("--------------");
}

el.addEventListener('focusin', printEventType);
```

2. input 이벤트
* 값을 입력하는 순간 발생하는 이벤트 
* 값이 입력돼야 발생하므로 esc 같은 특수키에선 발생 안한다!! 이게 키보드 이벤트와의 차이점. 
```js

```

3. change 이벤트
* 요소의 값이 변했을 때 발생.
* 이벤트 시작 전 값과 이벤트 완료됐을 때의 값 사이에 차이가 있을 때만 발생한다!! 
* 기본적으로는 그냥 input 이벤트만 발생하다가 focus out이 되기 직전 빠져나갈 때 입력이 완료됐다고 인식되면서 change 이벤트 발생.
* 엔터를 눌러서 focus out 안하고 change 이벤트 발생시킬 수도 있다. 

<br>

## 4. 스크롤 이벤트

스크롤을 내릴 때 발생한다.

scrollY 속성을 통해 얼만큼 스크롤 내렸는지 알 수 있다. 이걸 써서 어디 쯤 왔을 때 광고를 띄워준다든가 하는 식으로 구현할 수도 있다. 
```js
// Scroll 이벤트
let lastScrollY = 0;

function onSroll() {
  const nav = document.querySelector('#nav');
  const toTop = document.querySelector('#to-top');
  const STANDARD = 30;
  
  if (window.scrollY > STANDARD) { // 스크롤이 30px을 넘었을 때
    nav.classList.add('shadow');
    toTop.classList.add('show');
  } else { // 스크롤이 30px을 넘지 않을 때
    nav.classList.remove('shadow');
    toTop.classList.remove('show');
  } 

	if (window.scrollY > lastScrollY) { // 스크롤 방향이 아랫쪽 일 때
    nav.classList.add('lift-up');
  } else { // 스크롤 방향이 윗쪽 일 때
    nav.classList.remove('lift-up');
  }

  lastScrollY = window.scrollY;
}

window.addEventListener('scroll', onSroll);
```

<br>
