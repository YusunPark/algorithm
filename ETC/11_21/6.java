import java.io.*;
import java.util.stream.Stream; 
import java.util.Arrays;

class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
		
		int[] seatNum = Stream.of(input.split(" ")).mapToInt(Integer::parseInt).toArray();
		Arrays.sort(seatNum);
		int minValue = 999999999;
		int start = 0;
		int end = 0;
		for (int i = 0; i < seatNum.length-1; i++) {
			if(seatNum[i+1] - seatNum[i] < minValue) {
				minValue = seatNum[i+1] - seatNum[i];
				start = seatNum[i];
				end = seatNum[i+1];
			}
		}

		System.out.printf("%d %d",start, end);
	}
}