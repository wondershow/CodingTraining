/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Feb 14, 2017
 */
package algorithm;
/**
 *http://www.lintcode.com/en/problem/valid-palindrome/ 
 * */
public class ValidPalindrome_LintCode415 {
	public boolean isPalindrome(String s) {
        // Write your code here
        if (s == null || s.length() <= 1) return true;
        
        int l = 0, r = s.length() - 1;
        
        while (l < r) {
            while (l < s.length() && !isAlphabeticOrNumberic(s.charAt(l))) l++;
            while (r >= 0 && !isAlphabeticOrNumberic(s.charAt(r))) r--;
            if (Character.toLowerCase(s.charAt(l++)) !=
                Character.toLowerCase(s.charAt(r--)))
            return false;
        }
        
        return true;
    }
    
    private boolean isAlphabeticOrNumberic(char c) {
        if (Character.isAlphabetic(c)) return true;
        if (Character.isDigit(c)) return true;
        return false;
    }
}
