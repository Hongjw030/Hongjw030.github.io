# 🧃 반응형 웹 🧃
#### Week3 JS 기초 / Topic 1 반응형 웹 / 1. 반응형 웹


<br><br>

## 1. 반응형 웹이란?

브라우저 창 크기를 줄이거나 늘리는 등 크기에 따라 레이아웃이 바뀌는 걸 반응형 웹 디자인 (responsive web design) 이라 한다. 

* 장점: 이렇게 하면 따로 모바일, 태블릿 버전 웹을 안 만들어도 됨. 

이런 걸 만들려면 css 파일에서 미디어 쿼리 언어를 쓰자!!!

```css
/* 일단 24, 16px이 기본. */
h1{font-size: 24px;}
p{font-size: 16px;}

/* 브라우저 길이가 700px 이상이면 아래를 적용해라. */
@media (min-width: 700px){
    h1{font-size:36px;}
    p{font-size:24px;}
}

/* 브라우저 길이가 950px 이상이면 아래를 적용해라. */
@media (min-width: 950px){
    h1{font-size:45px;}
    p{font-size:30px;}
}
```

**이렇게 반응형을 만들 때엔 display: float 속성을 잘 쓰자!!**