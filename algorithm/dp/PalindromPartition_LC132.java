/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 1, 2017
 */
package algorithm.dp;

import java.util.Arrays;

public class PalindromPartition_LC132 {

	public static void main(String[] args) {
	}
	
	public int minCut(String s) {
        if (s == null || s.length() <= 1) {
            return 0;
        }
        
        int len = s.length();
        boolean[][] isPalindrome = preCompute(s);
        
        int[] dp = new int[len + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = -1;
        
        for (int i = 1; i <= len; i++) {
            for (int j = i - 1; j >= 0; j--) {
                if (dp[j] != Integer.MAX_VALUE && isPalindrome[j][i - 1]) {
                    dp[i] = Math.min(dp[i], dp[j] + 1);
                }
            }
        }
        
        return dp[len];
    }
    
    /***
        cache the isPalindrome(s, i, j) 
        into a 2D hash array.
    **/
    private boolean[][] preCompute(String s) {
        int len = s.length();
        boolean[][] res = new boolean[len][len];
        
        for (int i = 0; i < len; i++) {
            res[i][i] = true;
        }
        
        for (int offset = 1; offset < len; offset++) {
            for (int i = 0; i < s.length(); i++) {
                int j = i + offset;
                if (j >= s.length()) { 
                    break; 
                }
                if (s.charAt(i) == s.charAt(j)) {
                    if (i + 1 >= j - 1 || res[i + 1][j - 1]) {
                        res[i][j] = true;
                    }
                }
            }
        }
        return res;
    }

}
