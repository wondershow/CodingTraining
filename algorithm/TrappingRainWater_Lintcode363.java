/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Feb 14, 2017
 */
package algorithm;
/**
 * http://www.lintcode.com/en/problem/trapping-rain-water/
 * */
public class TrappingRainWater_Lintcode363 {
	public int trapRainWater(int[] heights) {
        // write your code here
        if (heights == null || heights.length <= 2) {
            return 0;
        }
        
        int lmax = heights[0], rmax = heights[heights.length - 1];
        int i = 0, j = heights.length - 1, res = 0;
        while (i <= j) {
            if (lmax < rmax) {
                res += Math.max(0, lmax - heights[i]);
                lmax = Math.max(heights[i++], lmax);
            } else {
                res += Math.max(0, rmax - heights[j]);
                rmax = Math.max(heights[j--], rmax);
            }
        }
        
        return res;
    }
}
