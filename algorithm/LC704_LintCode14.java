
public class LC704_LintCode14 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	class Solution {
	    public int search(int[] nums, int target) {
	        if (nums == null || nums.length == 0) {
	            return -1;
	        }
	        int lo = 0, hi = nums.length - 1;
	        while (lo + 1 < hi) {
	            int mid = lo + (hi - lo) / 2;
	            if (nums[mid] > target) {
	                hi = mid;
	            } else {
	                lo = mid;
	            }
	        }
	        
	        if (nums[hi] == target) {
	            return hi;
	        }
	        if (nums[lo] == target) {
	            return lo;
	        }
	        return -1;
	    }
	}
}
