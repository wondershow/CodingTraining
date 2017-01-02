/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 1, 2017
 */
package algorithm.dp;
/**
 * See problem statement at 
 * http://www.lintcode.com/en/problem/longest-common-subsequence/#
 * **/
public class LCS_LintCode {

	public static void main(String[] args) {

	}
	
	/**
	 * Very simple and straightforward 2-sequence DP
	 * **/
	public int longestCommonSubsequence(String A, String B) {
        // write your code here
        if (A == null || B == null || A.length() == 0 || B.length() == 0) {
            return 0;
        }
        
        int len1 = A.length(), len2 = B.length();
        
        int[][] dp = new int[len1 + 1][len2 + 1];
        
        for (int i = 1; i <= len1; i++) {
            for (int j = 1; j <= len2; j++) {
                if (A.charAt(i - 1) == B.charAt(j - 1)) {
                    dp[i][j] = Math.max(dp[i - 1][j - 1] + 1,
                        Math.max(dp[i - 1][j], dp[i][j - 1]));                    
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j - 1],
                        Math.max(dp[i - 1][j], dp[i][j - 1]));
                }
            }
        }
                    
        return dp[len1][len2];
    }
}
