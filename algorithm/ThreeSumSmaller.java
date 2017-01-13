/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 13, 2017
 */
package algorithm;

import java.util.Arrays;

/**
 * See problem statement at 
 * https://leetcode.com/problems/3sum-smaller/
 * typical two pointers problem
 * 
 * **/
public class ThreeSumSmaller {

	public static void main(String[] args) {

	}
	
	public int threeSumSmaller(int[] nums, int target) {
        if (nums == null || nums.length <= 2) {
            return 0;
        }
        
        Arrays.sort(nums);
        
        int res = 0;
        for (int i = 0; i < nums.length - 2; i++) {
            int k = i + 1, j = nums.length - 1;
            while (k < j) {
                if (nums[k] + nums[j]  + nums[i]>= target) {
                    j--;
                } else {
                    res += j - k;
                    k++;
                }
            }
        }
        return res;
    }
}
