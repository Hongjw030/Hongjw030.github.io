# 🍏 의미있는 태그 🍏
#### Week1 html css 기초 / Topic 3 HTML 핵심 / 9. 의미있는 태그

>목차 
>>
[1. 사이트에 대한 정보](#1-사이트에-대한-정보)<br>
[2. 시맨틱 태그](#2-시맨틱-태그)<br>


<br><br>

## 1. 사이트에 대한 정보
head 태그 내에선 페이지에 대한 정보를 담고 있다. 이 때 페이지에 대한 정보를 **Metadata, 메타데이터** 라고 한다.

일반적인 내용에 붙이는 정보값을 말한다! 

```html
<head>
    <meta charset="utf-8">
    <!-- 인코딩 방식을 지정해줌. -->
</head>
```

og는 페이스북에서 만든 메타데이터 형식으로, 오픈 그래프의 줄임말이다. 여러 활용도가 있지만 주로 sns 퍼가기를 할 때 미리보기를 만들어준다. 

```html
<head>
    <meta property="og:title"
        content="코드잇 사이트">
</head>
```

## 2. 시맨틱 태그
html은 문서의 내용과 구조를 만드는 것이다. 그 중 div는 문서의 영역만 나타내지 구조와 의미가 없음. 그래서!! div와 똑같은 기능을 하는데 그냥 헤더인지, 내비인지, 아티클인지 의미를 부여하기 위해 이름을 주었다

이게 바로 **시맨틱 태그** 이다. 성질은 div와 같음.

```html
<html>
    <head></head>
    <body>
        
        <header></header>
        <header></header>
        
        <main>
            <section>
                <article></article>
                <article></article>
                <figure></figure>
            </section>

            <section>
                <article></article>
                <article></article>
            </section>
        </main>

        <footer></footer>
    </body>
</html>
```

* header, footer, main(그 안에 section, article, figure), nav 가 있다.
* header, footer은 여러 번 쓸 수 있는 반면에 main은 한 페이지에 하나만 !!
* section이라는 큰 단락 안에 article들이 있다.
* figure은 사진과 사진의 설명을 담은 영역.

이런 시맨틱 태그는 사이트의 영역을 좀더 의미있게 나눠주기 때문에 태그를 작성하는 사람의 의도가 담겨있다. 

div만 써도 되는데 시맨틱 태그를 굳이 쓰는 이유는, 
1. 검색 최적화에 도움이 되기 때문이다. 검색엔진이 header, main 쪽에 중점적으로 본문을 읽으면서 정보를 잘 가져와 최적화가 잘 된다. 
2. 웹 접근성을 높이기 때문이다. Web Accessibility를 줄여서 A11y라고도 하는데, 장애인들도 잘 활용할 수 있게 모두에게 배리어 프리한 웹 접근을 하게끔 한다.
3. 개발자들 입장에서도 시맨틱 코드를 사용하는 게 더 이해하기 쉬워 개발성이 높아진다. 