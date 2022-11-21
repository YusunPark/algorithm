import java.io.*;
import java.util.stream.Stream; 
import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		List<String> str = new ArrayList<String>(Arrays.asList(br.readLine().split("")));
		List<String> key = new ArrayList<String>(Arrays.asList(br.readLine().split("")));

		int index = 0;
		int count = 0;
		int left = 0;
		int right = 0;
		
		boolean flag = false;
		int size = str.size()/2;
		while(key.size() > 0) {
			int findIndex = str.indexOf(key.get(0));
			if (findIndex == -1) {
				flag = true;
				break;
		  } else if (findIndex == index) {

				count++;
				key.remove(0);
			} else if (findIndex > index) {

				if((findIndex - index) <= size){
					right += (findIndex - index);
					count += (findIndex - index);
					index = findIndex;
				} else {

					left += (size*2 - findIndex+1) + index;
					count += (size*2 - findIndex+1) + index;
					index = findIndex;
				}
				
			} else if (findIndex < index ) {
				if((index - findIndex) <= size){
					left += (index - findIndex);
					count += (index - findIndex);
					index = findIndex;
				} else {

					right += (size*2 - index+1) + findIndex;
					count += (size*2 - index+1) + findIndex;
					index = findIndex;
				}
				
			}
		}
		if (flag) {
			System.out.println(-1);
		} else {
			System.out.printf("%d %d %d", count, right, left );

		}
		
	}
}

