/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Feb 28, 2017
 */
package algorithm;
/***
 * http://www.lintcode.com/en/problem/find-peak-element-ii/
 * **/
public class FindPeakElement2_LintCode390 {
	public List<Integer> findPeakII(int[][] A) {
        // write your code here
        List<Integer> res = new ArrayList<Integer>();
        if (A == null || A.length == 0 || A[0].length == 0) return res;
        int m = A.length, n = A[0].length - 1;
        int lo = 0, hi = A.length - 1;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            int peak = peakIndexInLine(A, mid);
            if (A[mid][peak] > A[mid - 1][peak] && A[mid][peak] > A[mid + 1][peak]) {
                res.add(mid);
                res.add(peak);
                return res;
            } else if (A[mid][peak] < A[mid - 1][peak]) {
                hi = mid;
            } else {
                lo = mid;
            }
        }
        
        res.add(lo, peakIndexInLine(A, lo));
        
        return res;
    }
    
    private int peakIndexInLine(int[][] A, int row) {
        int index = 0;
        
        int max = Integer.MIN_VALUE;
        
        for (int i = 0; i < A[0].length; i++) {
            if (A[row][i] > max) {
                max = A[row][i];
                index = i;
            }
        }
        
        return index;
    }
}
