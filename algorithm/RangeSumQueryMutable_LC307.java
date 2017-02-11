/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Feb 11, 2017
 */
package algorithm;
/**
 * https://leetcode.com/problems/range-sum-query-mutable/
 * 
 * This is Fenwick Tree (Binary Index Tree Solution)
 * **/
public class RangeSumQueryMutable_LC307 {
	int[] fw, old;
    public RangeSumQueryMutable_LC307(int[] nums) {
        fw = new int[nums.length + 1];
        old = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            update(i, nums[i]);
        }
    }
    
    public void update(int i, int val) {
        int delta = val - old[i];
        old[i] = val;
        i++;
        while (i < fw.length) {
            fw[i] += delta;
            i = i + (i & -i);
        }
    }
    
    
    public int sumRange(int i, int j) {
        return rangeFrom0(j) - rangeFrom0(i - 1);
    }
    
    private int rangeFrom0(int index) {
        index++;
        int res = 0;
        while (index > 0) {
            res += fw[index];
            index = index - (index & -index);
        }
        return res;
    }
}
