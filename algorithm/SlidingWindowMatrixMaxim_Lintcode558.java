/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Feb 14, 2017
 */
package algorithm;

/**
 * http://www.lintcode.com/en/problem/sliding-window-matrix-maximum/#
 * This is a 2D slding window problem. 
 * Mistakes made:
 * 1. my first thought is something like 2D Deque, where we can move
 * elements from four sides of a matrix. but this idea is really difficult
 * to express with code.
 * 2. By reading the solution, I feel that one key point missing in my 
 * mind is that, a submatrix(a,b to i,j) sum can be expressed by 
 * sum(0,0,i,j) - sum(0,0,i, b-1) - sum(0,0,a-1,j) + sum(0,0,a-b,b-1)
 * When it comes to 2d submatrix sum, always keep this point in 
 * your mind!
 * 
 * ***/
public class SlidingWindowMatrixMaxim_Lintcode558 {
	public int maxSlidingMatrix(int[][] matrix, int k) {
        // Write your code here
        if (matrix == null) return 0;
        
        int m = 0;
        if (matrix.length == 0 || matrix.length < k) return 0;
        
        int n = 0;
        if (matrix[0].length == 0 || matrix[0].length < k) return 0;
        
        m = matrix.length;
        n = matrix[0].length;
        
        int[][] sum = new int[m + 1][n + 1];
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                sum[i][j] = sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1]
                            + matrix[i - 1][j - 1];
            }
        }
        
        int res = Integer.MIN_VALUE;
        
        for (int i = k; i <= m; i++) {
            for (int j = k; j <= n; j++) {
                int sumk = sum[i][j] - sum[i - k][j] - sum[i][j - k] 
                           + sum[i - k][j - k];
                res = Math.max(sumk, res);
            }
        }
        
        return res;
    }
}
