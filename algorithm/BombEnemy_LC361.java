/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 23, 2017
 */
package algorithm;

import java.util.Arrays;

/**
 * https://leetcode.com/problems/bomb-enemy/
 * 
 * Over all roadmap;
 * scan each line with a two ptrs subroutine:
 * the fast ptr goes to either to the end of the row or next wall,
 * in this process, count how many enemies in that row.
 * after fast ptr stops, move slow prt one by one (from left to right),
 * at each col j, if we have not counted how many vertical enemies that cell
 * can affect, count it(another vertical subroutine). keep a max
 * result in this process
 * 
 * Mistakes made:
 * 1. in the vertical count function, each time the started row should 
 * be last updated row + 1, not the current row!
 * 2. in the vertical count function, we need to check if the updated
 * count has covered up to current row. see code below, use while not 
 * if!
 * 3. One thing to remember, in the two ptr solution: if when the 
 *    slow ptr hits a wall, we need to move the fast ptr to the next 
 *    position and reset the rowcount.
 * 
 * **/
public class BombEnemy_LC361 {

	public static void main(String[] args) {

	}

	public int maxKilledEnemies(char[][] grid) {
        if (grid == null || grid.length == 0 || grid[0].length == 0) {
            return 0;
        }
        
        int m = grid.length, n = grid[0].length;
        
        int[] verticalCount = new int[n];
        int[] verticalPointer = new int[n];
        Arrays.fill(verticalPointer, -1);
        
        int res = 0;
        for (int i = 0; i < m; i++) {
            int rowCount = 0;
            for (int slow = 0, fast = 0; slow < n; slow++) {
                while (fast < n) {
                    if (grid[i][fast] == 'W') break;
                    if (grid[i][fast++] == 'E') rowCount++; 
                }
                if (grid[i][slow] == '0') {
                    int vcount = countVertical(i, slow, verticalCount, verticalPointer, grid);
                    res = Math.max(res, rowCount + vcount);
                }
                if (grid[i][slow] == 'W') {
                    fast++;
                    rowCount = 0;
                }
            }
        }
        
        return res;
    }
    
    private int countVertical(int row, int col, int[] verticalCount, int[] verticalPointer, char[][] grid) {
        if (verticalPointer[col] >= row) return verticalCount[col];
        if (grid[row][col] == 'W') return 0;
        
        //Note, this while is very important, since one time of vertical search 
        // may not cover the current cell of that column, since there may be
        //more than 2 walls from the last terminated search place to the current cell
        while (verticalPointer[col] <= row) {
            verticalCount[col] = 0;
            
            //the beginning of the row should be carefully set
            int r = verticalPointer[col] + 1;
            
            for (; r < grid.length && grid[r][col] != 'W'; r++) {
                if (grid[r][col] == 'E') {
                    verticalCount[col]++;
                }
            }
            verticalPointer[col] = r;
        }
        return verticalCount[col];
    }
}
