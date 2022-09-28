function solution(num) {
  var answer = -1;
  
  for (var i = 0; i < 500; i++) {
      if (num == 1) {
          answer = i
          break
      }
      if (num % 2 == 0) num = num/2
      else num = num*3 +1
  }
  
  return answer;
}

console.log(16) // 4