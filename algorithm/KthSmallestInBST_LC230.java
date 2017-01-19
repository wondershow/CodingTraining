/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 19, 2017
 */
package algorithm;
/**
 * https://leetcode.com/problems/kth-smallest-element-in-a-bst/
 * 
 * **/
public class KthSmallestInBST_LC230 {

	public static void main(String[] args) {

	}
	
	public int kthSmallest(TreeNode root, int k) {
        int leftSize = size(root.left);
        if (leftSize + 1 == k) return root.val;
        else if (leftSize + 1  > k) return kthSmallest(root.left, k);
        else return kthSmallest(root.right, k - leftSize - 1);
    }
    
    private int size(TreeNode root) {
        if (root == null) {
            return 0;
        }
        return 1 + size(root.left) + size(root.right);
    }
}
