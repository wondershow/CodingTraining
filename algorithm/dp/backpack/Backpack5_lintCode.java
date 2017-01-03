/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 2, 2017
 */
package algorithm.dp.backpack;

/**
 * see problem statement at:
 * http://www.lintcode.com/en/problem/backpack-v/
 * **/
public class Backpack5_lintCode {

	public static void main(String[] args) {

	}
	
	public int backPackV(int[] nums, int target) {
        // Write your code here
        if (nums == null || nums.length == 0 || target <= 0) {
            return 0;
        }
        
        int len = nums.length;
        int[][] dp = new int[len + 1][target + 1];
        
        for (int i = 0; i <= len ; i++) {
            dp[i][0] = 1;
        }
        
        for (int i = 1; i <= len; i++) {
            for (int j = 1; j <= target; j++) {
                dp[i][j] = dp[i - 1][j];
                if (nums[i - 1] <= j) {
                    dp[i][j] += dp[i - 1][j - nums[i - 1]];
                }
            }
        }
        
        return dp[len][target];
    }
}
