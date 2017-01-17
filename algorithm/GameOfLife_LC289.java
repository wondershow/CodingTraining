/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 17, 2017
 */
package algorithm;
/**
 * https://leetcode.com/problems/game-of-life/
 * 
 * errors made:
 * had no idea on how to update cell info while keep the original
 * cell info. 
 * The key is that the cell info is 0 or 1 while the element in the
 * cell is a 32-bit int. So it is a "waste" to store a 0-1
 * info with a 32-bit integer. we can use other bits to store more 
 * information.
 * 
 * **/
public class GameOfLife_LC289 {

	public static void main(String[] args) {

	}
	
	
	public void gameOfLife(int[][] board) {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                int live = countNeighbors(board, i, j);
                if (board[i][j] == 1 && (live == 2 || live == 3)) {
                    board[i][j] = 3;
                }
                if (board[i][j] == 0 && live == 3) {
                    board[i][j] = 2;
                }
            }
        } 
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                board[i][j] >>= 1;
            }
        }
    }
    
    
    private int countNeighbors(int[][] board, int x, int y) {
        int res = 0, i = 0, j = 0;
        for (i = Math.max(0, x - 1); i <= Math.min(board.length - 1, x + 1); i++) {
            for (j = Math.max(0, y - 1); j <= Math.min(board[0].length - 1, y + 1); j++) {
                res += board[i][j] & 1;
            }
        }
        
        res -= board[x][y] & 1;
        return res;
    }
}
