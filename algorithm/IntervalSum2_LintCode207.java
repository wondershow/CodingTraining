/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Feb 12, 2017
 */
package algorithm;
/**
 * http://www.lintcode.com/en/problem/interval-sum-ii/
 * 
 * */
public class IntervalSum2_LintCode207 {
	int[] nums, fw;
	/**
	 * This is a Fenwick tree based solution, very easy to code
	 * but seems to be not very efficient
	 * **/
    public IntervalSum2_LintCode207(int[] A) {
        // write your code here
        if (A == null || A.length == 0) return;
        fw = new int[A.length + 1];
        nums = new int[A.length];
        for (int i = 0; i < A.length; i++) {
            update(i, A[i]);
        }
    }
    
    /**
     * @param start, end: Indices
     * @return: The sum from start to end
     */
    public long query(int start, int end) {
        // write your code here
        return query(end) - query(start - 1);
    }
    
    /**
     * @param index, value: modify A[index] to value.
     */
    public void modify(int index, int value) {
        // write your code here
        update(index, value);
    }
    
    private void update(int i, int val) {
        int delta = val - nums[i];
        nums[i++] = val;
        for (; i < fw.length; i += i & -i) {
            fw[i] += delta;
        }
    }
    
    private int query(int i) {
        i++;
        int res = 0;
        for (; i > 0; i -= i & -i) {
            res += fw[i];
        }
        return res;
    }
}
