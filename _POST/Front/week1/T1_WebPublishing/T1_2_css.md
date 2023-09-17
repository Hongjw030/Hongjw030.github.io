# 🧁 Css 기초 정리 🧁
#### Week1 html css 기초 / Topic 1 웹 퍼블리싱 / 2. css 기초

>목차 
>>[1. 배경색](#1-배경색)<br>
[2. 글자색](#2-글자색)<br>
[3. 글꼴](#3-글꼴)<br>
[4. 구글 폰트](#4-구글-폰트)<br>
[5. 글자 크기와 굵기](#5-글자-크기와-굵기)<br>
[6. 글 정렬](#6-글-정렬)<br>
[7. 크기](#7-크기)<br>
[8. 여백](#8-여백)<br>

<br><br>

## 0. css 기초 문법

html 태그에 css를 적용하기 위해 style이라는 속성을 사용한다. css 속성 문법은 

stye = "css 속성 이름 : css 속성 값"

으로 작성한다. 여러 속성을 쓰려면 세미콜론으로 이어주자. 


<br>
<br>


## 1. 배경색
배경색을 넣어보자. 지정된 영역에만 style이 적용되며, style은 css 속성이지 태그의 속성이 아니니 헷갈리지 말자!!
```html
<html>
    <head>
    </head>
    <body>
        <div style="background-color: purple">
            이곳 배경 색은 보라색이다.
        </div>
        <div style="#44f21f">
            보통 색상코드로 색을 표시한다.
        </div>
    </body>
</html>
```


## 2. 글자색
css 속성에 color 속성을 넣어주자.

만약 페이지 전체 글자 색을 적용하려면, 해당 페이지를 감싸는 부모 태그에 글자색을 넣자.

속성을 여러 개 부여하려면 세미콜론을 붙여 이어주자.
```html
<html>
    <head>
    </head>
    <body>
        <div style="background-color: purple; color:#ffffff">
            이곳 배경 색은 보라색이고 글자는 하얀색이다.
        </div>
        <div style="color: #44f21f">
            <div>
                한꺼번에 색을 지정하려면
            </div>
            <div>
                부모에게 색을 주자.
            </div>
        </div>
    </body>
</html>
```


## 3. 글꼴
font-family 속성은 여러 값을 동시에 받아 글꼴을 여러 개 지정할 수 있게 해준다. 

* sans-serif : 뭉툭한 고딕, 나눔 글씨체.
* serif: 날카로운 명조, 궁서체.


```html
<html>
    <head>
    </head>
    <body style="font-family: snas-serif">
        <div style="color: #44f21f">
            <div>
                한꺼번에 글꼴 지정하려면
            </div>
            <div>
                부모에게 이쁜 글꼴 적용하기
            </div>
        </div>
        <div style="fon-family: Arial, sans-serif">
            이렇게 여러 개 지정하면, 먼저 Arial 글씨를 지정하고 Arial을 적용할 수 없는 글자에선 sans-serif를 지정한다는 뜻!
        </div>
    </body>
</html>
```


## 4. 구글 폰트
글꼴파일을 사용자가 직접 하나하나 다운받게 하지 말고, 인터넷으로 제공하는 방법이 있다.

이를 **웹 폰트** 라고 부른다!!

내가 만든 웹 페이지에 접속하면 컴퓨터가 html 파일을 읽어 글꼴을 자동으로 인터넷에서 다운받아주는 방식이다. 

예를 들어 구글 폰트에서 링크를 가져오면...

```html
<html>
    <head>
        <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@200;300&display=swap" rel="stylesheet">
    </head>
    <body style="font-family: 'Noto Sans KR', sans-serif">
        이제 body 태그 내부 글자들은 모두 noto 글꼴이 된다. 
    </body>
</html>
```


## 5. 글자 크기와 굵기
크기는 font-size, 굵기는 font-weight 속성을 부여하자.
```html
<html>
    <head>
    </head>
    <body>
        <h1 style="font-size: 24px; font-weight: 900">
            글자의 크기를 바꾸자
        </h1>
        <h5 style="font-size:16px; font-weight: 100">
            weight 값은 100, 200, 300... 단위로, 작을 수록 얇다. 
        </h5>
    </body>
</html>
```


## 6. 글 정렬
기본적으로 웹 페이지는 좌측 정렬이다. text-align 속성에 값을 부여해 중앙, 우측 정렬도 할 수 있다!
```html
<html>
    <head>
    </head>
    <body>
        <div style="text-align: center">
            중앙 정렬 하시오.
        </div>
        <div style="text-align: right">
            우측 정렬 하시오.
        </div>
    </body>
</html>
```


## 7. 크기
이미지나 본문이나 어떠한 영역의 크기를 지정할 때엔 width와 height 속성을 부여하자.

이 때 px 뿐만 아니라 퍼센트로 값을 부여해 vp에 따라 이미지나 영역의 크기가 달라지게도 할 수 있다. 
```html
<html>
    <head>
    </head>
    <body>
        <img src="url" style="width: 100%; height: 35px" />
    </body>
</html>
```


## 8. 여백
* 영역의 내부 가장자리에 생기는 여백을 padding
* 영역 외부 가장자리에 생기는 여백을 madrgin

이라고 한다. 이 영역은 top, bottom, left, right 속성을 통해 크기를 조절한다. 

1. 속성값을 한 개만 쓰면 상하좌우 같은 여백 크기.
2. 속성값을 두 개 주면 a는 상하, b는 좌우 여백의 크기.
3. 속성값을 3개 주면 a는 위, b는 좌우, c는 아래 여백의 크기.
4. 속성값을 4개 주면 a는 상, b는 오른쪽, c는 아래, d는 왼쪽 여백의 크기.

* **margin에는 auto 속성값을 줄 수 있다!!!** margin: 10px auto; 하면 위아래 10px여백, 양 옆엔 자동으로 공간을 채워줌.
* **padding에는 auto 속성값이 없으니 주의!!**
```html
<html>
    <head>
    </head>
    <body>
        <div style="margin: 15px;">
            바깥 여백을 15px 만들기
        </div>
        <div style="padding: 32px;">
            안쪽 여백을 32px 만들기.
        </div>
        <div style="margin:0; padding:0">
            여백값에 0을 줄 수도 있다.
        </div>
    </body>
</html>
```