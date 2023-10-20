function solution(s, n) {
  my_str = s.split("");
  let answer = "";

  for (let i = 0; i < my_str.length; i++) {
    if (my_str[i] === " ") {
      answer += " ";
    } else if (my_str[i].charCodeAt() >= 65 && my_str[i].charCodeAt() <= 90) {
      // 대문자 범위인가?
      let asciiNum =
        my_str[i].charCodeAt() + n > 90
          ? my_str[i].charCodeAt() + n - 90 - 1 + 65
          : my_str[i].charCodeAt() + n;
      // console.log(asciiNum);
      answer += String.fromCharCode(asciiNum);
    } else if (my_str[i].charCodeAt() >= 97 && my_str[i].charCodeAt() <= 122) {
      // 소문자 범위인가?
      let asciiNum =
        my_str[i].charCodeAt() + n > 122
          ? my_str[i].charCodeAt() + n - 122 - 1 + 97
          : my_str[i].charCodeAt() + n;
      // console.log(asciiNum);
      answer += String.fromCharCode(asciiNum);
    }
  }
  console.log(answer);
  return answer;
}

solution("wxyz", 1);
