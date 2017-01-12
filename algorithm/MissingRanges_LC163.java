/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 11, 2017
 */
package algorithm;
/**
 * See problem statement at 
 * https://leetcode.com/problems/missing-ranges/
 * 
 * one thing to be aware overflow!
 * **/
import java.util.ArrayList;
import java.util.List;

public class MissingRanges_LC163 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	public List<String> findMissingRanges(int[] nums, int lower, int upper) {
        List<String> res = new ArrayList<String>();
        
        long missingFrom = (long)lower;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > missingFrom) {
                if (missingFrom + 1 < nums[i]) {
                    res.add(missingFrom + "->" + (nums[i] - 1));
                } else {
                    res.add(missingFrom + "");
                }
            }
            missingFrom = (long)nums[i] + 1;
        }
        if (upper > missingFrom) {
            res.add(missingFrom + "->" + upper);
        } else if (upper == missingFrom) {
            res.add(missingFrom + "");
        }
        
        return res;
    }
}
