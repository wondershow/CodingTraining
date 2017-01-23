/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 22, 2017
 */
package algorithm.dp;
/**
 * https://leetcode.com/problems/predict-the-winner/
 * exactly the same as Coins in A line 3
 * 
 * **/
public class PridictWinner_LC486 {

	public static void main(String[] args) {

	}
	public boolean PredictTheWinner(int[] nums) {
        if (nums.length == 1) {
            return true;
        }
        
        int len = nums.length, sum = 0;
        int[][] dp = new int[len + 1][len + 1];
        for (int i = 1; i <= len; i++) {
            sum += nums[i - 1];
            dp[i][i] = nums[i - 1];
            if (i < len) {
                dp[i][i + 1] = Math.max(nums[i - 1], nums[i]);
            }
        }
        
        for (int l = 3; l <= len; l++) {
            for (int i = 1; i + l - 1 <= len; i++) {
                int j = i + l - 1;
                //System.out.println(i);
                int left = nums[i - 1]
                            + Math.min(dp[i + 2][j], dp[i + 1][j - 1]);
                int right = nums[j - 1] 
                            + Math.min(dp[i + 1][j - 1], dp[i][j - 2]);
                dp[i][j] = Math.max(left, right);
            }
        }
        
        //System.out.println(dp[1][len]);
        return 2 * dp[1][len] >= sum;
    }
}
