/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 17, 2017
 */
package algorithm;
/**
 * https://leetcode.com/problems/trapping-rain-water/
 * 
 * 
 * **/
public class TrappingRainWater_LC42 {

	public static void main(String[] args) {

	}
	
	/***
	 * 2 pointers solution
	 * */
	public int trap1(int[] height) {
        if (height == null || height.length <= 2) {
            return 0;
        }
        
        int i = 0, j = height.length - 1;
        
        int left = height[i], right = height[j];
        int res = 0;
        while (i <= j) {
            if (left < right) {
                res += Math.max(0, left - height[i]);
                left = Math.max(left, height[i++]);
            } else {
                res += Math.max(0, right - height[j]);
                right = Math.max(right, height[j--]);
            }
        }
        
        return res;
    }
}
