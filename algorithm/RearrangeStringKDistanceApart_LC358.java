/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 20, 2017
 */
package algorithm;

import java.util.Arrays;
/**
 * https://leetcode.com/problems/rearrange-string-k-distance-apart/
 * This is a greedy problem. Each time we may want to append a 
 * char within the remaning chars that has most count while 
 * does not violate the "K apart" condition, so we need 
 * an array lastPosition to remember the last position (index)
 * where each character apperas
 * **/
public class RearrangeStringKDistanceApart_LC358 {

	public static void main(String[] args) {

	}

	
	public String rearrangeString(String str, int k) {
        if (str == null || str.length() == 0) {
            return "";
        }
        
        if (k == 0) {
            return str;
        }
        
        int[] hash = new int[26];
        int[] lastPositions = new int[26];
        Arrays.fill(lastPositions, -1);
        for (char c : str.toCharArray()) {
            hash[c - 'a']++;
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < str.length(); i++) {
            int offset = nextChar(lastPositions, hash, k, i);
            if (offset == -1) return "";
            lastPositions[offset] = i;
            hash[offset]--;
            sb.append((char)(offset + 'a') + "");
        }
        
        return sb.toString();
    }
    
    private int nextChar(int[] lastPositions, int[] hash, int k, int pos) {
        int max = 0, res = -1;
        for (int i = 0; i < hash.length; i++) {
            if ((lastPositions[i] == -1 || pos - lastPositions[i] >= k ) && hash[i] > max) {
                max = hash[i];
                res = i;
            }
        }
        
        return res;
    }
}
