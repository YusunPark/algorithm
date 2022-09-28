function solution(x) {
  var answer = true;
  var tmp = x
  var sum = 0
  var len = String(x)
  for (var i = 0; i< len ; i++) {
      sum += tmp % 10
      tmp = parseInt(tmp/10)
  }
  if (x % sum != 0){
      answer = false
  }
  return answer;
}

console.log(10) //true
