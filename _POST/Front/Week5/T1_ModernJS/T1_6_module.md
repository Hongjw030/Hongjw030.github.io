# 🍑 모듈 🍑

#### Week5 모던 자바스크립트 / Topic 1 모던 자바스크립트 / 6. 모듈

> 목차
>
> > 1. 모듈
> > 2. 모듈 문법
> > 3. 이름 바꾸기
> > 4. 한꺼번에 다루기
> > 5. default export

<br><br>

## 1. 모듈

코드가 길어지면 파일을 여러 개로 분리하는 게 좋다. 이렇게 기능이나 목적에 따라 파일을 분리하는 것을 모듈화 modularize 라고 부른다!! 그리고 각 파일을 모듈 이라고 부른다.

이렇게 모듈화를 하면 코드를 효율적으로 관리할 수 있고, 다른 프로그램에서 import로 재사용 할 수 있다는 장점이 있다!!

초창기 js는 간단히 웹 동작을 구현하기 위함이라 모듈화 기능이 없었지만, 2015년 이후 문법부턴 모듈 문법이 생겼다.

#### 모듈 파일의 조건

**모듈파일이 되려면 모듈 파일만의 독립적인 범위를 가져야 한다.**

- 이 모듈 파일이 가지는 독립적인 범위를 모듈 스코프라 하는데, 이 모듈 스코프 내에서 선언된 변수는 모듈 파일 내에서만 사용 가능해야 한다는 것이다.
- printer.js와 login.js 파일이 있을 때, 두 파일은 물리적으로 코드가 분리되었지만 printer에서 선언한 함수와 변수를 그냥 login에서 가져와 쓸 수 있다!!
- 따라서 모듈 파일 각각이 다른 파일과는 스코프를 공유하지 못하게 다음과 같은 코드를 추가하자.
- 모듈 문법은 보안문제 때문에 로컬에서 html 파일을 실행하면 에러가 난다. live 서버 같이 서버를 통해 열어야 모듈이 잘 임포트된다.

```html
<html>
  <head> </head>
  <body>
    <!-- type module을 선언하면 스코프 공유 안함 -->
    <script type="module" src="printer.js"></script>
    <!-- type 선언 안하면 스코프 공유 함! -->
    <script src="login.js"></script>
  </body>
</html>
```

<br>

## 2. 모듈 문법

모듈 스코프를 가지게 되면 다른 파일에서 모듈의 변수나 함수에 접근 못하지만, 모듈 문법을 통해 접근하게 할 수도 있다. 쓸 함수 앞에 export 키워드를 붙이고, 가져올 파일로 가서 import 문을 써주자.

```js
// printer.js

export const title = "codeit";

export function print(value) {
  console.log(value);
}
```

```js
// login.js
import { title, print } from "./printer.js";

print(title);
```

그런데 만약 login.js 안에서도 title이라는 이름의 변수를 다루려면 어떻게 할까? 그 경우 import한 title 변수의 이름을 바꿔주면 된다.

```js
import { title, print } from "./printer.js";
const title = "code"; // 에러 발생
```

```js
// 이렇게 as로 이름 붙이기.
import { title as printerTitle, print } from "./printer.js";
const title = "code";
print(title);
print(printerTitle);
```

근데 모듈 파일에 export 할 것들이 너무 많다면? \* 로 한꺼번에 가져오자.

참고로 이 \* 문자를 와일드 카드 문자라고도 한다.

```js
// 한꺼번에  export 하기. 이러면 각 문장에 export를 안 써도 된다.

const title = "printer";
function print(value) {
  console.log(value);
}

export { title, print };
// 참고로 export {title as printTitle print}; 이런 식으로 import 문 말고 export 문에서 미리 이름 지정할 수 있다!
```

```js
import * as printerJs from "./printer.js";
import { title as membersTitle, data as membersData } from "./members.js";

const title = "a";
console.log(title);
console.log(printerJs.title);
console.log(membersTitle);
```

<br>

## 3. default export

export 할 대상을 중괄호로 묶어서 여러 개 동시에 내보낼 수 있지만, default 키워드를 쓰면 반드시 한 개만 export가 가능하다.

앞서 여러 개 export한 걸 named export, 이렇게 한 개만 보내는 것을 default export라고 한다.

```js
export const title = "codeit";
export const data = [];

// export default 여러 개 쓰면 에러 남. 반드시 한 파일당 한개!
export default title;
```

export default로 아예 값을 주는 경우도 있다.

```js
// printer.js
export const title = "codeit";
export const data = [];
export default "codeit";
```

```js
// index.js
// default를 임포트할 땐 as 키워드로 반드시 이름을 붙여야 한다.
import { default as codeit, title, data } from "./printer.js";
console.log(codeit);

// 아예 default 를 생략할 수도 있다.
import codeit, {title, data} from './printer.js';

// 와일드 카드를 쓰면 default 키워드로 호출할 수 있다.
import * from './printer.js';
console.log(defalut);
```

default와 named 방식 둘 다 섞어쓰면 import 하기 복잡해질 수 있다.

따라서 여러 개 export 할 경우는 named, 한 개만 export할 경우 default를 쓰는 걸로 통일하는 것이 좋다!!

**물론 대상 여러 개를 default로 export할 수는 있다.**

- 이렇게 default로 객체를 불러와 import하면 import 문이 간결해져서 좋고 변수 이름이 겹치지 않지만 각 프로퍼티마다 점 표기법으로 불러와야 하고, 프로퍼티의 이름을 변경할 수도 없다는 단점이 있다.
- 그래서 보통 여러 개 export할 땐 named export를 쓰는 것!

```js
// 중괄호로 대상 여러 개 export 하기.
// 객체를 export 하는 걸로 인식됨!!
export default { title, print };
```

```js
import printJs from "./printer.js";
printJs.print(printjs.title);
```

**참고로 js 파일이 많아지면 모듈 함수를 한꺼번에 모아두는 functions.js 파일을 만들고 index.js에서 import 할 수도 있다!!**

<br>
