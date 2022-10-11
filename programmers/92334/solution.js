function solution(id_list, report, k) {
  var obj = {}
  var answer = [];

  id_list.forEach((id) => obj[id] = {cnt_report: new Set([]), cnt_email : 0})
  report.forEach((s) => {
      str = s.split(" ")
      obj[str[1]].cnt_report.add(str[0])
  })
  
  id_list.forEach((id) => {
      obj[id].cnt_report.size < k ? null : obj[id].cnt_report.forEach((i)=> obj[i].cnt_email++)
  })
  
  id_list.forEach((id) => {
      answer.push(obj[id].cnt_email)
  })
  
  return answer;
}

console.log(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)) // [2,1,1,0]
console.log(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3)) //	[0,0]z