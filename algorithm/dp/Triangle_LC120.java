/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 1, 2017
 */
package algorithm.dp;

import java.util.List;
/**
 * Three methods to solve this problem
 * 1. Divide and Conquer + Memoization
 * 2. TopDown DP
 * 3. BottomUp DP
 * ***/
public class Triangle_LC120 {

	public static void main(String[] args) {

	}
	
	public int minimumTotal(List<List<Integer>> triangle) {
        return bottomUpDP(triangle);
    }
    
    /**
        Divide and Conquer + Memoization Search
    **/
    private int dc(List<List<Integer>> triangle) {
        if (triangle == null || triangle.size() == 0) {
            return 0;
        }
        int n = triangle.size();
        int[][] hash = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                hash[i][j] = Integer.MAX_VALUE;
            }
        }
        return dcHelper(triangle, 0, 0, hash);
    }
    
    private int dcHelper(List<List<Integer>> triangle, int x, int y, int[][] hash) {
        if (x == triangle.size() - 1) {
            return triangle.get(x).get(y);
        }
        if (hash[x][y] != Integer.MAX_VALUE) {
            return hash[x][y];
        }
        
        int left = dcHelper(triangle, x + 1, y, hash);
        int right = dcHelper(triangle, x + 1, y + 1, hash);
        hash[x][y] = Math.min(left, right) + triangle.get(x).get(y);
        return hash[x][y];
    }
    
    /**
    DP solution, from solution point search until atomic state. 
    ***/
    private int topDownDP(List<List<Integer>> triangle) {
        if (triangle == null || triangle.size() == 0) {
            return 0;
        }
        
        int n = triangle.size();
        
        //dp[i][j] means the shortest sum from (0,0) to (i, j);
        int[][] dp = new int[n][n];
        dp[0][0] = triangle.get(0).get(0);
        
        for (int i = 1; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                if (j == 0) {
                    dp[i][j] = dp[i - 1][j] + triangle.get(i).get(j);
                } else if (j == i) {
                    dp[i][j] = dp[i - 1][j - 1] + triangle.get(i).get(j);
                } else {
                    dp[i][j] = Math.min(dp[i - 1][j], dp[i - 1][j - 1])  
                               + triangle.get(i).get(j);
                }
            }
        }
        
        int res = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            res = Math.min(res, dp[n - 1][i]);
        }
        
        return res;
    }
    
    /**
        from atomic state builds up until the problem solution
    */
    private int bottomUpDP(List<List<Integer>> triangle) {
        if (triangle == null || triangle.size() == 0) {
            return 0;
        }
        
        int n = triangle.size();
        
        int[][] dp = new int[n][n];
        
        for (int i = 0; i < n; i++) {
            dp[n - 1][i] = triangle.get(n - 1).get(i);
        }
        
        for (int i = n - 2; i >= 0; i--) {
            for (int j = 0; j <= i; j++) {
                dp[i][j] = Math.min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle.get(i).get(j);
            }
        }
        
        return dp[0][0];
    }
}
