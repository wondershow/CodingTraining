/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 2, 2017
 */
package algorithm.dp.backpack;

/**
 * see problem statement at
 * http://www.lintcode.com/en/problem/backpack-iii/#
 * This is a variation of backpack2. 
 * State transition function is different.
 * */
public class Backpack3_LintCode {

	public static void main(String[] args) {

	}

	public int backPack3(int[] A, int[] V, int m) {
        // Write your code here
        if (m <= 0 || A == null || V == null || A.length != V.length) {
            return 0;
        }
        
        int len = A.length;
        int[][] dp = new int[len + 1][m + 1];
        
        int res = 0;
        for (int i = 1; i <= len; i++) {
            for (int j = 1; j <= m; j++) {
                dp[i][j] = dp[i - 1][j];
                if (j >= A[i - 1]) {
                    dp[i][j] = Math.max(dp[i][j], 
                    dp[i][j - A[i - 1]] + V[i - 1]);
                }
                res = Math.max(res, dp[i][j]);
            }
        }
        
        return res;
    }
}
