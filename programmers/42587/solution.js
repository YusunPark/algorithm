function solution(priorities, location) {
  var loc = location
  var max = Math.max(...priorities)
  var idx = 0 // 출력된 인덱스
  while(1) {
      if (priorities[0] < max) {
          priorities.push(priorities.shift())
          loc == 0 ? loc = priorities.length - 1 : loc--
      } else {                // 최대값인 경우
          idx++               // 출력된 순서 업데이트
          priorities.shift()  // 출력된 아이 삭제
          max = Math.max(...priorities) // 최대값 업데이트
          // loc == 0 => 바라보는 애가 출력되었다.
          if (loc === 0) {    
              break
          } else { 
              loc--
          }
      }
  }
  return idx
}


console.log(solution([2, 1, 3, 2], 2)) //1