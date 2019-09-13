
public class LintCode141 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	
	/**
	 * Made a few mistakes:
	 * 1. have not considered when x is 0 or 1
	 * 2. lo started from 2 not 1
	 * 3. square may get overflow
	 * 4. hi * hi may get overflow
	 * **/
	public class Solution {
	    /**
	     * @param x: An integer
	     * @return: The sqrt of x
	     */
	    public int sqrt(int x) {
	        // write your code here
	        if (x == 0 || x == 1) {
	            return x;
	        }
	        
	        int lo = 1;
	        int hi = x;
	        while (lo + 1 < hi) {
	            int mid = lo + (hi - lo) / 2;
	            long square = (long)mid * (long)mid;
	            if (square > (long) x) {
	                hi = mid;
	            } else {
	                lo = mid;
	            }
	        }
	        
	        if ((long)hi * (long)hi <= (long)x) {
	            return hi;
	        } 
	        return lo;
	    }
	}

}
