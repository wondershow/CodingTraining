/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 3, 2017
 */
package algorithm;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * 30. Substring with Concatenation of All Words
 * See problem statement at
 * https://leetcode.com/problems/substring-with-concatenation-of-all-words/
 * 
 * Typical sliding window 2 pointers. Instead of moving
 * pointers character-by-character, need to move pointers
 * word-by-word.
 * */
public class LC30 {

	public static void main(String[] args) {
		
	}
	
	public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> res = new ArrayList<Integer>();
        if (s == null || words.length == 0) {
            return res;
        }
        
        Map<String, Integer> freq = new HashMap();
        
        for (String word : words) {
            freq.put(word, freq.getOrDefault(word, 0) + 1);
        }
        
        int count = 0, width = words[0].length();
        
        for (int offset = 0; offset < width; offset++) {
            for (int j = offset, k = offset; j + width <= s.length(); j += width) {
                while (k + width <= s.length()) {
                    if (count == words.length) {
                        break;
                    }
                    String word = s.substring(k, k + width);
                    if (freq.containsKey(word)) {
                        if (freq.get(word) > 0) {
                            count++;
                        }
                        freq.put(word, freq.get(word) - 1);
                    }
                    k += width;
                }
                if (k - j == words.length * width && count == words.length) {
                    res.add(j);
                }
                String w2 = s.substring(j, j + width);
                if (freq.containsKey(w2)) {
                    if (freq.get(w2) >= 0) {
                        count--;
                    }
                    freq.put(w2, freq.get(w2) + 1);
                }
            }
        }
        
        return res;
    }
}
