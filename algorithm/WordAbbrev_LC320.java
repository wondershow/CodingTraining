/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 15, 2017
 */
package algorithm;

import java.util.ArrayList;
import java.util.List;

/**
 * See problem statement at:
 * https://leetcode.com/problems/generalized-abbreviation/
 * errors made: 
 * 1. when a given path, forget to determine if last char
 *    of path is a length, producing invalid results as
 *    "w11d"
 * **/
public class WordAbbrev_LC320 {

	public static void main(String[] args) {

	}

	public List<String> generateAbbreviations(String word) {
        List<String> res = new ArrayList<String>();
        if (word == null || word.length() == 0) {
            res.add("");
            return res;
        }
        helper(word, 0, "", res);
        return res;
    }
    
    private void helper(String word, int pos, String path, List<String> res) {
        if (pos == word.length()) {
            res.add(path);
            return;
        }
        
        for (int i = pos + 1; i <= word.length(); i++) {
            if (i == pos + 1) {
                helper(word, i, path + word.substring(pos, i), res);
            }
            if (path.length() > 0 && Character.isDigit(path.charAt(path.length() - 1))) {
                break;
            }
            helper(word, i, path + (i - pos), res);
        }
    }
}
