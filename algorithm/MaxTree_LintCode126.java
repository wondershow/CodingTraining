/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Feb 13, 2017
 */
package algorithm;
/**
 * http://www.lintcode.com/en/problem/max-tree/#
 * A typical usage of Stack. 
 * look for 1st large element on both sides of one element.
 * */
public class MaxTree_LintCode126 {
	public TreeNode maxTree(int[] A) {
        // write your code here
        if (A == null || A.length == 0) return null;
        Stack<TreeNode> stack = new Stack();
        for (int i = 0; i <= A.length; i++) {
            TreeNode cur;
            if (i == A.length) {
                cur = new TreeNode(Integer.MAX_VALUE);
            } else {
                cur = new TreeNode(A[i]);
            }
            
            while (!stack.isEmpty() && stack.peek().val < cur.val) {
                TreeNode kid = stack.pop();
                if (stack.isEmpty()) {
                    cur.left = kid;
                } else {
                    if (cur.val > stack.peek().val) {
                        stack.peek().right = kid;
                    } else {
                        cur.left = kid;
                    }
                }
            }
            
            stack.push(cur);
        }
        
        return stack.peek().left;
    }
}
