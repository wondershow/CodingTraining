/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 6, 2017
 */
package algorithm.dp;
/**
 * See problem statements at:
 * http://www.lintcode.com/en/problem/coins-in-a-line/#
 * **/
public class CoinsInALine_LintCode {

	public static void main(String[] args) {

	}
	
	/**
	 * 1. state representation 
	 *   f[i] means if player is going to pick first when there are 
	 *    i coins left, he will win or lose when the game is over
	 * 2. state transition
	 *   f[i] = (!f[i - 2] && !f[i - 3]) || (!f[i - 4] && !f[i - 3])
	 * 
	 * ***/
	public boolean firstWillWin1(int n) {
        
        if (n <= 0) return false;
        if (n == 1) return true;
        if (n == 2) return true;
        if (n == 3) return false;
        
        boolean[] dp = new boolean[n + 1];
        for (int i = 4; i <= n; i++) {
            dp[i] = (!dp[i - 2] && !dp[i - 3]) ||
                    (!dp[i - 4] && !dp[i - 3]);
        }
        
        return dp[n];
    }
	
	/**
	 * 1. state representation 
	 *   f[i] means if player is picking i-th coin, what
	 *   is the result
	 * 2. state transition
	 * 	 f[i] = !f[i - 1] && !f[i - 2];
	 * 
	 ****/
	public boolean firstWillWin2(int n) {
        
        if (n <= 0) return false;
        if (n == 1) return true;
        if (n == 2) return true;
        
        boolean[] dp = new boolean[n + 1];
        dp[0] = false;
        dp[1] = true;
        dp[2] = true;
        
        for (int i = 3; i <= n; i++) {
            dp[i] = !dp[i - 1] || !dp[i - 2];
        }
        
        return dp[n];
    }
}
