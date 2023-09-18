# 🥓 리스트 🥓
#### Week1 html css 기초 / Topic 3 HTML 핵심 / 4. List

>목차 
>>[1. 순서 있는 리스트](#1-순서-있는-리스트)<br>
[2. 순서 없는 리스트](#2-순서-없는-리스트)<br>
[3. 리스트 스타일링](#3-리스트-스타일링)<br>


<br><br>


## 1. 순서 있는 리스트
ordered list의 줄임말인 ol 태그로 감싸서, 각 요소를 li 태그로 묶는다.
```html
<h1>할일</h1>
<ol>
    <li>밥먹기</li>
    <li>자기</li>
    <li>숨쉬기</li>
</ol>
```
자동으로 숫자가 1, 2, 3, 붙는다. 


## 2. 순서 없는 리스트
unordered list의 줄임말인 ul 태그로 감싸서, 각 요소를 li 태그로 묶는다.
```html
<h1>카테고리</h1>
<ul>
    <li>메이플</li>
    <li>엘소드</li>
    <li>옵치</li>
</ul>
```
숫자가 붙지 않고 앞에 불렛포인트만 붙는다. 


## 3. 리스트 스타일링
그런데 뭔가 list만 쓰니까 너무 안 이쁘다. 
1. ol 꾸미는 법
```html
<!-- 이렇게 type에 a, A, 가, 등 을 주면 자연수 숫자 말고 abc.. 가나다.. 이렇게 번호가 매겨진다.  -->
<ol type="a">
    <li>밥먹기</li>
    <li>자기</li>
    <li>숨쉬기</li></ol>
```
```css
ol{
    /* disc 속성을 주면 번호가 사라지고 불렛이 생긴다. */
    list-style: disc;
    /* none 속성을 주면 아예 모든 표시가 사라져 본문처럼 보인다. */
    list-style: none;
}

ol > li{
    /* 원래 li나 ol, ul 태그는 블록 속성이기 때문에 인라인으로 바꿔서 가로배치도 가능하다.  */
    display: inline-block;
    border: 1px solid gray;
}
```