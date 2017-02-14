/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Feb 14, 2017
 */
package algorithm;
/**
 * http://www.lintcode.com/en/problem/the-smallest-difference/
 * 
 * **/
public class SmallestDifferences_Lintcode387 {
	public int smallestDifference(int[] A, int[] B) {
        // write your code here
        int i = 0, j = 0;
        int res = Integer.MAX_VALUE;
        Arrays.sort(A);
        Arrays.sort(B);
        while (i < A.length && j < B.length) {
            res = Math.min(res, Math.abs(A[i] - B[j]));
            if (A[i] < B[j]) i++;
            else j++;
        }
        
        return res;
    }
}
