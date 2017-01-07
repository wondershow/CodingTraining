/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 7, 2017
 */
package algorithm.dp;
/**
 * See problem statement at:
 * http://www.lintcode.com/en/problem/coins-in-a-line-iii/#
 * **/
public class CoinsInALine3_LintCode {

	public static void main(String[] args) {
		
	}
	
	/**
	 * Solution 1 (Bottom up DP)
	 * 1. state definition:
	 * 	  dp[i][j] when values[i...j] are the leftover part to choose from,
	 *    what is the maximum value for the player to pick this round can 
	 *    end up with
	 * 2. state transition function
	 *    d[i][j] = max(left, right);
	 *    left  = values[i] + min(dp[i + 2][j], dp[i + 1][j - 1]);
	 *    right = values[j] + min(dp[i + 1][j - 1], dp[i][j - 2]);
	 *    explaination:
	 *    for the player who has to pick this round, 2 options:
	 *    a. pick the left most element, then the opponent has to handle values[i + 1, j], 
	 *       the opponent will have the pick the larger one, for this player, he will be 
	 *       left with the smaller one. 
	 *    b. pick the right most element...
	 * 3. Initialization
	 *    dp[i][i] = values[i];
	 *    dp[i][i + 1] = values[i] + values[i + 1];
	 * 4. Answer:
	 *    dp[0][len - 1];
	 * Note:
	 *    this is a bottom up method
	 * */
	public boolean firstWillWin1(int[] values) {
		long sum = 0;
	    for (int v : values) {
	        sum += v;
	    }
	    
	    int len = values.length;
	    long[][] dp = new long[len][len];
	    
	    for (int i = 0; i < len; i++) {
	        dp[i][i] = (long) values[i];
	    }
	    
	    for (int i = 0; i < len - 1; i ++) {
	        dp[i][i + 1] = (long)(values[i] + values[i + 1]);
	    }
	    
	    for (int l = 2; l < len; l++) {
	        for (int i = 0; i + l < len; i++) {
	            long left = values[i] + Math.min(dp[i + 2][i + l], 
	                                            dp[i + 1][i + l - 1]);
	            long right = values[i + l] +
	                        Math.min(dp[i + 1][i + l - 1], 
	                                 dp[i][i + l - 2]);
	            dp[i][i + l] = Math.max(left, right);
	        }
	    }
	    
	    return 2 * dp[0][len - 1] > sum;
	}
	
	/**
	 * Solution 2 (Bottom up DP)
	 * 1. state definition:
	 * 	  dp[i][j] means if given subarray i...j for a player, what is the
	 *    maximum he may end up with.
	 * 2. state transition:
	 *    dp[i][j] = max(sum(i,j) - dp[i - 1][j], sum(i,j) - dp[i][j - 1]);
	 *    explaination, for the player this round, 2 options
	 *    1) choose left most one, left dp[i - 1][j] to opponent, then this player's
	 *       final result is sum(i,j) - dp[i - 1][j];
	 *    2) choose right most one,.....
	 * 3. Initialization:
	 *    dp[i][i] = values[i];
	 ***/
	public boolean firstWillWin2(int[] values) {
        // write your code here
        int len = values.length;
        
        long[] sum = new long[len + 1];
        
        for (int i = 1; i <= len; i++) {
            sum[i] = sum[i - 1] + values[i - 1];
        }
        
        long[][] dp = new long[len][len];
        for (int i = 0; i < len; i++) {
            dp[i][i] = values[i]; 
        }
        
        for (int l = 1; l < len; l++) {
            for (int i = 0; i + l < len; i++) {
                long partSum = sum[i + l + 1] - sum[i];
                dp[i][i + l] = Math.max(partSum - dp[i + 1][i + l],
                                        partSum - dp[i][i + l - 1]);
            }
        }
        
        return 2 * dp[0][len - 1] > sum[len];
    }
	
	/**
	 * Solution 3 (TopDown meomized search)
	 * 1. state definition:
	 * 	  dp[i][j] means if given subarray i...j for a player, what is the
	 *    maximum he may end up with.
	 ***/
	public boolean firstWillWin3(int[] values) {
        // write your code here
        int len = values.length;
        
        long[] sum = new long[len + 1];
        
        for (int i = 1; i <= len; i++) {
            sum[i] = sum[i - 1] + values[i - 1];
        }
        
        Long[][] dp = new Long[len][len];
        for (int i = 0; i < len; i++) {
            dp[i][i] = (long)values[i]; 
        }
        
        return 2 * search(0, len - 1, values, dp, sum) > sum[len];
    }
    
    private long search(int i, int j, int[] values, Long[][] dp, long[] sum) {
        if (dp[i][j] != null) {
            return dp[i][j];
        }
        long partSum = sum[j + 1] - sum[i];
        
        long candiate1 = partSum - search(i + 1, j, values, dp, sum);
        long candiate2 = partSum - search(i, j - 1, values, dp, sum);
        dp[i][j] = Math.max(candiate1, candiate2);
        return dp[i][j];
    }
    
    
    /**
	 * Solution 4 (TopDown meomized search)
	 * 1. state definition:
	 * 	  same as solution 1.
	 ***/
    public boolean firstWillWin4(int[] values) {
        // write your code here
        int len = values.length;
        
        long[] sum = new long[len + 1];
        
        for (int i = 1; i <= len; i++) {
            sum[i] = sum[i - 1] + values[i - 1];
        }
        
        Long[][] dp = new Long[len][len];
        for (int i = 0; i < len; i++) {
            dp[i][i] = (long) values[i];
            if (i < len - 1) {
                dp[i][i + 1] = (long) Math.max(values[i], values[i + 1]);
            }
        }
        
        for (int i = 0; i + 2 < len; i++) {
            
            dp[i][i + 2] = Math.max((long) values[i] + Math.min(dp[i + 1][i + 1], 
                                                dp[i + 2][i + 2]),
                           (long) values[i + 2] + Math.min(dp[i + 1][i + 1], dp[i][i]));
        }
        
        return 2 * search1(0, len - 1, values, dp, sum) > sum[len];
    }
    
    private long search1(int i, int j, int[] values, Long[][] dp, long[] sum) {
        if (dp[i][j] != null) {
            return dp[i][j];
        }
        
        long candiate1 = values[i] + 
                         Math.min(search1(i + 2, j, values, dp, sum),
                                  search1(i + 1, j - 1, values, dp, sum)
                         );
        long candiate2 = values[j] + 
                         Math.min(search1(i + 1, j - 1, values, dp, sum),
                                  search1(i, j - 2, values, dp, sum)
                         );
        dp[i][j] = Math.max(candiate1, candiate2);
        return dp[i][j];
    }
}
