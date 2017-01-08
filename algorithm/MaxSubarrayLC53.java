package algorithm;
/**
 * See problem statement at 
 * https://leetcode.com/problems/maximum-subarray/
 * **/
public class MaxSubarrayLC53 {

	public static void main(String[] args) {
		
	}
	
	public int maxSubArray(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        
        /**
        create a prefix sum
        **/
        int len = nums.length;
        int[] sum = new int[len + 1];
        for (int i = 0; i < len; i++) {
            sum[i + 1] += sum[i] + nums[i];
        }
        
        int minSum = 0;
        int res = Integer.MIN_VALUE;
        /**
         * scan prefix sum from left to right,
         * update the minimum value at each 
         * iteration
        **/
        for (int i = 1; i <= len; i++) {
            res = Math.max(res, sum[i] - minSum);
            minSum = Math.min(minSum, sum[i]);
        }
        
        return res;
    }
	
}
