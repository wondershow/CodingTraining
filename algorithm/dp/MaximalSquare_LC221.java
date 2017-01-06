/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 6, 2017
 */
package algorithm.dp;

/**
 * See the problem statement at:
 * https://leetcode.com/problems/maximal-square/
 * **/
public class MaximalSquare_LC221 {

	public static void main(String[] args) {

	}
	
	public int maximalSquare(char[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return 0;
        }
        
        int rows = matrix.length, cols = matrix[0].length;
        int[][] dp = new int[2][cols + 1];
        
        int res = 0;
        for (int i = 1; i <= rows; i++) {
            for (int j = 1; j <= cols; j++) {
                if (matrix[i - 1][j - 1] == '0') {
                    dp[i % 2][j] = 0;
                } else {
                    dp[i % 2][j] = 1 + Math.min(dp[(i - 1) % 2][j - 1],
                               Math.min(dp[i % 2][j - 1], dp[(i - 1) % 2][j]));
                }
                res = Math.max(dp[i % 2][j] * dp[i % 2][j], res);
            }
        }
        
        return res;        
    }
}
