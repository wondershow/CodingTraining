/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 1, 2017
 */
package algorithm.dp;

public class UniquePaths_LC62 {

	public static void main(String[] args) {

	}
	/**
	 * Typical Matrix DP.
	 * Trick here uses only 1D dp array instead of 2d
	 * ***/
	public int uniquePaths(int m, int n) {
        if (m == 0 || n== 0) return 0;
        int[] dp = new int[n];
        
        dp[0] = 1;
        for (int i = 0; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (i == 0) {
                    dp[j] = dp[j - 1];
                } else {
                    dp[j] += dp[j - 1];
                }
            }
        }
        
        return dp[n - 1];
    }
}
