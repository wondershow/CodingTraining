/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 13, 2017
 */
package algorithm;
/**
 * See problem statement at
 * https://leetcode.com/problems/perfect-squares/
 * */
public class PerfcetSquares_LC279 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	/**
	 * DP solution
	 * dp[j] = min{ dp[j - 1*1] + 1 , dp[j - 2*2] + 1
	 *             ...... dp[j - k*k] + 1}
	 * **/
	public int numSquares(int n) {
        int[] dp = new int[n + 1];
        dp[0] = 0;
        for (int i = 1; i <= n; i++) {
            int min = Integer.MAX_VALUE;
            int j = 1;
            while ( i - j * j >= 0) {
                min = Math.min(min, dp[i - j * j] + 1);
                j++;
            }
            dp[i] = min; 
        }
        return dp[n];        
    }
	
	
}
