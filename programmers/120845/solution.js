function solution(box, n) {
  return box.map((i) => parseInt(i/n)).reduce((a,b) => a*b);
}

console.log(solution([10, 8, 6],3))	// 12