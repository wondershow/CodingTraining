/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Dec 31, 2016
 */
package algorithm;
public class RangeSum2DMutable_LC308 {
	
	/***
	 * Use a 2D Segment Tree to solve the problem.
	 * since a 1D sgement tree has two children, 
	 * a 2D segment tree has 4 kids.
	 * coding almost the same
	 * **/
	class TreeNode2D {
        int sum, rLo, rHi, cLo, cHi;
        TreeNode2D ne, nw, se, sw;
        TreeNode2D(int rl, int rt, int cl, int ct, int sum) {
            this.rLo = rl;
            this.rHi = rt;
            this.cLo = cl;
            this.cHi = ct;
            this.sum = sum;
            ne = nw = se = sw = null;
        }
    }
	
    TreeNode2D root = null;
    public RangeSum2DMutable_LC308(int[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return;
        }
        root = build2DSegTree(matrix, 0, matrix.length - 1, 0, matrix[0].length - 1);
    }

    public void update(int row, int col, int val) {
        updateSegTree(root, row, col, val);
    }

    public int sumRegion(int row1, int col1, int row2, int col2) {
        return sumSegTree(root, row1, row2, col1, col2);
    }
    
    private int sumSegTree(TreeNode2D root, int r_lo, int r_hi, int c_lo, int c_hi) {
        if (root == null || r_lo > root.rHi || r_hi < root.rLo || c_lo > root.cHi || c_hi < root.cLo) {
            return 0;
        }
        
        if (r_lo <= root.rLo && r_hi >= root.rHi && c_lo <= root.cLo && c_hi >= root.cHi) {
            return root.sum;
        }
        
        return  sumSegTree(root.ne, r_lo, r_hi, c_lo, c_hi)
              + sumSegTree(root.se, r_lo, r_hi, c_lo, c_hi)
              + sumSegTree(root.nw, r_lo, r_hi, c_lo, c_hi)
              + sumSegTree(root.sw, r_lo, r_hi, c_lo, c_hi);
    }
    
    private void updateSegTree(TreeNode2D root, int row, int col, int val) {
        if (root == null || row < root.rLo || row > root.rHi || col < root.cLo || col > root.cHi) {
            return;
        }
        if (root.rLo == root.rHi && root.cLo == root.cHi && row == root.rLo && col == root.cLo) {
            root.sum = val;
            return;
        }
        
        updateSegTree(root.nw, row, col, val);
        updateSegTree(root.ne, row, col, val);
        updateSegTree(root.sw, row, col, val);
        updateSegTree(root.se, row, col, val);
        
        root.sum = 0;
        if (root.nw != null) root.sum += root.nw.sum;
        if (root.ne != null) root.sum += root.ne.sum;
        if (root.sw != null) root.sum += root.sw.sum;
        if (root.se != null) root.sum += root.se.sum;
    }
    
    
    
    private TreeNode2D build2DSegTree(int[][] matrix, int r_lo, int r_hi, int c_lo, int c_hi) {
        if (r_lo < 0 || r_hi >= matrix.length || c_lo < 0 
            || c_hi >= matrix[0].length || r_lo > r_hi || c_lo > c_hi) {
            return null;
        }
        
        if (r_lo == r_hi && c_lo == c_hi) {
            return new TreeNode2D(r_lo, r_hi, c_lo, c_hi, matrix[r_lo][c_lo]);
        }
        
        TreeNode2D root = new TreeNode2D(r_lo, r_hi, c_lo, c_hi, 0);
        int r_mid = (r_lo + r_hi) >>> 1;
        int c_mid = (c_lo + c_hi) >>> 1;
        if (r_lo == r_hi) {
            root.sw = build2DSegTree(matrix, r_lo, r_hi, c_lo, c_mid);
            root.se = build2DSegTree(matrix, r_lo, r_hi, c_mid + 1, c_hi);
        } else if (c_lo == c_hi) {
            root.ne = build2DSegTree(matrix, r_lo, r_mid, c_lo, c_hi);
            root.se = build2DSegTree(matrix, r_mid + 1, r_hi, c_lo, c_hi);
        } else {
            root.nw = build2DSegTree(matrix, r_lo, r_mid, c_lo, c_mid);
            root.sw = build2DSegTree(matrix, r_mid + 1, r_hi, c_lo, c_mid);
            root.ne = build2DSegTree(matrix, r_lo, r_mid, c_mid + 1, c_hi);
            root.se = build2DSegTree(matrix, r_mid + 1, r_hi, c_mid + 1, c_hi);
        }
        
        if (root.nw != null) root.sum += root.nw.sum;
        if (root.sw != null) root.sum += root.sw.sum;
        if (root.ne != null) root.sum += root.ne.sum;
        if (root.se != null) root.sum += root.se.sum;
        return root;
    }
	
    public static void main(String[] args) {

	}
}
/**
 * This is a 2D Fenwick Tree solution. coding much easier  
 * performance should be better
 * ***/
class Solution2{
	int[][] treeBIT;
    int[][] orig;
    
    int m, n;
    public Solution2(int[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0)
            return;
        m = matrix.length;
        n = matrix[0].length;
        orig = new int[m][n];
        treeBIT = new int[m + 1][n + 1];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                update(i, j, matrix[i][j]);
            }
        }
    }
    
    
    public void update(int row, int col, int val) {
        int delta = val - orig[row][col];
        orig[row][col] = val;
        row++;
        col++;
        for (int x = row; x <= m; x += x & -x) {
            for (int y = col; y <= n; y+= y & -y) {
                treeBIT[x][y] += delta;
            }
        }
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        return sumFrom00(row2, col2) - sumFrom00(row2, col1 - 1) - sumFrom00(row1 - 1, col2) + sumFrom00(row1 - 1, col1 - 1);
    }
    
    public int sumFrom00(int row, int col) {
        if (row < 0 || col < 0) return 0;
        int res = 0;
        row++;
        col++;
        for (int x = row; x > 0; x -= x & -x) {
            for (int y = col; y > 0; y -= y & -y) {
                res += treeBIT[x][y];
            }
        }
        return res;
    }
}



