/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Feb 22, 2017
 */
package algorithm.dp;

/**
 * http://www.lintcode.com/en/problem/best-time-to-buy-and-sell-stock-iv/#
 * **/
public class BesttimeToSellStock4_LC188 {
	
	/***
	 * solution 1.
	 * 1. state definition: 
	 *    dp[i][j] finish at most i transactions in the first j days
	 * 2. tansition function
	 *    dp[i][j] = max{ dp[i][j - 1], dp[i - 1][x] +  }
	 *                   
	 * 
	 * **/
	public int maxProfit(int k, int[] prices) {
        // write your code here
        if (prices == null || prices.length == 0 
        || k <= 0 ) {
            return 0;
        }
        
        if (k > prices.length) return maxBuy(prices);
        
        int len = prices.length;
        int[][] dp = new int[k + 1][len + 1];
        
        for (int i = 1; i <= k; i++) {
            dp[i][0] = Integer.MIN_VALUE;
        }
        
        for (int i = 1; i <= k; i++) {
            for (int j = 2; j <= len; j++) {
                int maxSales = prices[j - 1];
                int maxProfit = Integer.MIN_VALUE;
                dp[i][j] = dp[i - 1][j];
                for (int l = j; l >= 1; l--) {
                    int lastProfit = maxSales - prices[l - 1];
                    maxProfit = Math.max(maxProfit, lastProfit);
                    maxSales = Math.max(maxSales, prices[l - 1]);
                    dp[i][j] = Math.max(dp[i][j], dp[i - 1][l] + maxProfit);
                }
            }
        }
        return dp[k][len];
    }
    
    private int maxBuy(int[] prices) {
        int res = 0, low = prices[0];
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] >= low) {
                res += prices[i] - low;
            }
            low = prices[i];
        }
        return res;
    }
}
