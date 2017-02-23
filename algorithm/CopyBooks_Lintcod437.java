/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Feb 19, 2017
 */
package algorithm;
/**
 * http://www.lintcode.com/en/problem/copy-books/#
 * 
 * **/
public class CopyBooks_Lintcod437 {
	
	/***
	 * Solution 1, DP.
	 * 1. state definition.
	 * 		f[i][j] means what is the time if you use j pepole to 
	 *       copy first 1 books
	 * 2. state tansistion
	 *     f[i][j] = min( max(f[r][j - 1], sum (r + 1, j))
	 *             
	 * 3. init:
	 *     f[i][0] = 0; ()
	 * 4. answer
	 *     f[n][k];
	 * time complexity o(n^2 k)
	 * ***/
	public int copyBooks(int[] pages, int k) {
        // write your code here
        int len = pages.length;
        
        int[][] dp = new int[len + 1][k + 1];
        
        for (int i = 1; i <= len; i++) {
            dp[i][0] = 0;
            dp[i][1] = dp[i - 1][1] + pages[i - 1];
        }
        
        for (int j = 2; j <= k; j++) {
            for (int l = 1; l <= len; l++) {
                int min = Integer.MAX_VALUE;
                int runnningsum = 0;
                for (int i = l; i >= 1; i--) {
                    runnningsum += pages[i - 1];
                    min = Math.min(min, Math.max(runnningsum, dp[i - 1][j - 1]));
                }
                dp[l][j] = min;
            }
        }
        
        return dp[len][k];
    }
	
	/**
	 * Binary search the minimum minutes to copy a book with k ppl
	 * 
	 * canCopy runs in o(n) time, so the whole 
	 * algorithm runs in o(c n) time, where c is up to 31. 
	 * **/
	public int copyBooks2(int[] pages, int k) {
        // write your code here
        if (pages == null || pages.length == 0) return 0;
        int lo = 1, hi = Integer.MAX_VALUE;
        
        while (lo + 1 < hi) {
            int mid = (lo + hi) >>> 1;
            if (canCopy(pages, k, mid)) {
                hi = mid;
            } else {
                lo = mid;
            }
        }
        if (canCopy(pages, k, lo)) return lo; 
        return hi;
    }
    
    private boolean canCopy(int[] pages, int k, int minutes) {
        
        int runnningsum = 0, ppl = 1;
        for (int i = 0; i < pages.length; i++) {
            if (runnningsum + pages[i] > minutes) {
                ppl++;
                runnningsum = pages[i];
            } else {
                runnningsum += pages[i];
            }
            if (ppl > k || minutes < pages[i]) return false;
        }
        
        return ppl <= k;
    } 
}
