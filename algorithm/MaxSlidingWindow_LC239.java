/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 17, 2017
 */
package algorithm;
/**
 * https://leetcode.com/problems/sliding-window-maximum/
 * Mistakes made:
 * 1. The first place to compute max should be k - 1,
 *    I made it at k.
 * */
import java.util.Deque;
import java.util.LinkedList;

public class MaxSlidingWindow_LC239 {

	public static void main(String[] args) {

	}
	
	class Wrapper {
        int index, val;
        Wrapper(int i, int v) {
            index = i;
            val = v;
        }
    }
    
    public int[] maxSlidingWindow(int[] nums, int k) {
        if (nums == null || nums.length == 0 || k == 0) {
            return new int[0];
        }
        
        int[] res = new int[nums.length - k + 1];
        
        Deque<Wrapper> que = new LinkedList();
        for (int i = 0; i < nums.length; i++) {
            if (que.size() > 0 && que.peekFirst().index + k == i) {
                que.pollFirst();
            }
            while (que.size() > 0 && que.peekLast().val <= nums[i]) {
                que.pollLast();
            }
            que.offerLast(new Wrapper(i, nums[i]));
            if (i >= k - 1) {
                res[i - k + 1] = que.peekFirst().val;
            }
        }
        
        return res;
    }

}
