/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 22, 2017
 */
package algorithm;
/**
 * https://leetcode.com/problems/wildcard-matching/
 * DP solution
 * 1. state definition
 * 
 * **/
public class WildCardMatching_LC44 {

	public static void main(String[] args) {

	}
	
	
	/**
	 * DP solution:
	 * 1. state definition
	 *    dp[i][j]  means if s(1...i) matches p(1...j).
	 * 2. transition function
	 *    when s(i) == p(j) or p(j) is '?'
	 *         dp[i][j] = dp[i - 1][j - 1];
	 *    when p(j) is '*'
	 *         dp[i][j] =  dp[i - 1][j - 1] (* matches only 1 char)
	 *                  || dp[i][j - 1] (* matches 0 chars)
	 *                  || dp[i - 1][j] (* matches more than one char)
	 * 3. Initialization:
	 *    dp[0][0] = true
	 *    dp[0][i] = true  if p(1) to p(i) are all '*'
	 * **/
	public boolean isMatch1(String s, String p) {
        if (s == null || p == null) {
            return false;
        }
        
        int len1 = s.length(), len2 = p.length();
        
        boolean[][] dp = new boolean[len1 + 1][len2 + 1];
        
        dp[0][0] = true;
        
        for (int i = 1; i <= len2; i++) {
            if (p.charAt(i - 1) != '*') {
                break;
            }
            dp[0][i] = true;
        }
        
        for (int i = 1; i <= len1; i++) {
            for (int j = 1; j <= len2; j++) {
                if (s.charAt(i - 1) == p.charAt(j - 1) || p.charAt(j - 1) == '?') {
                    dp[i][j] = dp[i - 1][j - 1];
                } else if (p.charAt(j - 1) == '*') {
                    dp[i][j] = dp[i - 1][j - 1] || dp[i - 1][j] || dp[i][j - 1];
                }
            }
        }
        
        return dp[len1][len2];
    }

}
