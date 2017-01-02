/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 1, 2017
 */
package algorithm.dp;

import java.util.Arrays;

/**
 * Classical 1D DP.
 * */
public class LIS_LC300 {

	public static void main(String[] args) {

	}
	
	public int lengthOfLIS(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        
        int len = nums.length;
        int dp[] = new int[len];
        Arrays.fill(dp, 1);
        
        int res = 1;
        for (int i = 1; i < len; i++) {
            for (int j = i - 1; j >= 0; j--) {
                if (nums[i] > nums[j]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                    res = Math.max(res, dp[i]);
                }
            }
        }
        
        return res;
    }
}
