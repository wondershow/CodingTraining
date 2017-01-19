/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 18, 2017
 */
package algorithm;
/**
 * https://leetcode.com/problems/h-index/
 * Two binarysearch solve the problem. 
 * 
 * **/
import java.util.Arrays;

public class HIndex_LC274 {

	public static void main(String[] args) {

	}
	
	public int hIndex(int[] citations) {
        if (citations == null || citations.length == 0) {
            return 0;
        }
        
        Arrays.sort(citations);
        int lo = 0, hi = citations.length;
        while (lo + 1 < hi) {
            int mid = (lo + hi) >>> 1;
            if (isHIndex(mid, citations)) {
                lo = mid;
            } else {
                hi = mid;
            }
        }
        
        if (isHIndex(hi, citations)) return hi;
        else return lo;
    }
    
    private boolean isHIndex (int h, int[] citations) {
        int first = findFirst(citations, h);
        return (citations.length - first) >= h;
    }
    
    //find 1st elment larger or equal than h
    private int findFirst(int[] citations, int h) {
        int lo = 0, hi = citations.length - 1;
        while (lo + 1 < hi) {
            int mid = (lo + hi) >>> 1;
            if (citations[mid] < h) {
                lo = mid;
            } else {
                hi = mid;
            }
        }
        if (citations[lo] >= h) return lo;
        else if (citations[hi] >= h) return hi;
        return hi + 1;
    }

}
