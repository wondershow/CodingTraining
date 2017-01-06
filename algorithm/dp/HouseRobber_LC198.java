/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 6, 2017
 */
package algorithm.dp;

/**
 * See problem statement at 
 * https://leetcode.com/problems/house-robber/
 * 
 * This is a pretty easy DP problem, but still 
 * we need to pay some attention here.
 * 
 * 1. State
 * 	  dp[i] means for subarray nums[0...i-1], what the maximum rob 
 *    value will be.
 * 2. State transition function:
 *    dp[i] = Max(dp[i - 2] + nums[i - 1], dp[i - 1]);	  
 * 3. initialization
 * 	  dp[0] = 0, dp[1] = nums[0];
 * 4. answer:
 *    dp[n]
 *  
 * one thing to think about is 
 *    for dp[i]'s solution it may or may not contains the nums[i - 1],
 *    then why we can make sure that dp[i + 1] can be either dp[i]
 *     or dp[i - 1] + nums[i];
 *    is it possible that the optimal solution of dp[i + 1] be dp[i]
 *  	  + nums[i] ? 
 *     
 *    dp[i] : either dp[i - 1] or dp[i - 2] + nums[i - 1] 
 *    so dp[i]'s solution may or may not contain nums[i - 1].
 *    Now, when we try to find out optimal solution for dp[i + 1]
 *    is it possible that dp[i + 1] = dp[i](when dp[i] does not 
 *    include nums[i - 1]) + nums[i]? Can we miss something here?
 *    
 *    The answer is no, the seems-to-missing state has been considered
 *    in our state-transition function.
 *    lets consider how to compute dp[i + 1].
 *    There are 2 situations of dp[i]:
 *  		    1) nums[i - 1] included in dp[i], lets say its dp[i]_a
 *          2) nums[i - 1] not included in dp[i], lets say its dp[i]_b
 *    notice that dp[i]_b = dp[i - 2];
 *    
 *    so for dp[i + 1], the dp[i] solution does not include nums[i - 1]
 *    is duplicated with the case that dp[i - 1] case, so we do not need
 *    to consider that case.
 ****/
public class HouseRobber_LC198 {

	public static void main(String[] args) {

	}
	
	
	public int rob(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        
        int len = nums.length;
        
        //only 2 states a useful, buffer them
        int[] dp = new int[2];
        dp[0] = 0;
        dp[1] = nums[0];
        for (int i = 2; i <= len; i++) {
            dp[i % 2] = Math.max(dp[(i - 2) % 2] + nums[i - 1], dp[(i - 1) % 2]);
        }
        
        return dp[len % 2];
    }
}
