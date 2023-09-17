# 🍩 CSS 기본 개념 🍩
#### Week1 html css 기초 / Topic 2 CSS 핵심 / 2. css 속성

>목차 
>>[1. 텍스트 스타일링](#1-텍스트-스타일링)<br>
[2. 배경 이미지](#2-배경-이미지)<br>
[3. 그라디언트](#3-그라디언트)<br>
[4. 그림자](#4-그림자)<br>
[5. 불투명도](#5-불투명도)<br>

<br><br>


## 1. 텍스트 스타일링
```css
.div{
    color: #f2f2f2; 
    /* 글자색 바꾸는 속성 */
    font-size: # 32px; 
    /* 글자 크기 바꾸는 속성 */
    font-family: Poppins, 'Noto Sans KR'; 
    /* 글꼴 지정 속성 */
    font-weight: 700; 
    /* 글자 굵기 지정 */

    line-height: 1.5;
    /* 줄의 높이 조절. 1 = font-size이다. */

    text-decoration: none;
    text-decoration: underline;
    text-decoration: line-through;
    /* 밑줄 없음, 밑줄 있음, 취소선 */
}

```


## 2. 배경 이미지
div 영역의 배경을 단색이 아니라 이미지로 넣어보자.
```css
.div{
    background-image: url('imges/img.png'); 
}
```
이렇게 기본적으로 사용하면 div가 이미지보다 더 클 경우, 이미지가 바둑판처럼 반복돼서 안 이쁘다. 다른 속성을 더 추가하자!!!
```css
.div{
    background-image: url('imges/img.png'); 
    /* url('따옴표쓰고 url 주소') */
    background-repeat: no-repeat;
    /* 이미지 반복하지 말고 하나만. */
    background-position:center;
    /* 이미지 중앙 정렬 */
    background-size: cover;
    /* div 영역에 이미지가 꽉 차게. */
}
```
참고로 background-size: contain 은 div 영역에 이미지가 잘리지 않는 선에서 최대 크기로! 

background-size: 100px 20px; 이렇게 길이 직접 지정도 가능.


## 3. 그라데이션
css 배경에 그라데이션 넣어보기. 그라데이션도 일종의 이미지라서 background-image 속성을 쓴다.

gradient generator이라고 구글에 쳐서 값 따오는 게 좋다. 
```css
.div{
    background-image: linear-gradient(rgba(0,0,0,1), rgba(0,0,0,0)); 
    /* 검은색에서 점점 투명하게, 위에서 아래로 */
    
    background-image: linear-gradient(90deg, rgba(0,0,0,1), rgba(0,0,0,0)); 
    /* 90도 반시계방향 회전. 왼쪽 검은색, 오른쪽 투명. */

    background-image: linear-gradient(rgba(0,0,0,1) 40%, rgba(0,0,0,0)); 
    /* div의 40퍼가 검은색. */

    background-image: 
        linear-gradient( rgba(0,0,0,1), rgba(0,0,0,0)),
        url('imges/img.png')
    ; 
    /* 그림과 그라데이션 겹치기. 단, 그라데이션을 먼저 써라!! */
}
```


## 4. 그림자
한 영역에 그림자를 넣으려면 box-shadow 속성을 쓰자.

마찬가지로 box-shadow generator을 구글에서 검색해서 따와도 좋다.
```css
.div{
    box-shadow: 10px 15px gray;
    /* 회색의 그림자가 오른쪽으로 10px, 밑으로 15px 생김. */

    box-shadow: 10px 15px 20px gray;
    /* 20px의 흐림효과 추가. */
    
    box-shadow: 10px 15px 20px 5px gray;
    /* 5px의 퍼짐효과 추가. */
}
```


## 5. 불투명도
영역을 반투명하게 만들어보자.
 * background를 rgba로 설정하는 방법은 배경색만 반투명하게 한다.
 * opacity라는 속성은 배경색 뿐만 아니라 내부 요소 전체를 반투명하게 한다.
```css
.div{
    opacity: 0.5
    /* 속성값은 0~1사이 값이다. */
}
```
