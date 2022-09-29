function solution(sizes) {
  let max = 0
  let min = 0
  for (let i = 0; i < sizes.length ; i++) {
      if (max < Math.max(...sizes[i])) max = Math.max(...sizes[i])
      if (min < Math.min(...sizes[i])) min = Math.min(...sizes[i])

  }

  width = max * min

  return width;
}