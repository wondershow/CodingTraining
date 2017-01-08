/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 6, 2017
 */
package algorithm.dp;

/**
 * See problem statement at
 * http://www.lintcode.com/en/problem/longest-increasing-continuous-subsequence/#
 * 
 * 
 * 
 * 
 ***/
public class LICS_LintCode {

	public static void main(String[] args) {

	}
	
	public int longestIncreasingContinuousSubsequence(int[] A) {
        if (A == null || A.length == 0) {
            return 0;
        }
        
        int len = A.length;
        int[] dp = new int[2];
        dp[1] = 1;
        
        int res = 1;
        for (int i = 2; i <= len; i++) {
            dp[i % 2] = 1;
            if (A[i - 1] > A[i - 2]) {
                dp[i % 2] = dp[(i - 1) % 2] + 1;
            }
            res = Math.max(res, dp[i % 2]);
        }
        
        dp[1] = 1;
        for (int i = 2; i <= len; i++) {
            dp[i % 2] = 1;
            if (A[i - 1] < A[i - 2]) {
                dp[i % 2] = dp[(i - 1)  % 2] + 1;
            }
            res = Math.max(res, dp[i % 2]);
        }
        
        return res;
    }
}
