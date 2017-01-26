/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 25, 2017
 */
package algorithm;

/**
 * https://leetcode.com/problems/maximal-rectangle/
 * 
 * This is a follow up of LC 84.
 * we scan the char[][] array from 1st to last line
 * at each line, we update the heights array,
 * then compute the maximal rectangle in histgoram (LC84)
 * and update the global maximum.
 * 
 * **/
import java.util.Stack;

public class MaximalRectangle_LC85 {

	public static void main(String[] args) {

	}

	public int maximalRectangle(char[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return 0;
        }
        
        int m = matrix.length, n = matrix[0].length;
        int res = 0;
        int[] heights = new int[n];
        //System.out.println(maximalRectangle(new int[] {3, 1, 3, 2, 2}));
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == '0') {
                    heights[j] = 0;
                } else {
                    heights[j] += 1;
                }
            }
            res = Math.max(res, maximalRectangle(heights));
        }
        return res;
    }
    
    private int maximalRectangle(int[] heights) {
        int res = 0, len = heights.length;
        Stack<Integer> stack = new Stack();
        for (int i = 0; i <= len; i++) {
            int h = i < len ? heights[i] : 0;
            while (!stack.isEmpty() && heights[stack.peek()] > h) {
                int height = heights[stack.pop()];
                int width = stack.isEmpty() ? i : (i - stack.peek() - 1); 
                res = Math.max(res, height * width);
            }
            stack.push(i);
        }
        return res;
    }
}
