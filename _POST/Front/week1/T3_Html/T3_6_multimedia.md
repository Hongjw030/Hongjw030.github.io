# 🥯 멀티미디어 🥯
#### Week1 html css 기초 / Topic 3 HTML 핵심 / 6. MultiMedia

>목차 
>>[1. 이미지](#1-이미지)<br>
[2. 비디오](#2-비디오)<br>
[3. 오디오](#3-오디오)<br>
[4. iframe](#4-iframe)<br>
<br><br>


## 1. 이미지
이미지 태그를 쓰고, 속성으로 src를 써서 이미지를 나타낸다.
* alt는 대체 텍스트를 표현한다. 되도록이면 적자.
* width, height는 크기를 표현한다. 미리 크기를 지정해주면 웹 입장에선 미리 크기를 알 수 있고 웹 로딩을 더 효율적으로 할 수 있다. 
```html
<img src="url" alt="대체 텍스트" width="320" height="320px"/>
```

## 2. 비디오
비디오 태그를 쓰고 src로 주소를 넣는다.
* autoplay는 속성 이름만 넣어줘도 참으로 반영된다. 일부 브라우저(크롬)에서는 autoplay muted 라고 적어야 작동. 비디오 자동재생하게 해주는데 muted 하면 소리 없이 자동 재생.
* controls 속성은 비디오에 정지 재생 버튼 자동으로 만들어준다.
* 여기도 width, height 속성이 있다. 
```html
<video src="url" autoplay controls></video>
```


## 3. 오디오
오디오 태그를 넣고 src로 주소를 넣는다. 근데 기본적으로 화면에 아무것도 안보이므로
* controls 속성이 반드시 필요하다!!!
* 여기도 autoplay 속성이 있다.
```html
<audio src="url" controls autoplay muted></audio>
```


## 4. iframe
iframe이란 inline frame이란 뜻이다. 

frame은 html 파일 각 부분을 나눠서 각 영역에 다른 html 파일들을 보여주는 기능인데, **문제가 많아서 안 쓴다.** iframe은 frame의 인라인버전으로, html 안에서 다른 html을 보여준다. 여기서도 src로 주소를 넣는다.
* 너비, 높이 속성이 있다.
```html
<iframe src="map.html"></iframe>
```

<br>
**기억하자!!! img 태그 빼곤 다 종료 태그가 있다.**