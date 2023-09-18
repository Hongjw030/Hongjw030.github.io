# 🍫 다른 코드 불러오기 🍫
#### Week1 html css 기초 / Topic 3 HTML 핵심 / 8. 다른 코드 불러오기

>목차 
>>[1. link 태그](#1-link-태그)<br>
[2. script 태그](#2-script-태그)<br>



<br><br>

## 1. link 태그
link 태그는 css파일이나 외부 파일을 가져올 때 쓴다. 

* link 태그의 속성 중 rel은 relation으로, 불러올 파일이 무슨 파일인지 적는다.
* href 속성은 파일의 주소 경로를 적는다. 

a 태그는 body!! link 는 head에 넣자!!!

```html
<html>
    <head>
        <link rel="stylesheet" href="style.css">
    </head>
</html>
```

또한 link 태그로 웹페이지 탭 옆에 작은 아이콘을 띄울 수 있는데 그걸 파비콘이라 한다.
```html
<html>
    <head>
        <link rel="icon" href="maple.icon">
    </head>
</html>
```

## 2. script 태그
인터넷에서 버튼 누르면 뭔가 바뀌고 등등.. 하여간 이런 동작은 js로 한다.

html 파일 안에 script 태그를 넣어서 js를 작성하자!!


```html
<html>
    <head></head>
    <body>
        <script>
            console.log("자바스크립트 출력");
        </script>
    </body>
</html>
```

보통은 js 파일을 따로 만든다. src 속성으로 js 위치를 정해주면 된다.  

반드시!! 종료 태그를 써야 함!! 
```html
<html>
    <head></head>
    <body>
        <script src="temp.js"></script>
    </body>
</html>
```