var prev = -1
var answer = [];

function p(value) {
    answer.push(value)
    prev = value
}

function solution(arr)
{
    arr.map((i)=> (i != prev) ? p(i) : null )    
    return answer;
}

console.log(solution([1,1,3,3,0,1,1]))