function solution(progresses, speeds) {
  var answer = [];
  var day = 0
  var count = 0
  progresses.map((v,i) => {
      if (Math.ceil((100 - v)/speeds[i]) > day) {
          answer.push(count)
          day = Math.ceil((100 - v)/speeds[i]) 
          count = 1
          
      } else {
          count++
      }
  })
  answer.push(count)
  return answer.slice(1);
}

console.log(solution([93, 30, 55], [1, 30, 5])) // [2, 1]