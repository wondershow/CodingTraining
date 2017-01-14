/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 14, 2017
 */
package algorithm;
/**
 * 
 * Please see problem statement at:
 * https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
 * this problem very close to
 * https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
 * **/
public class LongestSubstring2Distinct_LC159 {

	public static void main(String[] args) {

	}
	
	public int lengthOfLongestSubstringKDistinct(String s, int k) {
        if (s == null || s.length() == 0 ) {
            return 0;
        }
        int[] hash = new int[256];
        int countOfDistinct = 0;
        int res = 0;
        for (int i = 0, j = 0; i < s.length(); i++) {
            while (j < s.length()) {
                if (countOfDistinct == k && hash[s.charAt(j)] == 0) {
                    break;
                } else {
                    if (hash[s.charAt(j++)]++ == 0) {
                        countOfDistinct++;
                    }
                }
            }
            res = Math.max(res, j - i);
            if (hash[s.charAt(i)]-- == 1) {
                countOfDistinct--;
            }
        }
        
        return res;
    }
}
