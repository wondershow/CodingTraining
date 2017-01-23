/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 23, 2017
 */
package algorithm;
/**
 * https://leetcode.com/problems/shortest-word-distance-ii/
 * 
 * HashMap + Array/List ops
 * 
 * **/
public class ShortestWordDistance2_LC244 {

	public static void main(String[] args) {

	}
	
Map<String, List<Integer>> locations;
    
    public WordDistance(String[] words) {
        locations = new HashMap();
        for (int i = 0; i < words.length; i++) {
            locations.putIfAbsent(words[i], new ArrayList());
            locations.get(words[i]).add(i);
        }
    }
    
    public int shortest(String word1, String word2) {
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
