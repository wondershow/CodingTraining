/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 6, 2017
 */
package algorithm.dp;

/**
 * See problem statement at:
 * http://www.lintcode.com/en/problem/longest-increasing-continuous-subsequence-ii/
 * 
 * This is a pretty interesting DP problem. In 
 * this DP problem, it is hard to figure out the 
 * transition function with typical bottom-up  
 * DP paradigm. So we need to search from solution towards
 * atomic start points. In the middle of the searching process
 * the results will be memoized. 
 * **/
public class LICS2_LintCode {

	public static void main(String[] args) {

	}
	int[][] directions = new int[][] {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
    public int longestIncreasingContinuousSubsequenceII(int[][] A) {
        // Write your code here
        if (A == null || A.length == 0 || A[0].length == 0) {
            return 0;
        }
        int[][] dp = new int[A.length][A[0].length];
        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < A[0].length; j++) {
                dp[i][j] = -1;
            }
        }
        
        int res = 0;
        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < A[0].length; j++) {
                if (dp[i][j] == -1) {
                    dp[i][j] = search(A, i, j, dp);
                    res = Math.max(res, dp[i][j]);
                }
            }
        }
        
        return res;
    }
    
    private int search(int[][] A, int i, int j, int[][] dp) {
        if (dp[i][j] != -1) {
            return dp[i][j];
        }
        dp[i][j] = 1;
        for (int[] dir : directions) {
            int x = i + dir[0];
            int y = j + dir[1];
            if (x < 0 || y < 0 || x >= A.length
                  || y >= A[0].length || A[x][y] <= A[i][j]) {
                continue;
            }
            dp[i][j] = Math.max(dp[i][j], 1 + search(A, x, y, dp));
        }
        
        return dp[i][j];
    }
}
