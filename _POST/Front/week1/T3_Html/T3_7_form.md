# 🍹 폼 🍹
#### Week1 html css 기초 / Topic 3 HTML 핵심 / 7. Form

>목차 
>>[1. 폼 만들기](#1-폼-만들기)<br>
[2. 버튼](#2-버튼)<br>
[3. 폼 전송하기](#3-폼-전송하기)<br>
[4. 다양한 인풋](#4-다양한-인풋)<br>
[5. 인풋 태그 속성](#5-인풋-태그-속성)<br>


<br><br>

## 0. 폼이란?
데이터를 내가 웹 사이트에게 보내려면 어떻게 해야 할까? 폼을 쓰자!! 

폼의 구성은
* 내용을 적는 input
* 인풋에 붙은 글자 label
* 버튼

이 있다. 그리고 input에는 라디오박스나 체크박스, text, 등의 다양한 입력 방법이 있ㄷ사.


## 1. 폼 만들기
form  태그 안에 input 태그와 label 태그를 넣고, button 태그를 추가하자.
```html
<form>
    <label>이메일</label>
    <input>
    
    <!-- 라벨 안에 input을 넣으면 서로 연결된다. -->
    <label>이메일
        <input>
    </label>

    <!-- input 아이디를 라벨에 주어도 서로 연결된다. -->
    <label for="email-input">이메일</label>
    <input id="email-input">
</form>
```

input의 데이터를 웹으로 보내주려면 name 속성을 꼭!!! 지정해줘야 한다. id랑 헷갈리지 말자!!!

form 태그가 데이터를 보낼 때 이 name 값을 가지고 변수를 체크한다. 
```html
<form>
    <label for="eamil-input">이메일</label>
    <input id="email-input" name="myemail">
</form>
```

각 input에 type 속성을 줘서 표시하자. email, password, 등이 있다. 
```html
<form>
    <label for="eamil-input">이메일</label>
    <input id="email-input" name="myemail" type="email">
</form>
```


## 2. 버튼
버튼을 추가해보자!! **버튼은 기본적으로 form 태그 안에 있다.** form 바깥에 있으면 form과 연결되지 않아 데이터를 전송하지 않는다. 
```html
<form>
    <label for="eamil-input">이메일</label>
    <input id="email-input" name="myemail" type="email">
    <button>버튼</button>
</form>
```

버튼의 type 속성에 button 값을 주면 아무 동작도 하지 않지만, submit 으로 지정해주면 데이터를 전송하고, reset으로 하면 input에 적은 값을 초기화해준다.
```html
<form>
    <input type="email">
    <input type="password">
    <button type="submit">이 버튼은 제출용</button>
    <button type="reset">이 버튼은 초기화</button>
    <button type="button">이 버튼은 x</button>
</form>
```


## 3. 폼 전송하기
폼의 데이터를 전송하는 데에는 두가지 속성을 쓴다.
1. action 속성: 폼 내용을 전송할 주소를 정하기. 폼 제출 버튼을 누르면 기본적인 페이지 주소로 이동하는데, 이렇게 말고 직접 다른 주소로 지정할 수 있다.
```html
<form action="https://google.com/search">
    <input name="q">
  <button>검색</button>
</form>
```
2. method 속성: 폼을 어떻게 전송할지 정하기. 간단한 데이터를 받는 GET, 큰 데이터를 전송하는 POST, 등의 속성값이 있다. 지정하지 않으면 디폴트로 GET으로 된다. 
```html
<form method="post">
    <div>
        <label for="profile">프로필</label>
        <input id="profile" name="profile" type="file">
    </div>
    <button>확인</button>
</form>
```


## 4. 다양한 인풋

1. 여러 옵션 중 여러 개를 선택하는 체크박스.

아래처럼 코드를 짤 때 만약 액션과 코미디를 선택한다면 **film의 값으로 action, comedy value 값이 지정된다.** 즉, 주소로 film=action&film=comedy 주소로 전송됨.
```html
<label for="film">좋아하는 영화 장르</label>
<label>
  <input type="checkbox" name="film" value="action">
  액션
</label>
<label>
  <input type="checkbox" name="film" value="comedy">
  코미디
</label>
<label>
  <input type="checkbox" name="film" value="romance">
  로맨스
</label>
```

2. 날짜
```html
<input name="birthdate" type="date">
```

3. 파일을 선택하는 인풋.

* accept 속성으로 허용할 파일 확장자를 정하자.
* multiple 속성을 주면 파일을 여러 개 선택할 수도 있다.
```html
<input name="avatar" type="file" accept=".png, .jpg">

<input name="photos" type="file" mutliple> <!-- 여러 개 선택 가능 -->
<input name="avatar" type="file"> <!-- 한 개만 선택 가능 -->
```



4. 이메일. type을 이메일로 지정하면 이메일 형식에 어긋날 경우 폼이 전송되지 않는다.
```html
<input name="email" type="email">
```


5. 숫자. min, max, step 속성을 줄 수 있다.
```html
<input type="number">

<!-- 100에서 1000사이 -->
<input type="number" min="100" max="1000">

<!-- 100에서 1000사이, 버튼을 눌렀을 때 100씩 증가, 감소 -->
<input type="number" min="100" max="1000" step="100">
```

6. 비밀번호. 타이핑하면 내용이 자동으로 가려진다.
```html
<input type="password">
```

7. 라디오버튼. 체크박스는 여러 개 선택 가능하지만 라디오는 딱 하나!! 만 선택한다.
```html
<input id="bad" name="feeling" value="0" type="radio">
<label for="bad">나쁨</label>

<input id="soso" name="feeling" value="1" type="radio">
<label for="soso">그저그럼</label>

<input id="good" name="feeling" value="2" type="radio">
<label for="good">좋음</label></label>
```


8. 범위. 범위 안에서만 선택 가능하게 지정한다.
```html
<label for="signup-feeling">현재 기분</label>
<input id="signup-feeling" name="feeling" min="1" min="10" type="range">
```

9. 일반적인 텍스트.
```html
<input name="nickname" type="text">
```

10. 옵션 선택하는 select 태그. 옆에 화살표 누르면 옵션이 좌르륵 떠서 그 중 하나 선택하는 그거.
```html
<label for="genre">장르</label>
<select id="genre" name="genre">
  <option value="korean">한국 영화</option>
  <option value="foreign">외국 영화</option>
  <option value="drama">드라마</option>
</select>
```

11. 긴 글은 text 말고 textarea 쓰자.
```html
<textarea name="content"></textarea>
```



## 5. 인풋 태그 속성
1. placeholder은 input이 비어있을 때 미리 보여주는 값이다. 

**만약 placeholder의 스타일을 바꾸려면 css 선택자로 ::placeholder을 활용하자.**
```html
<input name="username" placeholder="이메일 또는 휴대전화">

<style>
    input::placeholder {
        color: #dddddd;
    }
</style>
```

2. 반드시 인풋을 채워야 할 때 required 속성을 넣자. 

이 required 인풋에 값이 비어있다면 전송 버튼을 눌러도 전송되지 않는다.
```html
<input name="email" type="email" required>
```

3. autocomplete는 자동완성을 띄워준다.

얘는 속성값에 참 거짓이 아니라 "on" 이라는 값을 꼭 넣어줘야 한다. 
```html
<input name="search" type="text" autocomplete="on">

```