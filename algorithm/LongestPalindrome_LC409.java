/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 19, 2017
 */
package algorithm;

public class LongestPalindrome_LC409 {

	public static void main(String[] args) {

	}
	
	public int longestPalindrome(String s) {
        if (s == null || s.length() == 0) {
            return 0;
        }
        
        int res = 0;
        int[] freq = new int[256];
        
        for (char c : s.toCharArray()) {
            freq[c]++;
        }
        for (int i = 0; i < 256; i++) {
            if (freq[i] == 0) continue;
            if (freq[i] % 2 == 1) {
                freq[i]--;
                if (res % 2 == 0) {
                    res++;
                }
            } 
            res += freq[i];
        }
        
        return res;
    }
}
