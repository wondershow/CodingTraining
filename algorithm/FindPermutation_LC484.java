/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 24, 2017
 */
package algorithm;
/***
 * 
 * https://leetcode.com/problems/find-permutation/
 * 
 * A greedy algorithm, see solutions
 * at 
 * https://discuss.leetcode.com/topic/76276/1-liner-and-5-liner-visual-explanation
 * 
 * */
public class FindPermutation_LC484 {

	public static void main(String[] args) {

	}
	
	
	public int[] findPermutation(String s) {
        int len = s.length();
        int[] res = new int[len + 1];
        
        for (int i = 1; i <= len + 1; i++) {
            res[i - 1] = i;
        }
        
        int i = 0, j = 0;
        while (i < s.length()) {
            if (s.charAt(i) == 'D') {
                j = i; 
                while (j < s.length() && s.charAt(j) == 'D') {
                    j++;
                }
                reverse(res, i, j);
                i = j;
            } else {
                i++;
            }
        }
        
        return res;
    }
    
    private void reverse(int[] a, int i, int j) {
        while (i < j) {
            int tmp = a[i];
            a[i] = a[j];
            a[j] = tmp;
            i++;
            j--;
        }
    }
}
