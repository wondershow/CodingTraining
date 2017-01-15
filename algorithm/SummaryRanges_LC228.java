/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 14, 2017
 */
package algorithm;


/**
 * See problem statement at
 * https://leetcode.com/problems/summary-ranges/
 * 
 * Note that there is one leftover interval to be 
 * handled when the loop is over.
 * 
 * */
import java.util.ArrayList;
import java.util.List;

public class SummaryRanges_LC228 {

	public static void main(String[] args) {
	}
	
	public List<String> summaryRanges(int[] nums) {
        List<String> res = new ArrayList<String>();
        if (nums == null || nums.length == 0) {
            return res;
        }
        
        int low = nums[0], limit = nums[0];
        
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == limit + 1) {
                limit++;
            } else {
                if (limit == low) {
                    res.add(limit + "");
                } else {
                    res.add(low + "->" + limit);
                }
                low = nums[i];
                limit = nums[i];
            }
        }
        
        if (limit == low) {
            res.add(limit + "");
        } else {
            res.add(low + "->" + limit);
        }
        
        return res;
    }

}
