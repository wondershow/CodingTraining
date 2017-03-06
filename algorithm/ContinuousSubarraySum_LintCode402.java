/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Mar 6, 2017
 */
package algorithm;

import java.util.ArrayList;

/**
 * http://www.lintcode.com/en/problem/continuous-subarray-sum/
 * 
 * */
public class ContinuousSubarraySum_LintCode402 {
	public ArrayList<Integer> continuousSubarraySum(int[] A) {
        // Write your code here
        ArrayList<Integer> res = new ArrayList<Integer>();
        int start = 0, end = 0;
        int local = 0, global = Integer.MIN_VALUE;
        //int total = 0;
        res.add(0);
        res.add(0);
        for (int i = 0; i < A.length; i++) {
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
        
        //int local = 0;
        return res;
    }
}
