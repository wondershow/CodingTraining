/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 2, 2017
 */
package algorithm.dp.backpack;
/**
 * See problem statement at:
 * http://www.lintcode.com/en/problem/backpack-iv/
 * 
 * The variation of state transition function.
 * Key is you need to manually populate dp[][] matrix
 * so that you can develop correct transition function.
 * **/
public class Backpack4_LintCode {

	public static void main(String[] args) {

	}

	public int backPackIV(int[] nums, int target) {
        if (nums == null || nums.length == 0 || target <= 0) {
            return 0;
        }
        
        int len = nums.length;
        
        int[][] dp = new int[len + 1][target + 1];
        
        for (int i = 0; i <= len; i++) {
            dp[i][0] = 1;
        }
        
        for (int i = 1; i <= len; i++) {
            for (int j = 1; j <= target; j++) {
                dp[i][j] = dp[i - 1][j];
                if (j >= nums[i - 1]) {
                    dp[i][j] += dp[i][j -  nums[i - 1]];
                }
            }
        }
        
        return dp[len][target];
    }
}
