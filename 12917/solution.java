import java.util.Arrays;
import java.util.Collections;

class Solution {
    public String solution(String s) {
        String[] stringArr = s.split("");
        Arrays.sort(stringArr);
        Collections.reverse(Arrays.asList(stringArr));
        return String.join("", stringArr);
    }
}
