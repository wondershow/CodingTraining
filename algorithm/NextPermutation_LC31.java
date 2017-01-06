/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 3, 2017
 */
package algorithm;

/**
 * See problem statement at
 * https://leetcode.com/problems/next-permutation/
 * 
 * Tricky question.
 *  + means position i larger than position i + 1;
 *  - means position i smaller than position i + 1;
 *  ? means unknown
 *                     k
 *  [? ? ? ? ? ? ..... + - - - - ]
 *  scan from end to k, find 1st        
 *         
 * **/
public class NextPermutation_LC31 {

	public static void main(String[] args) {

	}
	
	public void nextPermutation(int[] nums) {
        if (nums == null) return;
        
        int len = nums.length;
        int i = len - 2;
        for (; i >= 0; i--) {
            if (nums[i] < nums[i + 1]) {
                int j = len - 1;
                for (; j > i; j--) {
                    if (nums[j] > nums[i]) {
                        swap(nums, i, j);
                        reverse(nums, i + 1, len - 1);
                        return;
                    }
                }
            }
        }
        
        reverse(nums, 0, len - 1);
    }
    
    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
    
    private void reverse(int[] nums, int i, int j) {
        while (i < j) {
            swap(nums, i++, j--);
        }
    }
}
