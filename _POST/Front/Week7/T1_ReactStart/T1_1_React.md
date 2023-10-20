# 🍑 리액트 시작하기 🍑

#### Week7 리액트 / Topic 1 리액트 웹개발 시작 / 1. 리액트 시작하기

> 목차
>
> > 1. 리액트 셋팅
> > 2. 프로젝트 셋팅
> > 3. 인덱스 파일
> > 4. jsx
> > 5. 프래그먼트
> > 6. 컴포넌트
> > 7. props
> > 8. children
> > 9. state
> > 10. 컴포넌트 심화
> > 11. 코드 정리
> > 12. 리액트가 렌더링하는 방식
> > 13. 인라인 스타일
> > 14. css 클래스 네임
> > 15. 디자인 적용 방법

<br><br>

## 1. 리액트 셋팅

1. Node.js 설치하기. 기본적으로 js는 브라우저 내에서만 실행 가능하지만, node.js를 통해 js를 브라우저 밖에서도 실행 가능하게 할 수 있다. node.js는 프론트에서는 개발을 보조하는 정도이니 가볍게 익혀두자. 여기서는 window 64bit 운영체제에서 LTS 버전을 다운받았다.

2. Node.js가 잘 설치되었는지 확인하기. cmd 창에서 node -v 명령어를 입력하면 node.js의 버전 정보가 나온다!

3. node package manager 확인하기. 이걸 줄여서 npm이라 하는데, cmd 창에 npm -v 를 통해 버전을 확인하자.

<br>

## 2. 프로젝트 셋팅

1. 프로젝트 폴더 만들기. 먼저 프로젝트를 담을 디렉토리를 생성한다. 여기서는 `hello_react` 라는 이름으로 지었다. 참고로 디렉토리 이름은 대문자는 쓸 수 없다.

2. 리액트 프로젝트를 만드는 방법은 여러가지가 있는데, 그 중 하나인 create-react-app 도구를 사용하자.

3. 우선 vs 코드로 폴더를 열고, 폴더의 terminal에 `npm init react-app .` 명령어 입력. 그러면 프로젝트를 위한 기본적인 파일들이 생성된다.

4. 이후 `npm run start` 명령어를 입력하면 자동 생성된 파일들을 실행할 수 있다. 그러면 디폴트 웹사이트가 자동으로 열린다!! 우리가 파일을 수정할 때마다 자동으로 바로바로 반영해주는 기능이 있어 '개발모드를 실행했다' 라고 표현하기도 한다.

이제 이 웹사이트를 기반으로, 우리가 코딩을 하면 된다.

#### 그렇다면 어디에 index.html을 작성하고 꾸밀까?

우선 자동으로 실행된 localhost:3000 페이지는 src 파일의 App.js 파일이다. 신기하게도 html 파일이 아니라 js로 웹 페이지를 띄우는데, 리액트는 js 코드 내에 html 태그를 섞어쓰는 jsx 문법을 사용한다.

따라서 해당 사이트를 수정하면 된다!!

5. 이 개발모드를 끝내기 위해선 터미널 창에서 ctrl + c를 누르면 된다.

#### 개발자 모드

보통 f12를 눌러서 개발자 모드로 들어가 코드를 확인하는데, 리액트 코드를 확인하기 위해서는 리액트 개발자도구를 사용해야 한다. 리액트 개발자 도구는 크롬 확장 프로그램이므로 설치해주어야 한다.

react app 개발자 도구를 설치한 후 f12로 열어서 component 탭으로 가면 확인 가능!!

컴포넌트는 리액트 개발의 가장 기본적인 단위이므로 잘 알아두자.

#### 자동으로 생성된 파일들 알아보기.

1. public 디렉토리 정리하기:

먼저 public 디렉토리에는 index html과 그 외 부속품이 있는데 index.html 빼곤 다 필요없다!! 그리고 index.html에서도 body 내부에선 root 라는 id 값을 가진 div 태그 빼곤 다 지워도 된다

2. src 디렉토리 정리하기:

여기서도 index.js 빼곤 필요가 없다. App.js 나 css도 모두 삭제하자. index.js 파일에선 아래 코드를 붙여보자.

```js
import ReactDOM from "react-dom/client";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<h1>안녕 리액트!</h1>);
```

이 이후로 `npm run start` 를 하면 내가 바꾼 index.html대로 잘 출력된다.

참고로 우리가 다른 곳에서 리액트 프로젝트를 다운받아서 쓰려면, 압축을 푼 이후 해당 디렉토리의 터미널에서 `npm install` 명령어를 통해 먼저 설치를 해야 한다. 그 이후에 `npm run start`를 하자!

<br>

## 3. 인덱스 파일

1. index.html

index.html은 웹브라우저에서 가장 먼저 실행되는 파일이다. 그런데 리액트에서 html 용량은 생각보다 작다. 왜냐면 리액트는 jsx 문법을 쓰기 때문에, 보통 필요한 코드들을 js 파일에 적어두는 편이라 html은 상대적으로 간소하다!

2. index.js

index.html이 열린 이후에 바로 실행되는 파일로, 리액트 코드들 중 가장 먼저 실행되는 파일이다.

여기서 `ReactDom.render();` 메소드를 사용하는데, 리액트에서는 render 메소드로 html 태그를 만들어준다. (우리가 createElement 로 html DOM 트리에 html 태그를 만들었듯이.)

그래서 render 메소드 내에서

- 첫번째 인자로는 html 태그를 그대로 작성해준다! 이걸 jsx 문법이라 한다.이 첫번째 인자를 통해 html 요소를 새로 생성한다.
- 두 번째 인자로는 html 내 태그를 가져오는 js 문법을 사용한다. 첫 번째 인자로 만든 html 태그를 두 번째 아규먼트 값에 집어넣는 방식이다.

참고로 reactDom.render 메소드는 index.js 파일에서 한 번만 사용하므로 굳이 막 사용법을 외울 필요는 없고 이해하면 된다.

<br>

## 4. jsx

리액트는 jsx 문법을 사용한다고 했는데, 이는 간단하게 html와 js를 쓰게 해주는 js 확장 문법이다.

그래서 jsx에서는 js 코드도 함께 작성할 수 있다.

그리고 html 문법을 사용할 수도 있다!! 그런데, 완전 똑같이 html 문법을 사용은 못한다.

#### jsx에서 사용 못하는 html 문법은?

- class: html에서 class는 css의 class를 적용하는 속성이지만, react에선 객체를 만들기 위해 class 키워드를 사용하기 때문이다. 만약 jsx에서 css class 속성을 주려면 className 이라고 설정해야 한다.

```jsx
class Dice {}

ReactDOM.render(
  <p className="title-name">안녕하세요!</p>,
  document.getElementById("root")
);
```

- for: for은 label 태그에서 input 태그와 묶어주기 위해 사용되는 속성이다. 그런데 js 문법 중에 for 문이 있기 때문에 사용하지 못한다. 만약 jsx에서 html의 for 속성을 명시하려면, htmlFor 이라 작성해야 한다.

```jsx
ReactDOM.render(
  <form>
    <label htmlFor="name">이름</label>
    <input id="name" type="text" />
  </form>,
  document.getElementById("root")
);
```

- render 메소드 안에 들어갈 첫번째 인자는 반드시 하나의 html 태그이다. 여러 html 태그를 넣으면 안됨. 그래서 여러 태그를 넣고 싶다면, 하나의 box tag로 감싸야 한다.

```jsx
// 이런 거 불가능!!
// ReactDOM.render(
//     <p></p>
//     <p></p>
//   document.getElementById("root")
// );

// 이렇게 해야 함.
ReactDOM.render(
    <div>
        <p></p>
        <p></p>
    </div>
  document.getElementById("root")
);
```

<br>

## 5. 프래그먼트

render 메소드 안에 들어갈 첫 인자는 1개 뿐이라 계속 box로 묶어줘야 한다는 불편함이 있다. 이렇게 불필요한 박스가 아니라, 그냥 요소들만 넣어주기 위해서는 fragment 태그를 사용하자. 이 태그를 쓰면 자동으로 react 패키지에서 Fragment 가 임포트된다.

```jsx
import ReactDOM from 'react-dom';
import {Fragment} from 'react';

ReactDOM.render(
    <fragment>
        <p></p>
        <p></p>
    </fragment>
  document.getElementById("root")
);
```

근데 임포트도 귀찮고, fragment 라는 이름도 길어서 보통은 이렇게 쓴다.

```jsx
// 임포트 안함!!
ReactDOM.render(
    //이름도 작성 안함!!
    <>
        <p></p>
        <p></p>
    </>
  document.getElementById("root")
);
```

#### 그렇다면 jsx 코드에서 js 코드는 어떻게 쓸 수 있을까?

별 거 없다. 그냥 js 파일처럼 쓰면 된다.

```jsx
import ReactDOM from "react-dom";

const name = "hongjw";
// html 요소 내부에 js 코드 쓰기.
ReactDOM.render(
  <p>
    나의 이름은 {name} 이다. 대문자로 바꾸면 {name.toUppderCase()} 이다.
  </p>,
  document.getElementById("root")
);
```

```jsx
// js 코드 분리하기

import ReactDOM from "react-dom";

const name = "hongjw";
const bigName = name.toUpperCase();
const imgUrl = "url 주소....";

function buttonHandleClick() {
  alert("버튼 누름!");
}

ReactDOM.render(
  <>
  <h1>제목: {name} </h1>
  <button onClick={buttonHandleClick}>확인</button>
  <img src={imgUrl} alrt="사진." />,
  </>
  document.getElementById("root")
);
```

이렇게 중괄호 안에 js 변수와 코드를 넣어서 쓸 수 있다.

참고로 리액트의 jsx 문법에선 addEventListener보단 요소의 속성값으로 이벤트 핸들러를 등록해준다.

중괄호 안에는 표현식만 쓸 수 있으므로 if문, for 문혹은 함수 선언 같은 문장은 넣을 수 없다!!

#### 정리하자면...

1. jsx 문법은 js의 확장 버전이며, html 과는 class 이름이라든가 for 속성 같은 게 이름이 조금씩 다르다.
2. jsx는 낙타체를 사용하지만, 비표준 속성을 다룰 때 쓰는 data-\* 속성은 기존 html 문법 그대로 하이픈으로 써야 한다!!
3. render 메소드 첫번째 인자로 넣을 html 태그는 fragment로 감싸주자.
4. 자바스크립트 표현식을 넣을 때엔 중괄호로 감싸주자.

<br>

## 6. 컴포넌트

리액트 엘리먼트는 리액트 객체라 하는데, 이걸 ReactDOM에서 render 메소드로 전달하면 리액트가 객체를 해석해서 html로 렌더링하는 것.

```jsx
const element = <h1>안녕 리액트!</h1>;

// object 출력
console.log(element);

// 함수로 리액트 엘리멘트를 전달할 수도 있다.
function Hello() {
  return <h1>안녕 리액트!</h1>;
}

const elements = (
  <>
    <Hello />
    <Hello />
    <Hello />
  </>
);
```

이렇게 리액트 엘리먼트를 함수로 전달할 때, 이 함수를 리액트 컴포넌트라고 부른다.

- 반드시 리액트 컴포넌트 이름은 첫 글자가 대문자여야 한다.
- 리액트 컴포넌트는 반드시 jsx 문법으로 만든 리액트 엘리먼트를 리턴해야 한다.

참고로 리액트에서 이미지를 불러올 때엔 아래처럼 import 문으로 해야 한다.

```jsx
import diceBlue01 from "./assets/dice-blue-1.svg";

function Dice() {
  return <img src={diceBlue01} alt="주사위" />;
}

export default Dice;
```

만약 리액트 컴포넌트의 리턴문에 여러 줄을 쓰고 싶다면 소괄호로 묶어주면 된다.

```jsx
import Dice from "./Dice.js";

function App() {
  return (
    <div>
      <Dice />
    </div>
  );
}

export default App;
```

이렇게 jsx 문법으로 작성한 요소는 js 객체가 되어 리액트 객체, 리액트 엘리먼트라 부른다. 이 리액트 엘리먼트를 reactDOM.render 함수의 인자로 전달하면 리액트가 이 인자를 html 형태로 해석해서 브라우저 화면에 띄워주는 것.

그리고 리액트 컴포넌트는 리액트 엘리먼트를 자유롭게 다루기 위한 문법 중 하나. 컴포넌트를 만드는 가장 쉬운 방법은 js 함수를 활용하는 것인데, 위에서처럼 function 키워드로 함수를 만들고 그의 return으로 태그를 전달하는 것.

이 컴포넌트로 모듈 문법을 활용하여 파일들을 독립적으로 관리하고 컴포넌트의 특성에 집중하여 코드를 작성할 수 있다!!

<br>

## 7. props

앞에서 html 태그에 속성을 넣으려면 중괄호를 쓴다고 배웠다.

그런데 html 태그 말고 리액트 컴포넌트에도 속성을 넣을 수 있다!! 이렇게 컴포넌트에 전달된 속성을 props라고 부른다. 이 rpops를 활용하면 컴포넌트에 전달되는 props 값에 따라 컴포넌트가 다양하게 랜더 될 수 있다.

속성은 function의 파라미터로 적어야 한다.

```jsx
// Dice.js
function Dice(props){
  const diceImg = props.color === 'red'? diceRed:diceBlue;
  return <img src={diceImg} alt="dice" />;
}

// App.js
function App(){
  return ()
  <div>
    <Dice color="blue" />
  </div>;
}
```

참고로 구조분해를 써서 여러 속성값을 다룰 수도 있다.

```js
const DICE_IMGS = {
  blue: [diceBlue1, diceBlue2, diceBlue3, diceBlue4, diceBlue5, diceBlue6],
  red: [diceRed1, diceRed2, diceRed3, diceRed4, diceRed5, diceRed6],
};

// 구조분해 안 한 경우
function Dice(props) {
  const src = DICE_IMGS[props.color][props.num - 1];
  const alt = `${props.color}: ${props.num} 입니다.`;
  return <img src={src} alt={alt} />;
}

// 구조분해 한 경우 + 옵셔널 값도 줌.
function Dice({ color = "blue", num = 1 }) {
  const src = DICE_IMGS[color][num - 1];
  const alt = `${color}: ${num} 입니다.`;
  return <img src={src} alt={alt} />;
}
```

그런데 이렇게 num 속성에는 숫자 값이 들어갈텐데, 리액트 컴포넌트의 속성에 숫자를 넣으면 에러가 난다. 숫자는 반드시 중괄호로 감싸주자.

```jsx
function App() {
  return (
    <div>
      <Dice color="red" num={2} />
    </div>
  );
}
```

<br>

## 8. children

리액트 엘리먼트의 props 는 위에처럼 우리가 직접 만드는 것도 있지만, children이라는 props도 존재한다. children은 컴포넌트의 자식들을 값으로 갖는 props이다.

1. 위에서 배운 대로 prop 쓰려면..

```js
//Button.js
function Button({ text }) {
  return <button>{text}</button>;
}

export default Button;
```

```js
// App.js
import Dice from "./Dice.js";
import Button from "./Button.js";

function App() {
  return (
    <>
      <div>
        <Dice />
      </div>
      <div>
        <Button text="throw" />
        <Button text="away" />
      </div>
    </>
  );
}

export default App;
```

2. 위에처럼 해도 되지만, 지금 text는 button의 자식이기 때문에 이 경우 children을 활용하는 게 더 직관적이다.

```js
//Button.js
function Button({ children }) {
  return <button>{children}</button>;
}

export default Button;
```

```js
// App.js
import Dice from "./Dice.js";
import Button from "./Button.js";

function App() {
  return (
    <>
      <div>
        <Dice />
      </div>
      <div>
        <Button>throw</Button>/>
        <Button>away</Button> />
      </div>
    </>
  );
}

export default App;
```

이 떄 children으로 들어갈 값은 문자열 뿐만 아니라 다른 컴포넌트나 html 태그도 가능하다.

#### 정리하자면!!

props는 컴포넌트에 주는 속성이고, 이 props를 통해 다양하게 활용할 수 있다. props는 객체이기 때문에 구조분해 문법을 사용할 수 있음. 그리고 props 중에서도 children을 잘 쓰면 직관적인 코드 짜기가 가능하다!!

<br>

## 9. state

리액트에선 코드로 함수를 구현해, 예를 들어서 버튼을 누르면 숫자가 카운트되고 이미지가 바뀌는 식으로 속성값을 변화시킬 수 있다. 이는 리액트의 state라는 기능을 활용해서 가능하다!!

state는 리액트에서 변수 같은 개념으로, state를 바꾸면 리액트가 알아서 화면을 새로 렌더링해준다.

state를 쓰려면 import react를 통해 useState 라는 함수를 불러와야 한다.

```js
import { useState } from "react";

function App() {
  //먼저 useState 함수의 첫 파라미터로 초기값을 전달한다.
  const [num, setNum] = useState(1);
  // 배열의 형태로 요소 두 개를 리턴하므로 이렇게 구조분해 문법 작성.
}
```

useState 가 전달하는 첫 요소는 state 값이다. 현재 변수의 값을 나타낸다.
두 번째 요소는 setter 함수이다. 이 함수를 호출할 때 파라미터로 전달하는 값으로 State 값이 변경된다. state 값을 변경할 때엔 state 자체에 값을 넣어주는 게 아니라 setter 함수로 설정해야 한다. 그래서 변수도 const 키워드로 선언하고, 함수 이름은 보통 set변수이름 이렇게 짓는다.

리액트는 state 값이 변경될때마다 화면을 새로 렌더링하기때문에 화면을 바꿀 때엔 state를 잘 활용하자.

주사위를 던지는 식으로 구현한 js 파일

```js
import {useState} from 'react';
import Button from './Button';
import Dice from './Dice';

function random(n){
  return Math.ceil(Math.random()*n);
}

function App(){
  const [number, setNumber] = useState(1);

  const handleRollClick = ()=>{
    const nextNum = random(6);
    setNum(nextNum);
  };
  const handleClearClick = ()=>{
    setNum(1);
  };
  return (
    <div>
      <div>
        <Button onClick = {handleRollClick}>던지기</Button>
        <Button>처음부터</Button>
      </div>
      <Dice color ="red" num={number}>
    </div>
  );
}
```

참고로 우리가 구현한 Button 컴포넌트가 onClick 속성을 받을 수 있게, 버튼 컴포넌트의 인자에 onClick prop 를 넣어줘야 한다.

```js
//Button.js

function Button(children, onClick) {
  return <button onClick={onclick}>{children}</button>;
}
```

#### 참조형 state

배열이나 객체 같은 state를 참조형 state라 한다. 이걸 어떻게 다룰까.
예를 들어 주사위를 던지고 그 수가 계속 더해져서 sum을 출력하게 해보자.
그리고 이때껏 나왔던 수를 배열로 정리해서 한꺼번에 모두 보여주게 해보자.

```js
import {useState} from 'react';
import Button from './Button';
import Dice from './Dice';

function random(n){return Math.ceil(Math.random()*6);}
function App(){
  const [num, setNum] = useState(1);
  const [sum, setSum] = useState(0);
  const [gameHistory, setGameHistory] = useState([]);

  const handleRollClick =()=>{
    const nextNum = random(6);
    setNum(nextNum);
    setSum(sum + nextNum);
    //gameHistory.push(nextNum);
    //setGameHistory(gameHistory);

    // push를 해서 배열 자체를 주지 않는 이유!1 배열이 참조형이라 그렇다.
    // gameHistory 변수엔 배열의 주소값이 담겨있어 변함이 없다. 그래서 배열에 push로 원소를 추가해도 새로 render되지 않아 문제가 생긴다. 그래서 배열같은 참조형을 다룰 떄엔 아예 새 객체를 만들어 setter에게 새 객체를 넘겨줘야 한다.
    // 가장 쉬운 새 객체 만들기 방식은 spread 문법 활용이다.
    setGameHistory([...gameHistory, nextNum]);
  };

  const handleClearClick = ()=>{
    setNum(1);
    setSum(0);
    setGameHistory([]);
  };
  return (
    <div>
      <div>
        <Button onClick = {handRollClick}>던지기</Button>
        <Button onClick = {handleClearClick}>처음부터</Button>
      </div>
      <div>
        <Dice color="blue" num={num}></Dice>
        <p>{sum}</p>
        <p>{gameHistory.join(', ')}</p>
      </div>
    </div>>
  )
}
```

참고로 배열의 join 메소드는 인자 값을 배열의 각 요소 사이에 넣어서 하나의 문자열로 만들어줌.

<br>

## 10. 컴포넌트 심화

이렇게 컴포넌트를 쓰면 뭐가 좋은 것일까? 리액트는 컴포넌트 개발이라 할 정도로 핵심 개념인데, 이렇게 하면 반복적인 일이 줄어든다. 미리 만들어둔 부품을 여러 번 쓸 수 있으니까!! (재사용) 그리고 컴포넌트 하나만 고치면 되니까 유지보수가 쉽다. 그리고 일을 쉽게 나눌 수가 있다. 여러 명이 일을 나눠서 하고 그걸 합치기만 하면 되니까.. 협업성이 높아짐!!

이렇게 컴포넌트를 사용하는 것은 여러 분야에 쓰인다. 리액트 말고 다른 공장들도 제품을 만들 때 보통 컴포넌트 단위로 만든다.

#### 컴포넌트로 새로운 비슷한 컴포넌트 만들기

예를 들어 주사위 던지기 게임에서 내 주사위 던지기 컴포넌트가 상대방이랑 ui도 비슷하고 기능도 비슷하다면 결국 내 컴포넌트를 수정해서 비슷하게 하나 더 만들면 되는 것이다. 즉, 컴포넌트를 재사용하자는 것!!

어떻게하냐면!!

그냥 App() 컴포넌트를 복사해서 새로운 이름으로 파일 하나 만들고, 그거 자체를 컴포넌트로 쓰면 된다..

아래 코드는기존 App 컴포넌트를 Board 파일로 옮긴다음 가져온 것이다.

```js
function App() {
  return (
    <div>
      <Board name="me" color="blue"></Board>><Board
        name="you"
        color="red"
      ></Board>>
    </div>
  );
}
```

그런데 Board 컴포넌트 둘이 공유하는 하나의 state가 있을 때엔 App 에서 state를 설정하고 Board가 상속받게 해줘야 한다.

예를 들어 버튼 하나만 눌러도 Board me와 you 둘 다 동시에 바뀌게 하려면? 아래처럼 코드를 짠다. 이 때 이렇게 자식 컴포넌트의 state를 부모 컴포넌트에게 줘서 상속받게 하는 것을 state lifting이라 한다.

이벤트 핸들라 함수와 필요한 import 같은 것들도 다 부모 (App) 컴포넌트로 가져와서 쓸 수 있다.

```js
function App() {
  const [num, setNum] = useState(1);
  const [sum, setSum] = useState(0);
  const [gameHistory, setGameHistory] = useState([]);
  const [otherNum, setOtherNum] = useState(1);
  const [otherSum, setOtherSum] = useState(0);
  const [otherGameHistory, setOtherGameHistory] = useState([]);

  return (
    <div>
      <Board name="me" color="blue"></Board>><Board
        name="you"
        color="red"
      ></Board>>
    </div>
  );
}
```

<br>

## 11. 코드 정리

위의 코드를 보면 state가 너무 많아서 보기 힘들다. 그래서 적은 수의 state만 가지고 다른 것들을 계산해낼 수 있게 코드를 정리하자.

```js
function App() {
  const [gameHistory, setGameHistory] = useState([]);
  const [otherGameHistory, setOtherGameHistory] = useState([]);

  return (
    <div>
      <Board name="me" color="blue"></Board>><Board
        name="you"
        color="red"
      ></Board>>
    </div>
  );
}
```

<br>

## 12. 리액트가 렌더링하는 방식

리액트는 state가 바뀔 때마다 새로 렌더링한다고 했다.

state 값이 바뀔 때마다 App 함수를 새로 호출해서 새 state 값이 적용된 return 값을 받는 것이다.

그런데 이런 방법을 쓰면, text 값이나 input 값 같은 거 말고 button 같이 딱히 변화가 없는 요소들도 같이 새로 렌더링돼서 자원적인 낭비가 있다. 그래서 나타난 게 virtualDOM 가상 DOM 이라는 개념이다.

리액트는 엘리먼트를 새로 렌더링할 때 바로 실제 DOM 트리에 반영하는 게 아니라 일단 메모리 상에만 존재하는 영역인 virtual dom에 적용한다. 그다음 리액트는 virtual dom과 실제 dom 트리를 비교해서 변한 부분만 찾아 그 부분만 실제 dom 노드를 변경하는 것이다.

이렇게 가상 돔을 쓰면 좋은점

1. 개발자가 dom을 신경쓰지 않아 단순하고 깔끔하게 코드를 짤 수 있다. 기존에 우리가 배웠던 js로 dom 구조 찾아서 짜는 건 막 nextSiblingElement 찾고 innerText 바꾸고 뭐시기 해야 했는데 리액트 쓰면 dom 신경 안 쓰고 그냥 무슨 데이터를 보여줄지만 신경쓰면 된다.
2. 변경사항이 있다고 바로 변경하는 게 아니라 수정사항을 어느정도 모아서 한번에 실제 dom에 반영해주는 식으로 자원 낭비를 막을 수 있다.

이렇게 가상 돔을 쓰면 효율적으로 화면 처리할 수가 있어 리액트 말고도 다른 분야에서도 쓰인다.

<br>

## 13. 인라인 스타일

컴포넌트에 디자인을 입히는 방법 중 인라인 스타일을 사용하는 법을 알아보자.
리액트에서 스타일 정하려면 속성값으로 지정하는 게 아니라 style 객체를 만들어야 한다.

이 때 style 객체에서 속성 이름은 낙타체로 하이픈 없이 작성해야 한다.

```js
const style = {
  //속성: 값
  backGroundColor: "pink",
};
function Button({ children, onClick }) {
  return (
    <button style={style} onClick={onClick}>
      {children}
    </button>
  );
}

export default Button;
```

style도 객체 형식이기 때문에, 공통 스타일을 묶어서 개별 스타일 안에 spread로 작성할 수 있다.

```js
const commonStyle = {
  padding:: "14px 26px",
  outline: 'none',
  cursor: 'pointer',
}

const redStyle={
  ...commonStyle,
  backgroundColor: "red",
}
const blueStyle={
  ...commonStyle,
  backgroundColor: "blue",
}

function Button({children, onClick, color}){
  const style = color==="red"?redStyle:blueStyle;
  return(
    <button style={style} onClick={onClick}>
      {children}
    </button>
  );
}
```

<br>

## 14. css 클래스 네임

이번에는 인라인으로 스타일 적용하지 말고 css 클래스를 이용해서 스타일을 입혀보자. js에서 css 파일을 임포트하는 기능을 쓰면 된다.

```css
.Button {
}
.Button.blue {
}
.Button.red {
}
```

```js
// index.js
import ReactDOM from "react-dom";
import App from "./App";
import "./index.css";

ReactDOM.render(<App />, document.getElementById("root"));
```

컴포넌트에도 css 파일 임포트해서 쓰면 된다.

```js
//Button.js

import "./Button.css";

function Button({ children, onClick, color = "blue", clasSName = "" }) {
  // 이렇게 하면 class 명으로 Button, color, clasSName 이렇게 3개 들어감.
  const classNames = `Button ${color} ${className}`;
  return (
    <button className={classNames} onClick={onClick}>
      {children}
    </button>
  );
}
```

참고로 margin 같은 외부 스타일 요소는 app 컴포넌트에다 주자.
<br>

## 15. 디자인 적용 방법 정리.

1. 이미지 불러올 때엔 import 구문을 통해 주소 가져와서 src 속성의 값으로 넣어준다.

```js
import backImg from "./assets/dice.png";

function Dice() {
  return <img src={diceImg} alt="" />;
}

export default App;
```

2. css 파일 불러올 땐 from 키워드 없이 그냥 import 만.

3. 클래스 이름 사용해서 css 스타일 적용하는데, className 속성에 문자열로 클래스 이름 넣어주면 된다. 재사용성을 위해 className 인자를 부모 컴포넌트에서 받으면 더 좋다!!

```js
import diceImg from "./assets/dice.png";
import "./Dice.css";

function Dice({ className = "" }) {
  const classNames = `Dice ${className}`;
  return <img className={classNames} src={diceImg} alt="주사위 이미지" />;
}

export default App;
```

className 여러 개를 받아서 백틱으로 묶어서 문자열로 사용할 수 있긴 한데 그러면 클래스 이름이 길어질수록 보기 나빠진다. 그래서 쓰는 라이브러리가 classnames인데, 이건 뭐 따로 설정할게 있고 뭔말인지 모르겠으니 나중에 더 살펴보자..

<br>
```
