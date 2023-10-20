# 🍑 리액트 시작하기 🍑

#### Week7 리액트 / Topic 1 리액트 웹개발 시작 / 1. 리액트 시작하기

> 목차
>
> > 1.

<br><br>

## 1. 리액트로 데이터 다루기

리액트는 데이터를 필요한 걸 가져와서 그때 상황에 맞게 알아서 그려준다. 리액트는 알아서 지가 렌더링을 해주기 때문이다!! 예를 들어 유튜브 옆면에 추천 동영상 탭을 보자. 밑으로 내리면 로딩되면서 더 많은 동영상 리스트가 뜬다.

이런 걸 구현하려면 서버에서 배열 데이터를 받아와서 배열을 랜더링하는 컴포넌트를 만들어 사용하면 된다.

앞에서 배웠던 건 component 만드는 법, props 랑 state 활용하는 법이었다.

이제부턴

1. 컴포넌트에서 배열을 랜더링하는 방법과
2. 리액트로 서버에 리퀘스트를 보내고, 리스폰스를 활용하는 방법과 같이
   **리액트에서 데이터를 다루는 법**을 배워보자.

<br>

## 2. mock 데이터 추가하기

mock 데이터란, 네트워크랑 연결하기 이전에 test 용으로 확인하고 변경할 데이터들을 말한다. 보통 json 파일이다. src 폴더 안에 mock.json 파일을 넣고 활용하자. 참고로 리액트에선 create-react-app 을 사용해 프로젝트를 만드는데, 여기서는 json 파일을 import 하면 js에서 쓸 수 있게 알아서 트랜스파일링 해준다. https://stackoverflow.com/questions/34944099/how-to-import-a-json-file-in-ecmascript-6/39855320#39855320 참고

1. 앞서 배운 대로 폴더를 만들고
2. `npm init react-app .`
3. 폴더 정리하고
4. `npm run start` 해서 새 폴더 만들기.

<br>

#### 시작하기..

1. 리뷰 목록을 보여줄 컴포넌트 만들어보기. src 폴더 아래에 components 폴더를 만든다음 그 아래에 ReviewList.js 파일을 만들어보자. 그리고 App.js에서 ReviewList를 가져오고, index.js에서 App을 render하자.

```js
function ReviewList({ items }) {
  console.log(items);
  return <ul></ul>;
}

export default ReviewList;
```

```js
import ReviewList from "./ReviewList";
import items from "../mock.json";

function App() {
  return (
    <div>
      <ReviewList items={items} />
    </div>
  );
}

export default App;
```

```js
import App from "./components/App";
import ReactDOM from "react-dom";

ReactDOM.render(<App />, document.getElementById("root"));
```

<br>

## 3. map 배열 메소드를 사용해서 배열 요소 하나씩 불러올 때마다 각 요소를 렌더링하자.

ReviewList.js를 아래와 같이 고쳐보자.

map 메소드 안에서 jsx를 리턴하면 여러 jsx 코드를 추가한것처럼 동작한다. 즉, 데이터 1번 2번 3번 ... 134345246번까지 내가 각각 컴포넌트를 만드는 게 아니라 map을 활용해서 각 배열 내 원소를 활용한 jsx 코드를 만들어 추가할 수 있다.

```js
import "./ReviewList.css";

// 요소의 생성 날짜를 출력해줌.
function formatDate(value) {
  const date = new Date(value);
  return `${date.getFullYear()}. ${date.getMonth() + 1}. ${date.getDate()}`;
}

// 영화 하나의 이름, 이미지, 평점 등 정보를 보여주는 함수.
// createAt은 생성한 날짜를 나타내는 숫자형.
function ReviewListItem({ item }) {
  return (
    <div className="ReviewListItem">
      <img className="ReviewListItem-img" src={item.imgUrl} alt={item.title} />
      <div>
        <h1>{item.title}</h1>
        <p>{item.rating}</p>
        <p>{formatDate(item.createdAt)}</p>
        <p>{item.content}</p>
      </div>
    </div>
  );
}

function ReviewList({ items }) {
  return (
    <ul>
      {items.map((item) => {
        return (
          <li>
            <ReviewListItem item={item} />
          </li>
        );
      })}
    </ul>
  );
}

export default ReviewList;
```

<br>

## 4. 최신순 정렬 베스트순 정렬 이렇게 정렬하는 기능을 만들기 위해 sort를 쓰자.

배열 메소드 중에 sort 라는 메소드가 있다.
최신순으로 정렬하려면 날짜 순, 베스트 순 정렬은 rating 값 순으로 정렬하면 될 것이다.

전체 화면에서 요소들이 보이는 방식을 달리 해줄 것이니, App.js에서 수정해주자.

만약 베스트 순으로 보일 거라면 배열을 스코어순으로 정렬한다음 그걸 ReviewList 컴포넌트에게 넘겨주면 된다.

```js
function App() {
  const sortedItems = items.sort((a, b) => b.rating - a.rating);
  return (
    <div>
      <ReviewList items={sortedItems} />
    </div>
  );
}
```

스코어순으로 정렬할지, 최신순으로 정렬할지 선택하고 싶다면 state를 활용하자.
order 값을 createdAt으로 하면 최신순, rating으로 하면 평점순으로 정렬될 것이다.

```js
function App() {
  const [order, setOrder] = useState("createdAt");
  const sortedItems = items.sort((a, b) => b[order] - a[order]);

  return (
    <div>
      <ReviewList items={sortedItems} />
    </div>
  );
}
```

그다음 버튼을 눌러 정렬을 선택하게 해보자. 그러려면 버튼 컴포넌트를 추가하고 거기에 이벤트 핸들러를 넣자.

```js
function App() {
  const [order, setOrder] = useState("createdAt");
  const sortedItems = items.sort((a, b) => b[order] - a[order]);
  const handleNewestClick = () => setOrder("createdAt");
  const handleBestClick = () => setOrder("rating");
  return (
    <div>
      <div>
        <button onClick={handleNewestClick}>최신순</button>
        <button onClick={handleBestClick}>평점순</button>
      </div>
      <ReviewList items={sortedItems} />
    </div>
  );
}
```

<br>

## 5. filter로 아이템 삭제하는 기능 만들기

당연히 글을 삭제하는 기능도 있어야지. filter 메소드를 사용하자. 배열의 filter 기능으로 내가 원하는 글을 찾은 다음, 그 글의 id를 변수에 저장한다음

개어렵네 뭔개솔?

```js

```

<br>

## 6. 주의할 점!! key

배열 요소들을 각각 렌더링할 때 반드시 각 요소는 고유한 key 속성을 가져야 한다. 이거 지정 안 해주면 작동은 하는데 콘솔창에 자꾸 warning이라고 에러 뜸. 에러문 정확한 이름은, Warning Each child in list should have a unique key 라고 하는데, 여기서 child는 map 메소드에서 랜더링한거 말한 거임.

여기서는 예시로 가져온 mock.json 파일에 각 요소에 id 값이 붙어있으니 그걸 key로 쓰자.

이거 키 설정하는 법: ReviewList.js 에서 map 함수 안에 각 item child 리턴해주는 코드 최상단 태그에다 key 값ㅇ 지정함.

```js
function ReviewList({ items, onDelete }) {
  return (
    <ul>
      {items.map((item) => {
        return (
          <li key={item.id}>
            <ReviewListItem item={item} onDelete={onDelete} />
          </li>
        );
      })}
    </ul>
  );
}
```

배열에선 위코드처럼 key 속성 안 주면 에러 난다. 이걸 왜 써야 하는걸까??

예를 들어 한 요소에 무슨 값을 넣었는데 위나 아래나 하여간 다른 요소 삭제하면서 배열 순서 위치가 바뀌었다고 하자. 그럼 key 값이 없으니 input 값은 그냥 배열 위치 그대로에만 있어서 이상해진다. key 값으로 고유한 값을 줘야 그 id를 가진 요소에 바로 적용됨.

참고로 배열 인덱스도 배열 요소 삭제될 때마다 그 안에 각 인덱스에 들어있는 요소가 달라지니까 인덱스도 키로 쓸 수 없다.

<br>
