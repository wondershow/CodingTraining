/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Feb 19, 2017
 */
package algorithm;

public class CopyBooks2_LintCode438 {
	
	
	
	/**
	 * binary search based solution.
	 * 
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
