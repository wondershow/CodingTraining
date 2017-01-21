/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 21, 2017
 */
package algorithm;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/**
 * https://leetcode.com/problems/combination-sum-iv/
 * When given this problem, first notice that
 * combination problem may take up to 2^n time complexity.
 * 
 * The follow up problem:
 * What constrains do we need to add to allow negative numbers
 * 1. at most size k subsets
 * 2. the numbers in the subset has to be strictly increasing
 * 3. 
 * 
 * **/
public class Combination4_LC377 {

	public static void main(String[] args) {

	}
	
	public int combinationSum4(int[] nums, int target) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        
        Map<Integer, Integer> cache = new HashMap();
        return helper(nums, target, cache);
    }
    
    private int helper(int[] nums, int sum, Map<Integer, Integer> cache) {
        if (sum <= 0) {
            if (sum == 0)
                return 1;
            else
                return 0;
        }
        if (cache.containsKey(sum)) {
            return cache.get(sum);
        }
        
        int res = 0;
        for (int i = 0; i < nums.length; i++) {
            res += helper(nums, sum - nums[i], cache);
        }
        
        cache.put(sum, res);
        return cache.get(sum);
    }
    
    /**
     * DP solution2
     * */
    public int combinationSum4_1(int[] nums, int target) {
        if (target == 0) {
            return 1;
        }
        int[] dp = new int[target + 1];
        Arrays.fill(dp, -1);
        dp[0] = 1;
        return helper1(nums, target, dp);
    }
    
    private int helper1(int[] nums, int sum, int[] dp) {
        if (dp[sum] != -1) {
            return dp[sum];
        }
        
        int res = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] <= sum) {
                res += helper1(nums, sum - nums[i], dp);
            }
        }
        dp[sum] = res;
        return dp[sum];
    }
}
