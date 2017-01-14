/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 14, 2017
 */
package algorithm;

import java.util.Arrays;

/**
 * See problem statement at:
 * https://leetcode.com/problems/wiggle-sort-ii/
 * two solutions offered
 * **/
public class WiggleSort2_LC324 {

	public static void main(String[] args) {

	}
	
	/***
	 * Sort and rearrange
	 * time n long n
	 * space n;
	 * **/
	public void wiggleSort1(int[] nums) {
        if (nums == null || nums.length <= 1) {
            return;
        }
        
        Arrays.sort(nums);
        int mid = (nums.length - 1) / 2;
        
        int i = mid, j = nums.length - 1;
        
        int[] res = new int[nums.length];
        int k = 0;
        
        while (k < nums.length) {
            res[k++] = nums[i--];
            if (k < nums.length) {
                res[k++] = nums[j--];
            }
        }
        
        for (int t = 0; t < nums.length; t++) {
            nums[t] = res[t];
        }
    }
}
