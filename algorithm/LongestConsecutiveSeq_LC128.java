/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 3, 2017
 */
package algorithm;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/**
 * See problem statements at 
 * https://leetcode.com/problems/longest-consecutive-sequence/
 * 
 * This is a typical Union-Find problem. Besides the standard
 * union-find solution, one big thing is how to handle duplicate
 * elements in the given array.
 * **/
public class LongestConsecutiveSeq_LC128 {

	public static void main(String[] args) {
	}
	
	int[] uf;
    int[] size;
    
    public int longestConsecutive(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        
        int len = nums.length;
        uf = new int[len];
        size = new int[len];
        Arrays.fill(size, 1);
        Arrays.fill(uf, -1);
        
        Map<Integer, Integer> indexByValue = new HashMap();
        for (int i = 0; i < len; i++) {
            if (indexByValue.containsKey(nums[i])) {
                //skip duplicates
                continue;
            }
            indexByValue.put(nums[i], i);
            if (indexByValue.containsKey(nums[i] - 1)) {
                union(i, indexByValue.get(nums[i] - 1));
            }
            if (indexByValue.containsKey(nums[i] + 1)) {
                union(i, indexByValue.get(nums[i] + 1));
            }
        }
        
        int res = 0;
        for (int i = 0; i < size.length; i++) {
            res = Math.max(res, size[i]);
        }
        
        return res;
    }
    
    private int root(int i) {
        if (uf[i] == -1) return i;
        uf[i] = root(uf[i]);
        return uf[i];
    }
    
    
    private void union(int i, int j) {
        int r1 = root(i);
        int r2 = root(j);
        if (r1 != r2) {
            if (size[r1] < size[r2]) {
                uf[r1] = r2;
                size[r2] += size[r1];
            } else {
                uf[r2] = r1;
                size[r1] += size[r2];
            }
        }
    }
}
