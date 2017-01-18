/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 18, 2017
 */
package algorithm;

/**
 * https://leetcode.com/problems/maximum-product-of-word-lengths/
 * The hints of this problem is kinda like to compute the 
 * intersection of two sets, we want to know if the two sets
 * has zero size intersection set. One possible solution is 
 * to use BitSet java API. however, noticed that the probleme
 * stated that only lower case letters are cosidered. So we
 * may use a 32-bit intertger to hold this info
 * 
 ***/
public class MaxProductOfWordLength_LC318 {

	public static void main(String[] args) {

	}
	
	public int maxProduct(String[] words) {
        int[] bits = new int[words.length];
        for (int i = 0; i < words.length; i++) {
            for (char c : words[i].toCharArray()) {
                bits[i] |= 1 << (c - 'a');
            }
        }
        int res = 0;
        for (int i = 0; i < words.length; i++) {
            for (int j = i + 1; j < words.length; j++) {
                if ( (bits[i] & bits[j]) == 0) {
                    res = Math.max(res, words[i].length() * words[j].length());
                }
            }
        }
        
        return res;
    }

}
