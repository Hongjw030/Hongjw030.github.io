# 🍕 테이블 🍕
#### Week1 html css 기초 / Topic 3 HTML 핵심 / 5. Table

>목차 
>>[1. 테이블 태그](#1-테이블-태그)<br>
[2. 머리글, 바닥글](#2-머리글-바닥글)<br>
[3. 테이블 스타일링](#3-테이블-스타일링)<br>


<br><br>


## 1. 테이블 태그
html에 표를 넣으려면 table 태그를 쓰고, 그 안에

tr 로 각 행을 묶어주고 

td로 각 데이터를 묶는다. 

요즘엔 그리드나 flex같이 더 이쁜 게 많으니까 그냥 딱 정해진 간단한 표로 나타낼 때에나 쓰자.

```html
<table>
    <tr>
        <td>1행 1번</td> <td>1행 2번</td> <td>3행 3번</td>
    </tr>
    <tr>
        <td>2행 1번</td> <td>2행 2번</td> <td>2행 3번</td>
    </tr>
</table>
```

## 2. 머리글, 바닥글
표에서도 기준을 머리글, 바닥글이라 한다. 이걸 좀 더 의미있게 표현해보자.

기준을 thead 태그로 묶고, 각 기준은 th로 묶자. 

그 아래 내용은 tbody로 묶고,

바닥을 tfoot으로 묶자. 

즉, 각 데이터 내용은 td로 묶되 기준이나 합계 같은 것들은 th로 묶으면 된다!!
```html
<table>
    <thead>
        <tr>
            <th>이름</th> <th>나이</th> <th>성별</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1행 1번</td> <td>1행 2번</td> <td>3행 3번</td>

        </tr>
        <tr>
            <td>2행 1번</td> <td>2행 2번</td> <td>2행 3번</td>
        </tr>
    </tbody>
</table>
```

## 3. 테이블 스타일링
```css
table{
    /* 테이블의 가장자리 선 */
    border: 1px solid red;

    /* 테이블 표 사이 간격 0으로 만들기 */
    border-collapse: collapse;

    /* 테이블 표 간격 지정 */
    border-spacing: 15px;
}


```