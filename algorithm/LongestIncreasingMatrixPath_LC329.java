/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 15, 2017
 */
package algorithm;
/**
 * See problem statement at 
 * 	https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
 * errors made:
 * 1. Failed to determine if a cell is the lowest cell. (instead
 * found the highest cell)
 * 
 * */
import java.util.Arrays;

public class LongestIncreasingMatrixPath_LC329 {

	public static void main(String[] args) {

	}
	
	int[] distance;
    int[][] directions = new int[][] {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
    public int longestIncreasingPath(int[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return 0;
        }
        
        int res = 0;
        distance = new int[matrix.length * matrix[0].length];
        Arrays.fill(distance, -1);
        
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                res = Math.max(res, search(i, j, distance, matrix));
            }
        }
        
        return res;
    }
    
    private int search(int x, int y, int[] distance, int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        int number = x * n + y;
        if (distance[number] != -1) {
            return distance[number];
        }
        
        if (isSmallest(x, y, matrix)) {
            distance[number] = 1;
            return distance[number];
        }
        
        int res = 0;
        for (int[] dir : directions) {
            int i = x + dir[0];
            int j = y + dir[1];
            if (i >= 0 && j >= 0 && i < m && j < n && matrix[x][y] > matrix[i][j]) {
                res = Math.max(res, search(i, j, distance, matrix) + 1);
            }
        }
        
        distance[number] = res;
        return distance[number];
    }
    
    
    private boolean isSmallest(int x, int y, int[][] matrix) {
        for (int[] dir : directions) {
            int i = x + dir[0];
            int j = y + dir[1];
            if (i >= 0 && j >= 0 && i < matrix.length && j < matrix[0].length && matrix[x][y] > matrix[i][j]) {
                return false;
            }
        }
        return true;
    }

}
