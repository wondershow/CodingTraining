/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 13, 2017
 */
package algorithm;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

/**
 * See problem statement at:
 * https://leetcode.com/problems/unique-word-abbreviation/
 * The key things here:
 * 1. when the word is in the dictionary, how to handle
 * 2. when there are duplicates in the given dictionary, 
 *    how to handle
 * 3. (most common) when word is not in the dictionary.
 * **/
public class UniqewordAbbr_LC288 {

	public static void main(String[] args) {

	}
	
	Map<String, Integer> abbrfreq;
    Set<String> dict;
    public UniqewordAbbr_LC288(String[] dictionary) {
        abbrfreq = new HashMap();
        dict = new HashSet();
        for (String word : dictionary) {
            if (dict.contains(word)) continue;
            String abbr = getAbbr(word);
            abbrfreq.put(abbr, abbrfreq.getOrDefault(abbr, 0) + 1);
            dict.add(word);
        }
    }

    public boolean isUnique(String word) {
        String abbr = getAbbr(word);
        return !abbrfreq.containsKey(abbr)  || dict.contains(word) && abbrfreq.get(abbr) == 1;
    }
    
    private String getAbbr(String word) {
        if (word.length() <= 2) {
            return word;
        }
        return word.charAt(0) + "" + (word.length() - 2) + "" + word.charAt(word.length() - 1);
    }
}
