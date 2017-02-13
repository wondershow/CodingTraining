/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Feb 13, 2017
 */
package algorithm;
/**
 * http://www.lintcode.com/en/problem/convert-expression-to-polish-notation/# 
 * build a min tree first and then do a preorder traversal
 * **/
public class Expression2PolishNotation_LintCode369 {
	/**
     * @param expression: A string array
     * @return: The Polish notation of this expression
     */
    class TreeNode {
        String op;
        int val;
        TreeNode left, right;
        TreeNode(String s, int v) {
            op = s;
            val = v;
            left = right = null;
        }
    } 
     
     
    public ArrayList<String> convertToPN(String[] expression) {
        // write your code here
        ArrayList<String> res = new ArrayList<String>();
        List<TreeNode> list = new ArrayList();
        
        int base = 0;
        for (String str : expression) {
            TreeNode t = null;
            if (str.equals("(")) {
                base += 10;
            } else if (str.equals(")")) {
                base -= 10;
            } else if (str.equals("+") || str.equals("-")) {
                t = new TreeNode(str, base + 1);
            } else if (str.equals("*") || str.equals("/")) {
                t = new TreeNode(str, base + 2);
            } else {
                t = new TreeNode(str, Integer.MAX_VALUE);
            }
            if (t != null) list.add(t);
        }
        
        TreeNode root = buildMinTree(list);
        //System.out.println(list.size());
        preorder(root, res);
        
        return res;
    }
    
    private void preorder(TreeNode root, ArrayList<String> res) {
        if (root == null) return;
        res.add(root.op);
        preorder(root.left, res);
        preorder(root.right, res);
    }
    
    private TreeNode buildMinTree(List<TreeNode> list) {
        if (list == null || list.size() == 0) {
            return null;
        }
        
        Stack<TreeNode> stack = new Stack();
        
        for (int i = 0; i <= list.size(); i++) {
            TreeNode cur;
            if (i == list.size()) cur = new TreeNode("", 0);
            else cur = list.get(i);
            
            while (!stack.isEmpty() && stack.peek().val >= cur.val) {
                TreeNode kid = stack.pop();
                if (stack.isEmpty()) {
                    cur.left = kid;
                } else {
                    TreeNode left = stack.peek();
                    if (left.val < cur.val) {
                        cur.left = kid;
                    } else {
                        left.right = kid;
                    }
                }
            }
            
            stack.push(cur);
        }
        
       // System.out.println(stack.peek().left.op);
        return stack.peek().left;
    }
}
