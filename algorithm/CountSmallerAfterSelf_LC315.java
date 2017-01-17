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
    
    
    /*******
     * Solution 2:
     * This solution uses mergesort invariants to count the results.
     * errors made:
     * 1. failed to handle two equal elements in the merging phase.
     * 
     * Possible improvement, ditching using a wrapper class.
     * *******/
    
    class Wrapper {
        int val, cnt, index;
        Wrapper(int v, int i) {
            val = v;
            cnt = 0;
            index = i;
        }
    }
    
    public List<Integer> countSmaller1(int[] nums) {
        List<Integer> res = new ArrayList();
        if (nums == null || nums.length == 0) {
            return res;
        }
        
        Wrapper[] w = new Wrapper[nums.length];
        Wrapper[] aux = new Wrapper[nums.length];
        for (int i = 0; i < nums.length; i++) {
            w[i] = new Wrapper(nums[i], i);
            res.add(0);
        }
        mergesort(w, aux, 0, w.length - 1);
        
        for (int i = 0; i < w.length; i++) {
            res.set(w[i].index, w[i].cnt);
        }
        
        return res;
    }
    
    private void mergesort(Wrapper[] w, Wrapper[] aux, int lo, int hi) {
        if (lo >= hi) return;
        int mid = (lo + hi) >>> 1;
        mergesort(w, aux, lo, mid);
        mergesort(w, aux, mid + 1, hi);
        for (int i = lo; i <= hi; i++) {
            aux[i] = w[i];
        }
        
        int i = lo, j = mid + 1, k = lo;
        while (i <= mid || j <= hi) {
            if (i > mid) {
                w[k++] = aux[j++];
            } else if (j > hi) {
                w[k] = aux[i];
                w[k].cnt += hi - mid;
                k++;
                i++;
            } else if (aux[i].val <= aux[j].val) {
                w[k] = aux[i];
                w[k].cnt += j - mid - 1; 
                k++;
                i++;
            } else {
                w[k++] = aux[j++];
            }
        }
    }
    
    
    /**
     * Solution 3:
     * Small improvement over solution 2
     * ***/
    public List<Integer> countSmaller3(int[] nums) {
        List<Integer> res = new ArrayList();
        if (nums == null || nums.length == 0) {
            return res;
        }
        
        int[] indices = new int[nums.length];
        int[] counts = new int[nums.length];
        int[] aux = new int[nums.length];
        
        for (int i = 0; i < nums.length; i++) {
            indices[i] = i;
            counts[i] = 0;
        }
        
        mergesort(nums, counts, indices, aux, 0, nums.length - 1);
        
        for (int i = 0; i < nums.length; i++) {
            res.add(counts[i]);
        }
        
        return res;
    }
    
    private void mergesort(int[] values, int[] counts, int[] indices, int[] aux, int lo, int hi) {
        if (lo >= hi) return;
        int mid = (lo + hi) >>> 1;
        mergesort(values, counts, indices, aux, lo, mid);
        mergesort(values, counts, indices, aux, mid + 1, hi);
        
        for (int i = lo; i <= hi; i++) {
            aux[i] = indices[i];
        }
        
        int i = lo, j = mid + 1, k = lo;
        
        while (i <= mid || j <= hi) {
            if (i > mid) {
                indices[k++] = aux[j++];
            } else if (j > hi) {
                indices[k] = aux[i];
                counts[indices[k]] += hi - mid;
                k++;
                i++;
            } else if (values[aux[i]] <= values[aux[j]]) {
                indices[k] = aux[i];
                counts[indices[k]] += j - mid - 1; 
                k++;
                i++;
            } else {
                indices[k++] = aux[j++];
            }
        }
    }
    
}
