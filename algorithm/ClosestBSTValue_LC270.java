/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 19, 2017
 */
package algorithm;
/**
 * https://leetcode.com/problems/closest-binary-search-tree-value/
 * */
public class ClosestBSTValue_LC270 {

	public static void main(String[] args) {

	}

	public int closestValue(TreeNode root, double target) {
        int res = root.val;
        double min = Math.abs((double)root.val - target);
        
        while (root != null) {
            if (Math.abs((double)root.val - target) < min) {
                min = Math.abs((double)root.val - target);
                res = root.val;
            }
            if (target == (double) root.val) {
                return root.val;
            } else if (target > (double) root.val) {
                root = root.right;
            } else {
                root = root.left;
            }
        }
        
        return res;
    }
}
