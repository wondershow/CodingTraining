/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 13, 2017
 */
package algorithm;

import java.util.ArrayList;
import java.util.List;

/**
 * See problem statement at
 * https://leetcode.com/problems/encode-and-decode-strings/
 * The key of this problem is that we need to handle
 * 3 edge cases:
 * when the List is empty(size is 0);
 * when the list elements is/are empty string
 * and what delimiter we need to use
 * **/

public class StringCodec_LC271 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	// Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for (String word : strs) {
            for (char ch : word.toCharArray()) {
                if (ch == 'a') {
                    sb.append("ab");
                } else {
                    sb.append(ch);
                }
            }
            sb.append("aa");
        }
        return sb.toString();
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
        List<String> res = new ArrayList<String>();
        if (s.length() == 0) {
            return res;
        }
        
        //remove the tailing "aa" delimiter
        s = s.substring(0, s.length() - 2);
        String[] words = s.split("aa", -1);
        
        for (String word : words) {
            res.add(word.replaceAll("ab", "a"));
        }
        
        return res;
    }
}
