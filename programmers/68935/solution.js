const solution = (n) => {
  return parseInt([...n.toString(3)].reverse().join(''), 3);
};

result = solution(125);

console.log(result);
