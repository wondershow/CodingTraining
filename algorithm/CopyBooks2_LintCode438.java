/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Feb 19, 2017
 */
package algorithm;

public class CopyBooks2_LintCode438 {
	
	/**
	 * DP solution
	 * 1. state definition:
	 *    dp[i][j] means, if use first i ppl to copy j books what will be the best
	 *    finish time
	 * 2. state transition
	 *    dp[i][j] = min(dp[i - 1][j - k], k * time[j]);
	 * 3. initialization
	 *    dp[1][i] = i * time[0];
	 * 4. answer 
	 *    dp[len][i]
	 * 
	 * optimization:
	 *    rolling array
	 *    
	 * 
	 * **/
	public int copyBooksII2(int n, int[] times) {
        // write your code here
        
        int len = times.length;
        int[][] dp = new int[2][n + 1];
        
        for (int i = 0; i <= n; i++) {
            dp[1 % 2][i] = i * times[0];
        }
        
        for (int i = 2; i <= len; i++) {
            for (int j = 1; j <= n; j++) {
                dp[i % 2][j] = Integer.MAX_VALUE;
                int t = times[i - 1];
                int tmp = Math.max(dp[(i - 1) % 2][j - k], k * t);
                dp[i  % 2][j] = Math.min(dp[i % 2][j], tmp);
                if (k * t > dp[(i - 1) % 2][j - k]) break;
                }
            }
        }
        
        return dp[len % 2][n];
    }
	
	
	
	
	
	/**
	 * binary search based solution.
	 * **/
	public int copyBooksII(int n, int[] times) {
        int lo = 1, hi = Integer.MAX_VALUE;
        
        while (lo + 1 < hi) {
            int mid = (lo + hi) >>> 1;
            if (canCopy(n, times, mid)) {
                hi = mid;
            } else {
                lo = mid;
            }
        }
        //System.out.println(canCopy(n, times, 4));
        //System.out.println(hi);
        if (canCopy(n, times, lo)) return lo;
        return hi;
    }
    
    private boolean canCopy(int n, int[] times, int minute) {
        int books = 0;
        for (int i = 0; i < times.length; i++) {
            if (times[i] <= minute) {
                books += minute / times[i];
            }
            if (books >= n) return true;
        }
        //System.out.println(books);
        return books >= n;
    }
}
