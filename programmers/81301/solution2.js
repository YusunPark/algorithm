function solution(s) {
  let answer = s
  num_str = ["zero","one","two","three","four","five","six","seven","eight","nine"]
  for (let i = 0; i<num_str.length; i++){
      answer = answer.split(num_str[i]).join(i)
  }
  
  return Number(answer);
}