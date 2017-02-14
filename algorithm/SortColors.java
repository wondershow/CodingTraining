/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Feb 14, 2017
 */
package algorithm;
/**
 * http://www.lintcode.com/en/problem/sort-colors/
 * 
 * */
public class SortColors {

	public void sortColors(int[] nums) {
        // write your code here
        if (nums == null || nums.length <= 1) return;
        
        int i = 0, j = 0, k = nums.length - 1;
        
        while (j <= k) {
            if (nums[j] == 0) swap(nums, i++, j++);
            else if (nums[j] == 1) j++;
            else swap(nums, j, k--);
        }
    }
    
    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }

}
