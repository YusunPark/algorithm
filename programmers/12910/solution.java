import java.util.Arrays;

class Solution {
  public int[] solution(int[] arr, int divisor) {
      return Arrays.stream(arr).filter(factor -> factor % divisor == 0).toArray();
  }
}
