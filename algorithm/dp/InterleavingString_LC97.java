/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 1, 2017
 */
package algorithm.dp;

public class InterleavingString_LC97 {

	public static void main(String[] args) {

	}

	/***
    two sequence DP
    A good example of how to initialize 2D dp matrix.
    1. state definition
        dp[i][j] means if s1[1..i] and s2[1..j] can interleave s3[1...i+j]
    2. relateion between a problem and its subproblem
        dp[i][j] = true when either following condition holds:
            1) s1[i] equals s3[i + j] and dp[i - 1][j] is true
                Explaination: when s1[i] equals s3[i + j], if s1[1....i-1] and
                              s2[1...i] CAN interleave s3[i + j - 1], then
                              s1[1...i] and s2[1...j] CAN interleave s3[1... (i + j)]
            2) s2[j] equals s3[i + j] and dp[i][j - 1] is true
    3. Initilization:
       sure dp[0][0] = true since "" and "" interleaves ""
       BUT: for the first row and first column of dp, we need to think carefully.
            dp[0][j] means if s2[1..j] can represents s3[1...j], which can be translates
            into determine if s2[1..j].equals(s3[1...j])
       
****/

	public boolean isInterleave(String s1, String s2, String s3) {
	    if (s1 == null || s2 == null || s3 == null || s1.length() + s2.length() != s3.length()) {
	        return false;
	    }
	    
	    int len1 = s1.length(), len2 = s2.length();
	    
	    //dp[i][j] means if s3[0...(i+j-2)] can be interleaved by s1[0...i-1] and s2[0...j-1];
	    boolean[][] dp = new boolean[len1 + 1][len2 + 1];
	    
	    //empty string of s1 and s2 can be used to interleaving empty string of s3
	    dp[0][0] = true;
	    
	    for (int i = 1; i <= len1; i++) {
	        if (s1.charAt(i - 1) == s3.charAt(i - 1)) {
	            dp[i][0] = true;
	        } else {
	            break;
	        }
	    }
	    
	    for (int i = 1; i <= len2; i++) {
	        if (s2.charAt(i - 1) == s3.charAt(i - 1)) {
	            dp[0][i] = true;
	        } else {
	            break;
	        }
	    }
	    
	    for (int i = 1; i <= len1; i++) {
	        for (int j = 1; j <= len2; j++) {
	            int totalLen = i + j;
	            if (s1.charAt(i - 1) == s3.charAt(totalLen - 1) && dp[i - 1][j]) {
	                dp[i][j] = true;
	            }
	            if (s2.charAt(j - 1) == s3.charAt(totalLen - 1) && dp[i][j - 1]) {
	                dp[i][j] = true;
	            }
	        }
	    }
	    
	    return dp[len1][len2];
	}
}
