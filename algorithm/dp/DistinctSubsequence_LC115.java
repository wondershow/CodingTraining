/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 1, 2017
 */
package algorithm.dp;

public class DistinctSubsequence_LC115 {

	public static void main(String[] args) {

	}

	public int numDistinct(String s, String t) {
        if (s == null || t == null || s.length() == 0 || t.length() == 0 || s.length() < t.length()) {
            return 0;
        }
        
        int len1 = t.length(), len2 = s.length();

        int[][] dp = new int[len1 + 1][len2 + 1];
        
        for (int i = 0; i <= len2; i++) {      
            dp[0][i] = 1;
        }
        
        /***
            This problem is tricky:
            
            1. state representation
            dp[i][j] means how many t(0..i-1) as subsequence in s(0....j-1);
            
            2. relations between a problem and its subproblems
            so when t(i) != s(j), dp[i][j] = dp[i][j - 1] 
                    since index i and j do not match, the best thing we can do is to 
                    have t(0...i-1) find its appearances time in s(0...j-2);
            
               when t(i) == s(j), dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1], here we have 
                    two ways to create subsequences of t(0...i-1) out of s(0..j-1). 
                    1) we can count int how many subsequences of t(0....i-2) in s(0...j-2)
                    2) still we can "ignore" s(j - 1), count how many t(0..i-1) as subsequences in s(0...j-2)
            3. initializations.
               if t is empty(""), then it is a subsequence of any string for one time.
               so dp[0][j] = 1;
               
        NOTE: for this problem, dp[][] array population order matters. 
               We have to match t(0...i) to the whole string of S. then
               we can do next level t(0...i+1). 
               If it is other order, we match s(0...i) to the whole string of T.
               it seems to be really hard to figure out the relations between 
               a problem and its subproblems
        ***/
        for (int i = 1; i <= len1; i++) {
            for (int j = 1; j <= len2; j++) {
                if (t.charAt(i - 1) != s.charAt(j - 1)) {
                    dp[i][j] = dp[i][j - 1];
                } else {
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1];
                }
            }
        }
        
        return dp[len1][len2];
    }
}
