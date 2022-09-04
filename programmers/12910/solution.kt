class Solution {
    fun solution(arr: IntArray, divisor: Int): IntArray {
        var answer = ArrayList<Int>()
        var idx: Int = 0

        for (e in arr) {
            if (e%divisor == 0) {
                answer.add(e)
            }
        }
        if (answer.isEmpty()) answer.add(-1)

        return answer.toIntArray().sortedArray()
    }
}
