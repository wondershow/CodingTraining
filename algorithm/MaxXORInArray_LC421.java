/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 22, 2017
 */
package algorithm;

/**
 * https://leetcode.com/submissions/detail/90180944/
 * 
 * 
 * 
 * */

public class MaxXORInArray_LC421 {

	public static void main(String[] args) {

	}
	
	class TrieNode {
        TrieNode[] kids;
        TrieNode() {
            kids = new TrieNode[2];
        }
    }
    
    public int findMaximumXOR(int[] nums) {
        TrieNode root = new TrieNode();
        
        for (int num : nums) {
            TrieNode p = root;
            for (int i = 30; i >= 0; i--) {
                int bit = (num & (1 << i)) == 0 ? 0 : 1;
                if (p.kids[bit] == null) {
                    p.kids[bit] = new TrieNode();
                }
                p = p.kids[bit];
            }
        }
        
        
        int max = 0;
        for (int num : nums) {
            TrieNode p = root;
            int res = 0;
            for (int i = 30; i >= 0; i--) {
                int bit = (num & (1 << i)) == 0 ? 0 : 1;
                if (p.kids[bit ^ 1] != null) {
                    res |= (1 << i);
                    p = p.kids[bit ^ 1];
                } else {
                    p = p.kids[bit];
                }
            }
            max = Math.max(res, max);
        }
        
        return max;
    }
}
