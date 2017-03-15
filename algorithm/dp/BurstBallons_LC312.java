/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Mar 14, 2017
 */
package algorithm.dp;
/**
 * https://leetcode.com/problems/burst-balloons/#/description
 * **/
public class BurstBallons_LC312 {
	
	/***
	 * 
	 * Bottom UP DP
	 * 
	 * f[i][j] means max value we can find by bursting balloons from index i to j.
	 * int order to find out the max value of f[i][j], we iterate variable k from i to j
	 * k is the last balloon to burst in range i to j. 
	 * 
	 * **/
	public int maxCoins(int[] nums) {
        // Write your code here
        if (nums == null || nums.length == 0) return 0;
        
        int len = nums.length;
        
        int[][] f = new int[len][len];
        
        //f[i][j] means the max val if k is the last to burst
        //in range i...j
        for (int i = 0; i < len; i++) {
            int left = i == 0 ? 1 : nums[i - 1];
            int right = i == len - 1 ? 1 : nums[i + 1];
            f[i][i] = left * right * nums[i];
        }
        
        for (int l = 2; l <= len; l++) {
            for (int i = 0; i + l - 1 < len; i++) {
                int start = i, end = i + l - 1;
                int left = start == 0 ? 1 : nums[start - 1];
                int right = end == len - 1 ? 1 : nums[end + 1];
                for (int k = start; k <= end; k++) {
                    int leftScore = k == start ? 0 : f[start][k - 1];
                    int rightScore = k == end ? 0 : f[k + 1][end];
                    f[start][end] = Math.max(f[start][end], leftScore + rightScore + left * right * nums[k]);
                }
            }
        }
        
        return f[0][len - 1];
    }
}
