package algorithm;

import java.util.ArrayList;

/**
	See http://www.lintcode.com/en/problem/maximum-subarray-ii/
 ***/
public class MaxSubarray2LintCode {

	public static void main(String[] args) {

	}
	
	public int maxTwoSubArrays(ArrayList<Integer> nums) {
        if (nums == null || nums.size() == 0) {
            return 0;
        }
        
        int len = nums.size();
        int[] prefixSum = new int[len];
        int[] suffixSum = new int[len];
        
        //create prefix sum array
        for (int i = 0; i < len; i++) {
            if (i == 0) {
                prefixSum[i] = nums.get(i);
            } else {
                prefixSum[i] = prefixSum[i - 1] + nums.get(i); 
            }
        }
        
        //create suffix sum array
        for (int i = len - 1; i >= 0; i--) {
            if (i == len - 1) {
                suffixSum[i] = nums.get(i);
            } else {
                suffixSum[i] = nums.get(i) + suffixSum[i + 1];
            }
        }
        
        //maxBefore[i]  means max subarray value that lies in 0 and i
        int[] maxBefore = new int[len];
        //maxAfter[i]  means max subarray value that lies in i and lengths
        int[] maxAfter = new int[len];
        
        int minSum = 0;
        int runningMax = Integer.MIN_VALUE;
        //popluate maxBefore
        for (int i = 0; i < len; i++) {
            runningMax = Math.max(runningMax, prefixSum[i] - minSum);
            minSum = Math.min(minSum, prefixSum[i]);
            maxBefore[i] = runningMax; 
        }
        
        minSum = 0;
        //populate maxAfter
        runningMax = Integer.MIN_VALUE;
        for (int i = len - 1; i >= 0; i--) {
            runningMax = Math.max(runningMax, suffixSum[i] - minSum);
            minSum = Math.min(minSum, suffixSum[i]);
            maxAfter[i] = runningMax;
        }
        
        int res = Integer.MIN_VALUE;
        //find maxvalue of two subarrays
        for (int i = 0; i < len - 1; i++) {
            res = Math.max(maxBefore[i] + maxAfter[i + 1], res);
        }
        
        return res;
    }
}
