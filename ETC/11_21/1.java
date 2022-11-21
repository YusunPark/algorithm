
import java.io.*;
import java.util.stream.Stream; 
import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;


class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String n = br.readLine();
		List<List<String>> grid = new ArrayList<>();
		List<List<String>> newGrid = new ArrayList<>();

		for (int i = 0; i < Integer.parseInt(n); i++) {
			List<String> row = new ArrayList<String>(Arrays.asList(br.readLine().split("")));
			grid.add(row);
		}
		
		
		
		while(grid.size() !=  1) {
			for (int y = 0; y < grid.size(); y = y+2) {
				List<String> newRow = new ArrayList<String>();

				for (int x = 0; x < grid.size(); x = x+2) {			
					if (grid.get(y).get(x).equals(grid.get(y).get(x+1)) &&  grid.get(y+1).get(x).equals( grid.get(y+1).get(x+1)) && grid.get(y).get(x+1).equals(grid.get(y+1).get(x))) {
						newRow.add(grid.get(y).get(x));
					} else{
						String tmp = '(' + grid.get(y).get(x) + grid.get(y).get(x+1) + grid.get(y+1).get(x)+ grid.get(y+1).get(x+1) +')';
						newRow.add(tmp);
					}
				}			
				newGrid.add(newRow);
			}
			grid = newGrid;
			newGrid = new ArrayList<>();

		}
		System.out.println(grid.get(0).get(0));

	} 
}


