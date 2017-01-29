/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 29, 2017
 */
package algorithm;

public class BinaryTree_LCS_LC298 {

	public static void main(String[] args) {

	}
	
	
	int res = 0;
    public int longestConsecutive(TreeNode root) {
        helper(root, null, 0);
        return res;
    }
    
    
    private void helper(TreeNode root, Integer parent, int length) {
        if (root == null) {
            return;
        }
        if (parent != null && root.val == parent + 1) {
            length++;
        } else {
            length = 1;
        }
        res = Math.max(res, length);
        helper(root.left, root.val, length);
        helper(root.right, root.val, length);
    }
}
