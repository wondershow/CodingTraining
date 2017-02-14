/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Feb 14, 2017
 */
package algorithm;

public class PartitionByOddEven_LintCode373 {
	public void partitionArray(int[] nums) {
        // write your code here;
        if (nums == null || nums.length <= 1) {
            return;
        }
        int i = 0, j = nums.length - 1;
        while (i < j) {
            if (i < nums.length && nums[i] % 2 == 1) i++;
            if (j >= 0 && nums[j] % 2 == 0) j--;
            if (i < j) {
                swap(nums, i, j);
            }
        }
    }
    
	private void swap(int[] A, int i, int j) {
        int tmp = A[i];
        A[i] = A[j];
        A[j] = A[i];
    }
}
