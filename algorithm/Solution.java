/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 10, 2017
 */
package algorithm;

import java.util.ArrayList;
import java.util.List;

public class Solution {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//System.out.println(largestRound(33));
		
		int k = 2;
		int[] prices = new int[] {4,4,6,1,1,4,2,5};
		int res = Solution.maxProfit(k, prices);
		System.out.println(res);
	}
	
	public static int maxProfit(int k, int[] prices) {
        // write your code here
        if (prices == null || prices.length == 0 
        || k <= 0 || k > prices.length) {
            return 0;
        }
        
        int len = prices.length;
        int[][] dp = new int[k + 1][len + 1];
        
        for (int i = 1; i <= k; i++) {
            dp[i][0] = Integer.MIN_VALUE;
        }
        
        /**
            dp[i][j] means max profit to do at most i 
            transactions in first j days.
        **/
        for (int i = 1; i <= k; i++) {
            for (int j = 2; j <= len; j++) {
                int maxSales = prices[j - 1];
                int maxProfit = Integer.MIN_VALUE;
                dp[i][j] = dp[i - 1][j];
                for (int l = j; l >= 1; l--) {
                    int lastProfit = maxSales - prices[l - 1];
                    maxProfit = Math.max(maxProfit, lastProfit);
                    maxSales = Math.max(maxSales, prices[l - 1]);
                    //minBuy = Math.min(minBuy, prices[l - 1]);
                    dp[i][j] = Math.max(dp[i][j], dp[i - 1][l] + maxProfit);
                    System.out.println(dp[i - 1][l] + maxProfit + " : max profit" );
                    System.out.println("maxProfit = " + maxProfit + ", maxSales = " + maxSales);
                }
            }
        }
        
        for (int i = 0; i <= k; i++) {
        		for (int j = 0; j <= len; j++) {
        			System.out.print(dp[i][j] + " ");
        		}
        		System.out.println();
        }
        
        return dp[k][len];
    }
}
