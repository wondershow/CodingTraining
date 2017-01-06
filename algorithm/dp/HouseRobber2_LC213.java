/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 6, 2017
 */
package algorithm.dp;

/**
 * See problem statement at 
 * https://leetcode.com/problems/house-robber-ii/
 * When you are given a circle
 * 
 * **/
public class HouseRobber2_LC213 {

	public int rob(int[] nums) {
        return mySol1(nums);
    }
    
    private int mySol1(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        if (nums.length == 1) {
            return nums[0];
        }
        
        int len = nums.length;
        int[] dp = new int[2];
        
        int res = 0;
        
        for (int offset = 0; offset < len; offset++) {
            dp[0] = 0;
            dp[1] = nums[offset];
            for (int i = 2; i < len; i++) {
                int curIndex = (i + offset - 1) % len;
                dp[i % 2] = Math.max(dp[(i - 1) % 2], dp[(i - 2) % 2] + nums[curIndex]);
            }
            
            res = Math.max(res, dp[(len - 1) % 2]);
        }
        
        return res;
    }
    
    private int mySol2(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        if (nums.length == 1) {
            return nums[0];
        }
        
        int len = nums.length;
        int[] dp = new int[2];
        dp[0] = 0;
        dp[1] = 0;
        for (int i = 2; i <= len; i++) {
            dp[i % 2] = Math.max(dp[(i - 2) % 2] + nums[i - 1], dp[(i - 1) % 2]);
        }
        
        int answer1 = dp[len % 2];
        
        dp[0] = 0;
        dp[1] = nums[0];
        
        for (int i = 2; i <= len; i++) {
            dp[i % 2] = Math.max(dp[(i - 2) % 2] + nums[i - 1], dp[(i - 1) % 2]);
        }
        
        return Math.max(dp[(len - 1) % 2], answer1);
    }
}
