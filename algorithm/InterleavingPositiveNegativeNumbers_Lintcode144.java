/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Feb 14, 2017
 */
package algorithm;
/**
 * 
 * http://www.lintcode.com/en/problem/interleaving-positive-and-negative-numbers/
 * 
 * **/
public class InterleavingPositiveNegativeNumbers_Lintcode144 {
	public void rerange(int[] nums) {
        // write your code here
        if (nums == null || nums.length == 0) return;
        
        int posCnt = posCount(nums);
        int remainder = 0;
        if (nums.length % 2 != 0 && posCnt > (nums.length - 1) / 2) {
            remainder = 1;
        }
        
        int i = 0, j = 1;
        
        
        while(i < nums.length && j < nums.length) {
            while (i < nums.length && isMatch(nums, i, remainder)) i += 2;
            while (j < nums.length && isMatch(nums, j, remainder)) j += 2;
            if (i < nums.length && j < nums.length) {
                swap(nums, i, j);
            }
        }
    }
    
    private int posCount(int[] nums) {
        int res = 0;
        for (int num : nums) {
            if (num > 0) {
                res++;
            }
        }
        return res;
    }
    
    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
    
    private boolean isMatch(int[] nums, int i, int remainder) {
        if (nums[i] < 0 && i % 2 == (0 ^ remainder)) return true;
        if (nums[i] > 0 && i % 2 == (1 ^ remainder)) return true;
        return false;
    }
}
