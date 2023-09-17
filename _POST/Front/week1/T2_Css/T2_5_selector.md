# 🍤 Selector 개념 🍤
#### Week1 html css 기초 / Topic 2 CSS 핵심 / 5. selector

>목차 
>>
[1. css 선택자란](#1-css-선택자란)<br>
[2. 선택자 붙여쓰기](#2-선택자-붙여쓰기)<br>
[3. 자식, 자손 선택하기](#3-자식-자손-선택하기)<br>
[4. 가상 클래스](#4-가상-클래스)<br>
[5. 알아두면 좋은 선택자들](#5-알아두면-좋은-선택자들)<br>
[6. 선택자 레시피](#6-선택자-레시피)<br>

<br><br>


## 1. css 선택자란
css 규칙을 선언할 때, 선택자로 태그나 아이디, 클래스를 쓸 수 있으며 이들을 조합해서 더 구체적으로 명시할 수도 있다.

* 선택자 목록" 스타일이 같은 클래스들 여러 개를 목록으로 묶어서 선택자로 지정한다.
```css
.Aclass, .Bclass, Cclass{
    color: #ff22ff;
    /* Aclass와 Bclass, Cclass가 적어도 한 개 이상 지정된 태그들에게 스타일 부여. */
}
```

css의 문법은
```css
선택자{
    선언;
    선언;
}
으로 이루어졌다.
```

## 2. 선택자 붙여쓰기
html 태그에서는 하나의 클래스만 주는 게 아니라 여러 클래스를 한꺼번에 줄 수 있다. 이렇게 여러 클래스를 가진 태그를 선택할 때엔 선택자를 붙여쓴다.

선택자 붙여쓰기를 할 때엔 html태그가 가장 먼저 와야 한다.

그 이후엔 아이디가 먼저 와도 되고, 클래스가 먼저 와도 되지만 암묵적으로 아이디를 먼저 쓰는 편이다.

**클래스를 무조건 많이 쓰기보단, 두 개 이하가 적당하다.**

```html
<div class="Aclass Bclass">
    이 div에는 클래스가 2개 주어졌다.
</div>
<div class="Aclass">
    이 div에는 클래스가 1개 주어졌다.
</div>
```
```css
.Aclass.Bclass{
    color: #ff22ff;
    /* 첫번째 div에만 적용되는 스타일 */
}

div.Aclass{
    color: #22ff22;
    /* div 태그이면서 Aclass를 가진 태그에만 적용되는 스타일. */
}

```

## 3. 자식, 자손 선택하기
복잡한 웹을 만들다보면 실수로 아이디나 클래스 이름을 중복해서 작성하는 경우가 있다. 이걸 막기 위해 자식, 자손을 선택해서 선택자를 작성하자.

1. 부모의 직계 자식 선택하기: **child combinator인 > 기호를 사용해라.**
```css
.parent-class > .child-class{
    color: #ff22ff;
    /* parent-class 클래스를 가진 요소의 직계 자식 태그 중 child-class 요소에만 적용하라. */
}
```
2. 부모의 자손 선택하기: **descent combinator인 스페이스바를 사용해라.**
```css
.parent-class .descent-class{
    color: #ff22ff;
    /* 부모 하위 자손들 중 descent-class 클래스 요소에 전체 적용하라. */
}
```

참고로 부모의 자손에는 직계 자식도 포함됨!!



## 4. 가상 클래스
태그 선택자들에겐 미리 컴퓨터가 정해둔 가상 클래스들이 있다. 이걸 활용하면 더 많은 스타일을 쓸 수 있다. 아래는 예시.

```css
a{
    text-decoration: none;
}
a:hover{
    text-decoration: underline;
}
```
a 태그에 밑줄을 모두 없애되, 마우스를 올리면 밑줄이 생긴다.

여기서 :hover이 가상클래스 이름이다.

가상클래스 종류:
**hover, active, visited, focus 가 있음.**


<br>
정리하자면 선택자를 쓰는 방식에는

```css
.a-class, .b-class{
    /* a-class or b-class에 적용 */
}
```
```css
.a-class.b-class{
    /* a-class and b-class에 적용 */
}
```
```css
.a-class .b-class{
    /* a-class 하위 자식 태그 중 b-class에 적용 */
}
```

## 5. 알아두면 좋은 선택자들
```css
*{
    box-sizing: border-box;
    /* 전체 요소를 선택한다. */
}

.a-class>*{
    /* a-class의 모든 직계 자식을 선택한다. */
}

.a-class :nth-child(3){
    /* a-class의 직계 자식 중 3번째를 선택한다 */
}

.a-class :nth-child(even){
    /* a-class의 직계 자식 중 짝수 자식을 선택한다. */
}

.a-class :first-child{
    /* a-class의 직계 자식 중 첫놈 */
}

.a-class :last-child{
    /* a-class의 직계 자식 중 마지막 놈 */
}
```



## 6. 선택자 레시피
1. 선택자는 단순하게 조합해라!!
2. 같은 클래스 중에서도 변화를 줄 때 선택자를 조합하자. 
3. 클래스를 넣어줄 태그가 너무 많다면 자손 선택자를 쓰자. 
4. 가끔 nth-child도 쓰긴 쓴다. 잘 판단하자!