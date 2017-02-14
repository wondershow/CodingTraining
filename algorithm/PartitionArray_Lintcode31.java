/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Feb 14, 2017
 */
package algorithm;
/**
 * http://www.lintcode.com/en/problem/partition-array/
 * 
 * **/
public class PartitionArray_Lintcode31 {
	public int partitionArray(int[] nums, int k) {
	    //write your code here
	    if (nums == null || nums.length == 0) return 0;
	    
	    int i = 0, j = nums.length - 1;
	    
	    while (i < j) {
	        while (i < j && nums[i] < k) i++;
	        while (i < j && nums[j] >= k) j--;
	        swap(nums, i, j);
	    }
	    if (nums[i] < k) i++;
	    return i;
    }
    
    private void swap(int[] chars, int i, int j) {
        int ch = chars[i];
        chars[i] = chars[j];
        chars[j] = ch;
    }
}
