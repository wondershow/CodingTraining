/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 10, 2017
 */
package algorithm;
/**
 * See problem statement at
 * https://leetcode.com/problems/range-sum-query-2d-mutable/
 * This version is a 2d Segmentation Tree. The computation is 
 * still overloaded. There should be a better version.
 * 
 * */
public class RangeSum2D_LC308 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	class SegTree {
        SegTree leftup, rightup, leftdown, rightdown;
        int sum, x1, x2, y1, y2;
        SegTree(int x1, int y1, int x2, int y2, int sum) {
            this.x1 = x1;
            this.x2 = x2;
            this.y1 = y1;
            this.y2 = y2;
            this.sum = sum;
            leftup = rightup = leftdown = rightdown = null;
        }
    }

    SegTree segRoot;
    public RangeSum2D_LC308(int[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            segRoot = null;
        } else {
            segRoot = build(matrix, 0, 0, matrix.length - 1, matrix[0].length - 1);
            //System.out.println(segRoot.sum);
        }
    }

    public void update(int row, int col, int val) {
        update(row, col, val, segRoot);
    }

    public int sumRegion(int row1, int col1, int row2, int col2) {
        return rangeQuery(row1, col1, row2, col2, segRoot);
    }
    
    private SegTree build(int[][] matrix, int x1, int y1, int x2, int y2) {
        if (x1 < 0 || x2 >= matrix.length || y1 < 0 || y2 > matrix[0].length || x1 > x2 || y1 > y2) {
            return null;
        }
        
        if (x1 == x2 && y1 == y2) {
            return new SegTree(x1, y1, x2, y2, matrix[x1][y1]);
        }
        
        SegTree root = new SegTree(x1, y1, x2, y2, 0);
        
        int midx = (x1 + x2) >>> 1;
        int midy = (y1 + y2) >>> 1;
        
        root.leftup = build(matrix, x1, y1, midx, midy);
        root.leftdown = build(matrix, midx + 1, y1, x2, midy);
        root.rightup = build(matrix, x1, midy + 1, midx, y2);
        root.rightdown = build(matrix, midx + 1, midy + 1, x2, y2);
        if (root.leftup != null) root.sum += root.leftup.sum;
        if (root.leftdown != null) root.sum += root.leftdown.sum;
        if (root.rightup != null) root.sum += root.rightup.sum;
        if (root.rightdown != null) root.sum += root.rightdown.sum;
        return root;
    }
    
    private void update(int x, int y, int val, SegTree root) {
        if (root == null || root.x1 > x || root.x2 < x || root.y1 > y || root.y2 < y) {
            return;
        }
        if (root.x1 == root.x2 && root.y1 == root.y2) {
            root.sum = val;
            return;
        }
        update(x, y, val, root.leftup);
        update(x, y, val, root.leftdown);
        update(x, y, val, root.rightup);
        update(x, y, val, root.rightdown);
        root.sum = 0;
        if (root.leftup != null) root.sum += root.leftup.sum;
        if (root.leftdown != null) root.sum += root.leftdown.sum;
        if (root.rightup != null) root.sum += root.rightup.sum;
        if (root.rightdown != null) root.sum += root.rightdown.sum;
    }
    
    private int rangeQuery(int x1, int y1, int x2, int y2, SegTree root) {
        if (root == null || root.x1 > x2 || root.x2 < x1 || root.y1 > y2 || root.y2 < y1) {
            return 0;
        }
        if (x1 <= root.x1 && x2 >= root.x2 && y1 <= root.y1 && y2 >= root.y2) {
            return root.sum;
        }
        return rangeQuery(x1, y1, x2, y2, root.leftup) 
             + rangeQuery(x1, y1, x2, y2, root.leftdown)
             + rangeQuery(x1, y1, x2, y2, root.rightup)
             + rangeQuery(x1, y1, x2, y2, root.rightdown);
    }

}
