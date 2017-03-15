/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Mar 14, 2017
 */
package algorithm;
/**
 * https://leetcode.com/problems/next-greater-element-ii/#/description
 * */
public class NextGreaterElement_LC503 {
	public int[] nextGreaterElements(int[] nums) {
        if (nums == null || nums.length == 0) return nums;
        List<Integer> doubled = new ArrayList();
        for (int i = 0; i < nums.length; i++) {
            doubled.add(nums[i]);
        }
        
        for (int i = 0; i < nums.length; i++) {
            doubled.add(nums[i]);
        }
        
        int len = nums.length;
        
        Stack<Integer> stack = new Stack();
        int[] res = new int[len];
        for (int i = 0; i < doubled.size(); i++) {
            if (i < len) {
                while (stack.size() > 0 && doubled.get(i) > nums[stack.peek()]) {
                    int index = stack.pop();
                    res[index] = nums[i];
                }
                stack.push(i);
            } else {
                while (stack.size() > 0 && doubled.get(i) > nums[stack.peek()]) {
                    int index = stack.pop();
                    res[index] = doubled.get(i);
                }
            }
        }
        
        while (stack.size() > 0) {
            res[stack.pop()] = -1;
        }
        
        return res;
    }
}
