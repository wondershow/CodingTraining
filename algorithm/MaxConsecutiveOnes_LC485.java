/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 21, 2017
 */
package algorithm;
/***
 * https://leetcode.com/problems/max-consecutive-ones/
 * 
 * 
 * **/
public class MaxConsecutiveOnes_LC485 {

	public static void main(String[] args) {

	}
	
	public int findMaxConsecutiveOnes(int[] nums) {
        int res = 0;
        
        int i = 0, j = 0;
        while (i < nums.length) {
            while (j < nums.length) {
                if (nums[j] == 0) break;
                j++;
            }
            if (nums[i] == 1) {
                res = Math.max(res, j - i);
            }
            i = j;
            while (i < nums.length && nums[i] == 0) i++;
            j = i;
        }
        
        return res;
    }
}
