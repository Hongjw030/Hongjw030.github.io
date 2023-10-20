function solution(s, n) {
  // 초깃값 설정.
  let answer = "";
  const A_ASCII = 65;
  const Z_ASCII = 90;
  const a_ASCII = 97;
  const z_ASCII = 122;

  for (let i = 0; i < s.length; i++) {
    let originASCII = s[i].charCodeAt();
    // 공백인가?
    if (my_str[i] === " ") {
      answer += " ";
    } else if (originASCII >= A_ASCII && originASCII <= Z_ASCII) {
      // 대문자 범위인가?
      let newASCII =
        originASCII + n > Z_ASCII
          ? originASCII + n - Z_ASCII - 1 + A_ASCII
          : originASCII + n;
      answer += String.fromCharCode(newASCII);
    } else if (originASCII >= a_ASCII && originASCII <= z_ASCII) {
      // 소문자 범위인가?
      let newASCII =
        originASCII + n > z_ASCII
          ? originASCII + n - z_ASCII - 1 + a_ASCII
          : originASCII + n;
      answer += String.fromCharCode(newASCII);
    }
  }
  return answer;
}
