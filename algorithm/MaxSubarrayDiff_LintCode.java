package algorithm;
/**
 * See problem statement at 
 * http://www.lintcode.com/en/problem/maximum-subarray-difference/
 * **/
public class MaxSubarrayDiff_LintCode {

	public static void main(String[] args) {
		
	}
	
	public int maxDiffSubArrays(int[] nums) {
        if (nums == null || nums.length <= 1) {
            return 0;
        }
        
        int len = nums.length;
        int[] leftMin = new int[len];
        int[] leftMax = new int[len];
        
        /**
            Compute leftMin array, which leftMin[i] means min subarray array
            lies in between index 0 and i;
            similar for leftMax;
        **/
        int prefixSum = 0;
        int minSum = 0, maxSum = 0;
        int maxVal = Integer.MIN_VALUE, minVal = Integer.MAX_VALUE;
        for (int i = 0; i < len; i++) {
            prefixSum += nums[i];
            maxVal = Math.max(maxVal, prefixSum - minSum);
            minVal = Math.min(minVal, prefixSum - maxSum);
            leftMin[i] = minVal;
            leftMax[i] = maxVal;
            maxSum = Math.max(maxSum, prefixSum);
            minSum = Math.min(minSum, prefixSum);
        }
        
        
        /**
            Compute rightMin arrary, which rightMin[i] means min subarray array
            lies in between i and len -1;
            simiarl for rightMax array
        **/
        int[] rightMin = new int[len];
        int[] rightMax = new int[len];
        minSum = 0;
        maxSum = 0;
        maxVal = Integer.MIN_VALUE;
        minVal = Integer.MAX_VALUE;
        int suffixSum = 0;
        for (int i = len - 1; i >= 0; i--) {
            suffixSum += nums[i];
            maxVal = Math.max(maxVal, suffixSum - minSum);
            minVal = Math.min(minVal, suffixSum - maxSum);
            rightMin[i] = minVal;
            rightMax[i] = maxVal;
            maxSum = Math.max(maxSum, suffixSum);
            minSum = Math.min(minSum, suffixSum);
        }
        
        int res = 0;
        for (int i = 0; i < len - 1; i++) {
            res = Math.max(res, Math.abs(leftMin[i] - rightMax[i + 1]));
            res = Math.max(res, Math.abs(leftMax[i] - rightMin[i + 1]));
        }
        
        return res;
    }
}
