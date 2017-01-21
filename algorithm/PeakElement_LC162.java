/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 20, 2017
 */
package algorithm;
/**
 * https://leetcode.com/problems/find-peak-element/
 * 
 * **/
public class PeakElement_LC162 {

	public static void main(String[] args) {

	}
	
	public int findPeakElement(int[] nums) {
        
        int len = nums.length;
        int lo = 0, hi = len - 1;
        
        while (lo + 1 < hi) {
            int mid = (lo + hi) >>> 1;
            if (nums[mid] > nums[Math.max(0, mid - 1)] && nums[mid] > nums[Math.min(len - 1, mid + 1)]) {
                return mid;
            } else if (nums[mid] < nums[Math.max(0, mid - 1)]) {
                hi = mid;
            } else if (nums[mid] < nums[Math.min(len - 1, mid + 1)]) {
                lo = mid;
            }
        }
        
        if (nums[lo] > nums[hi]) {
            return lo;
        }
        return hi;
    }
}
