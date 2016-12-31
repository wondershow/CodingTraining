/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Dec 31, 2016
 */
package algorithm;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


public class CountSmallerAfterSelf_LC315 {

	public static void main(String[] args) {
		
	}
	/**
	 * This solution takes advantage of Segment tree to count how many 
	 * numbers smaller than self after
	 * Time complexity is expected to be o(nlogn) 
	 * space complexity is o(n).
	 * Should be better performance solutions
	 * ***/
	class TreeNode {
        int sum, start, end;
        TreeNode left, right;
        TreeNode(int s, int e, int sum) {
            start = s;
            end = e;
            this.sum = sum;
            left = right = null;
        }
    }
    
    public List<Integer> countSmaller(int[] nums) {
        List<Integer> res = new ArrayList<Integer>();
        if (nums == null || nums.length == 0) {
            return res;
        }
        
        int[] copy = nums.clone();
        Arrays.sort(copy);
        Map<Integer, Integer> rankByIndex = new HashMap();
        for (int i = 0; i < nums.length; i++) {
            rankByIndex.put(i, binFindFirst(copy, nums[i]));
        }
        
        TreeNode root = buildSegTree(0, nums.length);
        
        for (int i = nums.length - 1; i >= 0; i--) {
            int rank = rankByIndex.get(i);
            res.add(sumRange(root, 0, rank - 1));
            increment(root, rank);
        }
        
        Collections.reverse(res);
        return res;
    }
    
    //reutrn the index int the nums where target first appear
    int binFindFirst(int[] nums, int target) {
        int lo = 0, hi = nums.length - 1;
        while (lo + 1 < hi) {
            int mid = (lo + hi) >>> 1;
            if (nums[mid] >= target) {
                hi = mid;
            } else {
                lo = mid;
            }
        }
        if (nums[lo] >= target) return lo;
        else return hi;
    }
    
    private TreeNode buildSegTree(int lo, int hi) {
        if (lo > hi) {
            return null;
        }
        if (lo == hi) {
            return new TreeNode(lo, hi, 0);
        }
        TreeNode root = new TreeNode(lo, hi, 0);
        int mid = (lo + hi) >>> 1;
        root.left = buildSegTree(lo, mid);
        root.right = buildSegTree(mid + 1, hi);
        return root;
    }
    
    private int sumRange(TreeNode root, int from, int to) {
        if (root == null || from > to || root.start > to || root.end < from) {
            return 0;
        }
        
        if (root.start >= from && root.end <= to) {
            return root.sum;
        }
        
        return sumRange(root.left, from, to) + sumRange(root.right, from, to);      
    }
    
    private void increment(TreeNode root, int index) {
        if (root == null || root.start > index || root.end < index) {
            return;
        }
        if (root.start == root.end && root.start == index) {
            root.sum++;
            return;
        }
        
        increment(root.left, index);
        increment(root.right, index);
        root.sum = 0;
        root.sum += root.left.sum;
        root.sum += root.right.sum;
    }

}
