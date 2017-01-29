/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 29, 2017
 */
package algorithm;
/**
 * https://leetcode.com/problems/valid-word-abbreviation/
 * 
 * */
public class ValidWordAbbr_LC408 {

	public static void main(String[] args) {

	}

	public boolean validWordAbbreviation(String word, String abbr) {
        int i = 0, j = 0; 
        while (i < word.length() && j < abbr.length()) {
            if (word.charAt(i) == abbr.charAt(j)) {
                i++;
                j++;
                continue;
            }
            if (abbr.charAt(j) <= '0' || abbr.charAt(j) > '9') {
                return false;
            }
            int skip = 0;
            while (j < abbr.length() && Character.isDigit(abbr.charAt(j))) {
                skip = skip * 10 + (abbr.charAt(j) - '0');
                j++;
            }
            i += skip;
        }
        return i == word.length() && j == abbr.length();
    }
}
