/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Mar 7, 2017
 */
package algorithm;
/**
 * http://www.lintcode.com/en/problem/continuous-subarray-sum-ii/
 * */
public class ContinuousSubarraySum2_Lintcode403 {
	/**
	 *  This solution is not very good. 
	 *  the maxsum array can only be one of two candidates
	 *  a. a continuous subarray in the middle of the array
	 *  b. a discontinuous subarray with part in the end of the array
	 *     and part in the beginning of the array
	 *  so. we use two for loops
	 *  1. 1st for loop finds the max value in case a
	 *  2. 2nd for loop finds the max value in case b
	 *     in the case b, watch out on test case when all
	 *     the items in an array is negative.
	 * **/
	public ArrayList<Integer> continuousSubarraySumII(int[] A) {
        // Write your code here
        ArrayList<Integer> res = new ArrayList<Integer>();
        int start = 0, end = 0;
        int local = 0, global = Integer.MIN_VALUE;
        int total = 0;
        //int total = 0;
        res.add(0);
        res.add(0);
        for (int i = 0; i < A.length; i++) {
            total += A[i];
            if (local < 0) {
                local = A[i];
                start = end = i;
            } else {
                local += A[i];
                end = i;
            }
            if (local > global) {
                global = local;
                res.set(0, start);
                res.set(1, end);
            }
        }
        
        start = 0;
        local = 0;
        end = 0;
        
        //System.out.println(global);
        
        for (int i = 0; i < A.length; i++) {
            if (local > 0) {
                local = A[i];
                start = end = i;
            } else {
                local += A[i];
                end = i;
            }
            
            if (start == 0 && end == A.length - 1) continue;
            
            if (total - local > global) {
                global = total - local;
                res.set(0, end + 1);
                res.set(1, start - 1);
            }
        }
        
        //System.out.println(global);
        
        return res;
    }
}
