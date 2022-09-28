function solution(n) {
  var answer = [];
  var num = String(n).length
  for (var i = num-1 ; i >= 0 ; i--) {
      answer.push(n%10)
      n = parseInt(n / 10)
  }
  return answer;
}

console.log(12345) //	[5,4,3,2,1]