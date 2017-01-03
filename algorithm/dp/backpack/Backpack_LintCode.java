/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 2, 2017
 */
package algorithm.dp.backpack;

public class Backpack_LintCode {

	public static void main(String[] args) {

	}
	
	/**
     * @param m: An integer m denotes the size of a backpack
     * @param A: Given n items with size A[i]
     * @return: The maximum size
     * 
     * See problem statement at
     * http://www.lintcode.com/en/problem/backpack/#
     * 
     * A very straightforward backpack problem. But still worthing
     * looking at.
     * 1. state :
     * 	   dp[i][j] means if first i items can be picked up to 
     *     sum up to a weight of j 
     * 2. state transition function:
     * 	   dp[i][j] = true if either the following conditions holds
     * 	   1). dp[i - 1][j] is true, means first i - 1 item can form 
     *         a j weight pickup. then lets just ditch i-th item
     *     2). dp[i - 1][j - A[i]] is true. means if first i - 1 items 
     *         can form a j - A[i] weight, then lets add i-ith item 
     *         with A[i] weight, we are able to form a j weight pick.
     *         Note that j - A[i] should be a valid array index
     * 3. Initialization states:
     * 	  It is easy to note that dp[0][0] is true, since first 0 item
     *    CAN form a zero weight sum. It might be ignored that 
     *    dp[i][0] are also true, since not matter how many items
     *    I am given, I am able to form a 0-weight pick by picking 
     *    nothing.   
     * 4. Answer:
     *    ....
     */
    public int backPack(int m, int[] A) {
        if (A == null || A.length == 0) {
            return 0;
        }
        
        boolean[][] dp = new boolean[A.length + 1][m + 1];
        
        for (int i = 0; i <= A.length; i++) {
            dp[i][0] = true;
        }
        
        for (int i = 1; i <= A.length; i++)
            for (int j = 1; j <= m; j++) {
                dp[i][j] = dp[i - 1][j];
                if (j - A[i - 1] >= 0 && dp[i - 1][j - A[i - 1]]) {
                    dp[i][j] = true;
                }
            }
        
        int i = m;
        for (; i >= 0; i--) {
            if (dp[A.length][i]) {
                break;
            }
        }
        
        return i;
    }
}
