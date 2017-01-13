/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 13, 2017
 */
package algorithm;

/**
 * See problem statement at:
 * https://leetcode.com/problems/wiggle-sort/
 * The key of this problem:
 * do a sort first, then adjust 
 * 1,2,3,4,5,6,7,8,
 * from position 1, every other index, replace i and its next, making
 * it 
 * 1,3,2,5,4,7,5,8 
 * o (n log n)
 * 
 * or we can scan from left to right, at any position if violates
 * the rule, swap it with its predecessor.
 * 
 * **/
public class WiggleSort_LC280 {

	public static void main(String[] args) {

	}
	
	public void wiggleSort(int[] nums) {
        for (int i = 1; i < nums.length; i++) {
            if (i % 2 == 1 && nums[i] < nums[i - 1] || i % 2 == 0 && nums[i] > nums[i - 1]) {
                swap(nums, i, i - 1);
            }
        }
    }
    
    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}
