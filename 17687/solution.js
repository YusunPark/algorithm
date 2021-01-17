const TEST_CASE = [
  [2, 4, 2, 1],
  [16, 16, 2, 1],
  [16, 16, 2, 2],
];

const solution = (n, t, m, p) => {
  let answer = "";
  let counter = 0;
  while (t * m > answer.length) {
    answer += counter.toString(n).toUpperCase();
    ++counter;
  }
  return answer
    .split("")
    .filter((x, i) => (i % m) + 1 === p)
    .slice(0, t)
    .join("");
};

TEST_CASE.forEach((inputs) => console.log(solution(...inputs)));
