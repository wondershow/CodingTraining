/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 21, 2017
 */
package algorithm;
/**
 * https://leetcode.com/problems/median-of-two-sorted-arrays/
 * 
 * 
 * 
 * **/
public class MedianTwoSortedArrays_LC4 {

	public static void main(String[] args) {

	}
	
	/**
	 * This is a binary search method. Each time we remove 
	 * half elements until we find the last single one element.
	 * Mistakes made:
	 * 1. The 1st array should be shorter than 2nd one, this makes
	 *    sure that 2nd array can never be overflow
	 * 2. The element of k/2-th element pick is tricky, use
	 *    an example to derive the relation.
	 * **/
	public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.length, n = nums2.length;
        if (m > n) {
            int[] tmp = nums1;
            nums1 = nums2;
            nums2 = tmp;
        }
        return 0.5 * (double) (kthElement(nums1, nums2, 0, 0, 1 + (m + n) / 2)  + kthElement(nums1, nums2, 0, 0, 1 + (m + n - 1) / 2)); 
    }
    
    private int kthElement(int[] nums1, int[] nums2, int lo1, int lo2, int rank) {
        //System.out.println("lo1 = " + lo1 + " lo2 = " + lo2 + ", rank = " + rank);
        
        if (lo1 >= nums1.length) {
            return nums2[lo2 + rank - 1];
        }
        if (lo2 >= nums2.length) {
            return nums1[lo1 + rank - 1];
        }
        if (rank == 1) {
            return Math.min(nums1[lo1], nums2[lo2]);
        }
        
        int ele1 = (nums1.length - lo1) < rank / 2 ? Integer.MAX_VALUE : nums1[lo1 + rank / 2 - 1];     
        int ele2 = nums2[lo2 + rank / 2 - 1];
        
        if (ele1 < ele2) {
            int removed = Math.min(nums1.length - lo1, rank / 2);
            return kthElement(nums1, nums2, lo1 + removed, lo2, rank - removed);
        } else {
            return kthElement(nums1, nums2, lo1, lo2 + rank / 2, rank - rank / 2);
        }
    }
}
