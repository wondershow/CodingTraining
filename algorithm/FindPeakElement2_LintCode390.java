/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Feb 28, 2017
 */
package algorithm;

import java.util.List;

/***
 * http://www.lintcode.com/en/problem/find-peak-element-ii/
 * **/
public class FindPeakElement2_LintCode390 {
	
	/**
	 * Solution 1.
	 * o(m logn)
	 * */
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
        
        res.add(lo);
        res.add(peakIndexInLine(A, lo));
        
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
    
    
    /**
     * Solution 2
     * o(m + n)
     * **/
    public List<Integer> findPeakII_2(int[][] A) {
        // write your code here
        List<Integer> res = new ArrayList<Integer>();
        if (A == null || A.length == 0 || A[0].length == 0) return res;
        int m = A.length, n = A[0].length - 1;
        int rowFrom = 0, rowTo = A.length - 1, colFrom = 0, colTo = A[0].length - 1; 
        int midRow = 0, midCol = 0, peakRow = 0, peakCol = 0;
        
        while (rowFrom < rowTo && colFrom < colTo) {
            midRow = (rowFrom + rowTo) >>> 1;
            peakCol = peakIndexInLine(A, midRow, colFrom, colTo);
            
            if (isPeak(A, midRow, peakCol)) {
                res.add(midRow);
                res.add(peakCol);
                return res;
            } else if (A[midRow][peakCol] < A[midRow - 1][peakCol]) {
                rowTo = midRow;
            } else {
                rowFrom = midRow;
            }
            
            midCol = (colFrom + colTo) >>> 1;
            peakRow = peakIndexCol(A, midCol, rowFrom, rowTo);
            if (isPeak(A, peakRow, midCol)) {
                res.add(peakRow);
                res.add(midCol);
                return res;
            } else if (A[peakRow][midCol] < A[peakRow][midCol - 1]) {
                colTo = midCol;
            } else {
                colFrom = midCol;
            }
        }
        
        if (rowFrom == rowFrom) {
            res.add(rowFrom);
            res.add(peakCol);
        } else {
            res.add(peakRow);
            res.add(colFrom);
        }
        
        return res;
    }
    
    private int peakIndexInLine(int[][] A, int row, int lo, int hi) {
        int index = 0;
        int max = Integer.MIN_VALUE;
        for (int i = lo; i <= hi; i++) {
            if (A[row][i] > max) {
                max = A[row][i];
                index = i;
            }
        }
        return index;
    }
    
    private int peakIndexCol(int[][] A, int col, int lo, int hi) {
        int index = 0;
        int max = Integer.MIN_VALUE;
        for (int i = lo; i <= hi; i++) {
            if (A[i][col] > max) {
                max = A[i][col];
                index = i;
            }
        }
        return index;
    }
    
    private boolean isPeak(int[][] A, int row, int col) {
        if (A[row][col] < A[row - 1][col]) return false;
        if (A[row][col] < A[row + 1][col]) return false;
        if (A[row][col] < A[row][col - 1]) return false;
        if (A[row][col] < A[row][col + 1]) return false;
        return true;
    }
}
