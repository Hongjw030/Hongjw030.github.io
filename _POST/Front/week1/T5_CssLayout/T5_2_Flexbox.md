# 🥗 Flexbox 🥗
#### Week1 html css 기초 / Topic 5 css 레이아웃 / 2. Flexbox

>목차 
>>[1. 배치 방향](#1-배치-방향)<br>
[2. 정렬](#2-정렬)<br>
[3. 요소가 넘칠 때](#3-요소가-넘칠-때)<br>
[4. 간격 주기](#4-간격-주기)<br>
[5. 요소 꽉 채우기](#5-요소-꽉-채우기)<br>
[6. flex 요소의 크기](#6-flex-요소의-크기)<br>
[7. 인라인 안에서 flex box 만들기](#7-인라인-안에서-flex-box-만들기)<br>
[8. flex box 안에서 포지셔닝 하기.](#8-flex-box-안에서-포지셔닝-하기)<br>

<br><br>

## 0. flex box

**flex-box는 display 속성의 값이다.**

요소를 1차원적으로 일렬 배치하게 하는 게 flex box이다. 가로든, 세로든, 내가 원하는 방향으로 요소를 쌓을 수 있고 중앙 정렬도 할 수 있고 다양하게 활용할 수 있다. 


## 1. 배치 방향
기본적으로 flex box는 왼쪽에서 오른쪽으로 가로 배치가 된다.
```css
.container{
    display: flex;
    /* 이렇게 하면 container 내 요소들이 가로로 나열됨.  */
}
```

세로 정렬하려면 flex-direction 속성을 설정하자. 이러면 세로로 위-> 아래 배치가 된다. block이 배치되는 것과 비슷해보이지만 **flex에는 간격을 주고 정렬을 하는 등 더 많은 기능이 있다.**
```css
.container{
    display: flex;
    flex-direction: column;
}
```

만약 아래에서 위, 우에서 좌로 방향을 전환하려면 row-reverse, column-reverse 속성값을 주자. 
```css
.container{
    display: flex;
    flex-direction: column-reverse;
}
```


## 2. 정렬
* 기본축: 요소가 정렬되는 방향.
* 교차 축: 요소와 수직인 방향.

즉, flex-direction이 column이라면 기본 축은 세로, 교차 축은 가로가 된다. 

정렬을 할 때엔 center, flex-end(기본 축에서 맨 끝에 정렬), flex-start, space-between(간격 일정하게 배치), space-around(간격 일정하게 배치하고 컨테이너에도 같은 간격을 둬서 padding처럼 있게 함.)

1. 기본축 방향에서 정렬하려면 justify-content 속성을 부여하자.
```css
.container{
    display: flex;
    justify-content: center;
    /* 중앙 정렬 */
}
```

2. 교차축 방향에서 정렬하려면 align-item 속성을 부여하자.
```css
.container{
    display: flex;
    align-item: space-bewteen;
    /* 교차축을 기준으로 나열됨. */
}
```



## 3. 요소가 넘칠 때
만약 콘테이너 요소 크기는 100px밖에 안되는데 안에 요소가 겁나 많다면??

**요소가 그대로 튀어나온다!!**

그래서 요소가 콘테이너 바깥으로 삐져나가지 않게 자동으로 줄바꿈하게 해줄 수 있다. 바로 flex-wrap 속성이다.

wrap에 nowrap 값을 주면 줄바꿈이 안된다. 
```css
.container{
    display: flex;
    flex-wrap: wrap;
}
```


## 4. 간격 주기
요소 사이에 간격을 넣어보자. gap 속성을 쓰면 된다!!
```css
.container{
    display: flex;
    gap: 30px;
}
```
만약 flex-wrap: wrap 속성으로 줄바꿈이 된 경우, 각 줄 사이에도 gap이 생긴다. 

만약 양 옆의 간격과 각 줄 사이 간격의 크기를 다르게 하려면 값을 두 개 주면 된다.
```css
.container{
    display: flex;
    gap: 30px 60px;
    /* 항상 방향은 세로 간격 가로 간격!! */
}
```
**flex direction을 바꾼대도 gap은 항상 세로-> 가로 순으로 간격을 적는다!!**



## 5. 요소 꽉 채우기
콘테이너 안을 요소들로 꽉 채우고 싶은데, width와 height 속성 없이 요소가 크기가 늘어나게 할 수 있다!! 

바로 flex-grow 속성이다.

아래 코드처럼 flex-grow는 단위 없이 숫자로 쓴다. 컨테이너 내부 여백을 1:2로 나눠서 a 요소를 1만큼 더 늘리고, b 요소를 2만큼 더 늘려준다.

기본적으로 flex-grow 값은 0이다.
```css
.container{display:flex;}
.a{
    flex-grow: 1;
}
.b{
    flex-grow:2;
}
.c{}
```

만약 요소가 너무 크면 flex-shrink 속성으로 저절로 요소가 줄어들기도 한다. 기본적으로 shrink 속성에 1 값이 주어지기 때문이다.
```css
.container{display:flex;}
.a{}
.b{
    flex-shrink:2;
}
.c{ 
    flex-shrink: 0;
}
```

넘치는 크기 중 1만큼 a를 줄이고, 2만큼 b를 줄이고, c는 아예 줄이지 않고 그냥 그 모습 그대로를 보여준다!! 

**헷갈리지 말자!! 요소의 개수가 너무 많으면 컨테이너 바깥으로 삐져나온다. 그치만 요소는 컨테이너 안에 다 들어가는데, 일부러 요소의 크기를 1000px 이렇게 늘리면 늘어난 공간은 overflow:hidden이 되어서 보이지 않는다!!!**


## 6. flex 요소의 크기
flex box 컨테이너 내부의 요소 크기는 flex-grow, flex-shrink를 통해 유연하게 크기가 늘어나고 줄어든다.

그거 말고 그냥 width, height로 정할 수는 있지만 flex-box 내에선 flex-basis 속성을 사용하자.
```css
.div{
    flex-grow: 1;
    flex-shrink: 0;
    flex-basis: 100px;
}
```
그리고 grow, shrink, basis를 하나로 줄일 수도 있다.
```css
.div{
    flex: 1 0 100px;
}
```

## 7. 인라인 안에서 flex box 만들기
인라인 태그 안에 flex 속성을 가진 a 태그를 두었다고 하자. a 태그는 인라인인데도 불구하고, display: flex; 속성때문에 블록처럼 된다.

따라서 a 태그 내부를 flex 적용하면서 a 자체는 인라인 상태로 유지하려면, **inline-flex로 속성값을 주자**

```html
<p>
  코딩, 쉬워질 때도 됐다. 
  <a class="new-window-link" href="https://codeit.kr">
    코드잇
    <img class="icon" src="new-window-link.svg" alt="새 창 열기" width="13" height="13">
  </a>
  에서 지금 바로 시작해보세요.
</p>
```
```css
.new-window-link {
  display: inline-flex;
  align-items: center;
  gap: 4px;
}
```

display:flex 였다면 a 태그가 block처럼 배치되어

<br>
코딩, 쉬워질 때도 됐다.<br>
코드잇<br>
에서 지금 바로 시작해보세요.<br><br>

로 배치가 된다. 그치만 inline-flex를 통해 
코딩, 쉬워질 때도 됐다.<br>
코드잇 에서 지금 바로 시작해보세요.<br><br>

라고 쓸 수 있는 것이다. 


## 8. flex box 안에서 포지셔닝 하기.
원래 자기의 위치에서 벗어나지 않는 static, relative, sticky 요소 빼고 

absolute, fixed는 원래 위치에서 아예 빠져버리는 포지션이다. 이 포지션은 **flex-box에서 아예 벗어나 컨테이너 바깥에 있는 것처럼 동작한다.**

만약 컨테이너 내부에서 요소에 absolute 속성을 주면, 다른 속성들은 그 놈을 없는 취급 한다. 그와 동시에 **absoluted 요소는  flex-grow, flex-shrink 등 flex 속성을 모두 무시한다!!**