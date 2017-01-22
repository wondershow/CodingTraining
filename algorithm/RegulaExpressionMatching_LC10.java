/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 22, 2017
 */
package algorithm;
/**
 * https://leetcode.com/problems/regular-expression-matching/
 * 
 * For this problem it is a dp solution.
 * 1. state definition:
 *    dp[i][j] means if s(0...i-1) matches p(0...j-1);
 * 2. state transition function
 *    2.1 if s (i - 1) == p(j - 1) || p (j - 1) == '.'
 *        dp[i][j] = dp[i - 1][j - 1];
 *    2.2 if p(j - 1) == '*'
 *        2.2.1 s(i - 1) != p(j - 2) && p (j - 2) != '.'
 *              dp[i][j] = dp[i - 1][j - 2];
 *              when the latest chars dont mactch, the best thing
 *              we can do is to let '*' represents zero characters
 *              and let p(0...j - 3) to match s(0...i - 1) 
 *        2.2.2 s(i - 1) == p(j - 2) || p (j - 2) != '.'
 *        		dp[i][j] = dp[i][j - 2] || dp[i - 1][j - 2] || 
 *                         dp[i - 1][j];
 *               explain: a)a vs aa* : dp[i][j] = dp[i][j - 2]
 *                        b)ba vs ba*  dp[i][j] = dp[i - 1][j - 2]
 *						 c)baa vs ba*  dp[i][j] = dp[i - 1][j]
 *  Initialization:
 *       dp[0][0] = true ("" always matches "")
 *       dp[0][Even index] = true if sees '*' at continues even 
 *               index.
 * 
 *
 * **/
public class RegulaExpressionMatching_LC10 {

	public static void main(String[] args) {

	}
	
	public boolean isMatch(String s, String p) {
        if (s == null || p == null) {
            return false;
        }
        
        int len1 = s.length(), len2 = p.length();
        boolean[][] dp = new boolean[len1 + 1][len2 + 1];
        dp[0][0] = true;
        
        //initialization, i skips 2 at each iteration
        for (int i = 2; i <= len2; i += 2) {
            if (p.charAt(i - 1) == '*') {
                dp[0][i] = true;
            } else {
               break;
            }
        }
        
        
        for (int i = 1; i <= len1; i++) {
            for (int j = 1; j <= len2; j++) {
                if (p.charAt(j - 1) == '.' || s.charAt(i - 1) == p.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else if (p.charAt(j - 1) == '*') {
                    if (s.charAt(i - 1) != p.charAt(j - 2) && p.charAt(j - 2) != '.') {
                        dp[i][j] = dp[i][j - 2];
                    } else 
                        dp[i][j] = dp[i][j - 2] || dp[i - 1][j - 2] || dp[i - 1][j];
                }
            }
        }
        
        return dp[len1][len2];
    }
}
