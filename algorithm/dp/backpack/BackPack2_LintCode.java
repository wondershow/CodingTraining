/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 2, 2017
 */
package algorithm.dp.backpack;
/**
 * See problem statement at
 * http://www.lintcode.com/en/problem/backpack-ii/#
 * **/
public class BackPack2_LintCode {

	public static void main(String[] args) {

	}
	
	public int backPackII(int m, int[] A, int V[]) {
        // write your code here
        if (A == null || V == null || m <= 0 || A.length != V.length) {
            return 0;
        }
        
        int len = A.length;
        
        int[][] dp = new int[len + 1][m + 1];
        
        int res = 0;
        /**
        dp[i][j] means what is the maximum value of 
        using first i items limited with j weight
        ***/
        for (int i = 1; i <= len; i++) {
            for (int j = 1; j <= m; j++) {
                dp[i][j] = dp[i - 1][j];
                if (j >= A[i - 1]) {
                    dp[i][j] = Math.max(dp[i][j], 
                         dp[i - 1][j - A[i - 1]] + V[i - 1]);
                }
                res = Math.max(res, dp[i][j]);
            }
        }
        
        return res;
    }
}
