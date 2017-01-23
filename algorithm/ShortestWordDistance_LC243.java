/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 23, 2017
 */
package algorithm;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * https://leetcode.com/problems/shortest-word-distance/
 * 
 * mistakes made:
 * 1. when compareing the distance of two words, instead of 
 *    compareing the real value l1.get(idx1) l2.get(idx2), 
 *    I compared idx1 and idx2, which is stupid, be careful 
 *    next time
 * 
 * **/
public class ShortestWordDistance_LC243 {

	public static void main(String[] args) {

	}
	
	public int shortestDistance(String[] words, String word1, String word2) {
        if (words == null || words.length == 0) {
            return 0;
        }
        
        Map<String, List<Integer>> locations = new HashMap();
        for (int i = 0; i < words.length; i++) {
            locations.putIfAbsent(words[i], new ArrayList());
            locations.get(words[i]).add(i);
        }
        
        List<Integer> l1 = locations.get(word1);
        List<Integer> l2 = locations.get(word2);
        
        int idx1 = 0, idx2 = 0;
        int res = Integer.MAX_VALUE;
        while (idx1 < l1.size() && idx2 < l2.size()) {
            res = Math.min(res, Math.abs(l1.get(idx1) - l2.get(idx2)));
            if (l1.get(idx1) < l2.get(idx2)) {
                idx1++;
            } else {
                idx2++;
            }
        }
        
        return res;
    }
}
