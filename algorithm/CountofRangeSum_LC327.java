/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 22, 2017
 */
package algorithm;
/**
 * https://leetcode.com/problems/count-of-range-sum/
 * 
 * 
 * Mistakes made:
 * 1. the prefix sum's length is len + 1
 *    so the mergesort parts should be mergesort(0, len)
 *    instead of mergesort(0, len - 1);!
 * ***/
public class CountofRangeSum_LC327 {

	public static void main(String[] args) {

	}
	
	
	
	public int countRangeSum(int[] nums, int lower, int upper) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        int len = nums.length;
        long[] pfx = new long[len + 1];
        long[] aux = new long[len + 1];
        for (int i = 1; i <= len; i++) {
            pfx[i] = pfx[i - 1] + nums[i - 1];
        }
        
        //Note that here should be 0 to len (NOTE len - 1!!!!)
        int res = countAndSort(pfx, aux, lower, upper, 0, len);
        return res;
    }
    
    private int countAndSort(long[] pfx, long[] aux, int down, int up, int lo, int hi) {
        
        if (lo >= hi) {
            return 0;
        }
        
        int mid = (lo + hi) >>> 1;
        int res = countAndSort(pfx, aux, down, up, lo, mid)
                  + countAndSort(pfx, aux, down, up, mid + 1, hi);
        
        for (int i = lo; i <= hi; i++) {
            aux[i] = pfx[i];
        }
        
        int i = lo, j = mid + 1, k = lo;
        int downPtr = mid + 1, upPtr = mid + 1;
        while (i <= mid || j <= hi) {
            if (i > mid) {
                pfx[k++] = aux[j++];
            } else if (j > hi || aux[i] <= aux[j]) {
                while (downPtr <= hi && aux[downPtr] - aux[i] < down) downPtr++; 
                while (upPtr <= hi && aux[upPtr] - aux[i] <= up) upPtr++;
                res += upPtr - downPtr;
                pfx[k++] = aux[i++];
            } else {
                pfx[k++] = aux[j++];
            }
        }
        
        return res;
    }
}
