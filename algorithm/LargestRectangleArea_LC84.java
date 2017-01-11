/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 11, 2017
 */
package algorithm;

import java.util.Stack;

public class LargestRectangleArea_LC84 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	/**
    See problem statement at 
    https://leetcode.com/problems/largest-rectangle-in-histogram/
    
    [2,1,5,6,2,3]
    
    for this problem, in order to find the maximal rectangle, at each position
    i, we need to know the 1st position that is smaller than i on both sides.
    then we are able to find the maximal rectangle at position i. 
    
    this is a hint of using stack, we can scan the array from left to right, 
    maintain a maxstack, whenever we encounter a new element at position i, 
    we can find its "left boundary" by comparing it with the stack elements,
    for the right boundary, we always consider the stack top element, since if
    stack top is smaller than the new incoming element, then its right boundary 
    is determined. 
    */
    public int largestRectangleArea(int[] height) {
        // write your code here
        int len = height.length, res = 0;
        Stack<Integer> s = new Stack<Integer>();
        for (int i = 0; i <= len; i++) {
            int h = i == len ? -1 : height[i];
            while (!s.isEmpty() && height[s.peek()] > h) {
                int high = height[s.pop()];
                int w = s.isEmpty() ? i : (i - s.peek() - 1);
                int area = w * high;
                res = Math.max(area, res);
            }
            s.push(i);
        }
        return res;
    }

}
