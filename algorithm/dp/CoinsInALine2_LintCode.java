/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 7, 2017
 */
package algorithm.dp;

/**
 * See problem statement at
 * http://www.lintcode.com/en/problem/coins-in-a-line-ii/#
 * 
 * Game DP.
 * */
public class CoinsInALine2_LintCode {

	public static void main(String[] args) {
	}
	
	/**
	 * Solution 1. 
	 * 1. state define: 
	 *    f[i], when there are i coins left, the player who needs to
	 *    pick first, what is his maximum coin sum when game is over
	 * 2. state transition
	 *    f[i] = Math.max(a, b);
	 *         a = Math.min(f[i - 2], f[i - 3]) + coins[n - i];
	 *         b = Math.min(f[i - 3], f[i - 4]) + coins[n - i - 1];
	 *    explaination:
	 *    	   when i coins left, there are two options for this player:
	 *    	   a. pick one coin (value is coins[n - i]), then i - 1 coins
	 * 			  left, the opponent will definitely pick a better(larger) option
	 *            which is the larger one in f[i - 2] (pick one) and 
	 *            f[i - 3]. so in case a, his final score will be the smaller
	 *            one (the leftover of f[i - 2] and f[i - 3] after opponent's pick)
	 *       	  plus coins[n - i]
	 *         b. similar
	 * 3. Initialization.
	 * 	  dp[0] = 0;
	 *    dp[1] = last coin
	 *    dp[2] = last coin + 2nd to last
	 *    dp[3] = 2nd to last + 3rd to last
	 * 4. Answer:
	 *    dp[len] > sum / 2;
	 ****/
	public boolean firstWillWin1(int[] values) {
        int len = values.length;
        long sum = 0;
        for (int i = 0; i < len; i++) {
            sum += values[i];
        }
        
        if (len == 1 || len == 2) return true;
        else if (len == 3) return (values[0] + values[1] > sum / 2);
        
        long[] dp = new long[4];
        
        dp[0] = 0;
        dp[1] = values[len - 1];
        dp[2] = values[len - 1] + values[len - 2];
        dp[3] = values[len - 2] + values[len - 3];
        
        for (int i = 4; i <= len; i++) {
            dp[i % 4] = Math.max(Math.min(dp[(i - 2) % 4], dp[(i - 3) % 4]) + values[len - i],   
                             Math.min(dp[(i - 3) % 4], dp[(i - 4) % 4]) + 
                             values[len - i + 1] + values[len - i]);
        }
        
        return dp[len % 4] > sum / 2;
    }
	
	/**
	 * Solution 2.
	 * 1. state:
	 *    when i coins left, the person who picks i-th coin, what is his maximum sum value
	 * 2. state transition:
	 *    f[i] = Math.max(sum[i] - f[i - 1], sum[i] - f[i - 2]);
	 * 3. initialization
	 *    f[0] = 0;
	 *    f[1] = last one
	 *    f[2] = last one + 2nd to last
	 * 4. answer
	 *    f[n] > sum / 2;
	 * **/
	public boolean firstWillWin2(int[] values) {
        int len = values.length;
        if (len <= 2) return true;
        long[] sum = new long[len + 1];
        
        for (int i = 1; i <= len; i++) {
            sum[i] += sum[i - 1] + values[len - i];
        }
        
        long[] dp = new long[3];
        dp[0] = 0;
        dp[1] = values[len - 1];
        dp[2] = values[len - 2] + values[len - 1];
        
        for (int i = 3; i <= len; i++) {
            dp[i % 3] = Math.max(sum[i] - dp[(i - 1) % 3], 
                                 sum[i] - dp[(i - 2) % 3]);
        }
        
        return dp[len % 3] > sum[len] / 2;
    }
	
	/**
	 * solutions, top down memoization search. 
	 * state definition same as solution 1.
	 * **/
	public boolean firstWillWin3(int[] values) {
        
        long sum = 0;
        for (int n : values) {
            sum += n;
        }
        
        Long[] dp = new Long[values.length + 1];
        dp[0] = (long)0;
        
        return sum < 2 * topDown(values, dp, values.length);
    }
    
    /**
        dp[i] max value when there are i coins left,
    ***/
    private long topDown(int[] values, Long[] dp, int i) {
        if (i == 0) return (long)0;
        else if (i == 1) return (long) values[values.length - 1];
        else if (i == 2) return (long) (values[values.length - 1]
                         + values[values.length - 2]);
        else if (i == 3) return (long) (values[values.length - 3]
                         + values[values.length - 2]);
        if (dp[i] != null) {
            return dp[i];
        }
        
        
        dp[i] = Math.max(
                    Math.min(topDown(values, dp, i - 2)
                    , topDown(values, dp, i - 3)) + values[values.length - i],
                     Math.min(topDown(values, dp, i - 4)
                    , topDown(values, dp, i - 3)) + values[values.length - i]
                    + values[values.length - i + 1]);
        
        return dp[i];
    }
}
