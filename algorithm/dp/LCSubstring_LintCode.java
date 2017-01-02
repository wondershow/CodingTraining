/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 1, 2017
 */
package algorithm.dp;

/**
 * See the problem statement at 
 * http://www.lintcode.com/en/problem/longest-common-substring/#
 * */
public class LCSubstring_LintCode {

	public static void main(String[] args) {

	}
	
	/**
	 * Typicall two sequence DP. Need to pay attention
	 * to the function between i and i - 1
	 * */
	public int longestCommonSubstring(String A, String B) {
        // write your code here
        if (A == null || B == null || A.length() == 0 || B.length() == 0) {
            return 0;
        }
        
        int len1 = A.length();
        int len2 = B.length();
        int[][] dp = new int[len1 + 1][len2 + 1];
        
        //dp[i][j] means the longest common substring
        //ends at i and j
        int res = 0;
        for (int i = 1; i <= len1; i++)
            for (int j = 1; j <= len2; j++) {
                if (A.charAt(i - 1) == B.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                }  else {
                    dp[i][j] = 0;
                }
                res = Math.max(res, dp[i][j]);
            }
            
        return res;
    }

}
