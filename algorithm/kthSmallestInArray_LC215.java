/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Feb 12, 2017
 */
package algorithm;
/**
 * https://leetcode.com/problems/kth-largest-element-in-an-array/
 * */
public class kthSmallestInArray_LC215 {
	
	/**
	 * Solution one, partition based
	 * */
	public int findKthLargest(int[] nums, int k) {
		if (nums == null || nums.length == 0 || k > nums.length) {
			return -1;
		}
	      
		return helper(nums, k, 0, nums.length - 1);
	}
	  
    private int helper(int[] nums, int rank, int lo, int hi) {
        int pivot = nums[lo];
        int i = lo, j = lo, k = hi;
        while (j <= k) {
          if (nums[j] == pivot) j++;
          else if (nums[j] > pivot) {
            swap(nums, j, k--);
          } else {
            swap(nums, i++, j++);
          }        
        }
        
        if (rank >= hi - k + 1 && rank <= hi - i + 1) {
          return pivot;
        } else if (rank < hi - k + 1) {
          return helper(nums, rank, k + 1, hi);
        } else {
          return helper(nums, rank - (hi - i + 1), lo, i - 1);
        }
    }
  
    private void swap(int[] nums, int i, int j) {
      int tmp = nums[i];
      nums[i] = nums[j];
      nums[j] = tmp;
    }
	
    
    /**
     * Solution 2, binary search based.
     * **/
    public int kthSmallest(int k, int[] nums) {
        // write your code here
        int lo = Integer.MAX_VALUE, hi = Integer.MIN_VALUE;
        for (int num : nums) {
            lo = Math.min(lo, num);    
            hi = Math.max(hi, num);
        }
        
        while (lo + 1 < hi) {
            int mid = (lo + hi) >>> 1;
            int a = rankOfVal(nums, mid);
            int b = rankOfVal(nums, mid + 1);
            if (a <= k && k < b) return mid;
            if (a > k) {
                hi = mid;
            } else {
                lo = mid;
            }
        }
        
        int a = rankOfVal(nums, lo);
        int b = rankOfVal(nums, hi);
        if (a <= k && k < b) return lo;
        return hi;
    }
    
    private int rankOfVal(int[] nums, int val) {
        int res = 1;
        
        for (int num : nums) {
            if (num < val) {
                res++;
            }
        }
        
        return res;
    }
}
