/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 2, 2017
 */
package algorithm;

import java.util.Random;

/**
 * Problem Statement at 
 * https://leetcode.com/problems/linked-list-random-node/
 * 
 * Reservoir Sampling.
 * 
 * Given a stream of incoming numbers, how to randomly 
 * select one node from them with equal probability?
 * 
 * Solution: keep a "candiate" variable, 
 * at index i, with 1/i prob to choose that one to update candidate
 * 
 * so for ith node, its prob to be picked as final result is:
 * (1/i) *  (i / (i + 1)) * ((i + 1) / (i + 2)) * .... * (N-1)N = 1/N
 * 
 * 
 * An extension of this problem is that, how to select K node from an incoming
 * stream with equal probability.
 * 
 * Solution: keep a list of candidates of size k. For i-th (i > k), with a 
 * probability of k/i pick that node and replace a random node in candidates
 * list. 
 * 
 * so for any i-th (i > k) its prob of been eliminated is
 *   (i - k) / i *  
 *
 * 
 ****/
public class LinkedListRandomNode_LC382 {

	class ListNode {
		int val;
		ListNode next;
		ListNode(int x) { val = x; }
	}
	
	public static void main(String[] args) {

	}
	
	ListNode head = null;
    Random rand = new Random();
    
    /** @param head The linked list's head.
        Note that the head is guaranteed to be not null, 
        so it contains at least one node. */
    public LinkedListRandomNode_LC382(ListNode head) {
        this.head = head; 
    }
    
    /** Returns a random node's value. */
    public int getRandom() {
        ListNode p = head;
        ListNode selected = null;
        for (int i = 0; p != null; i++, p = p.next) {
            if (i == rand.nextInt(i + 1)) {
                selected = p;
            }
        }
        
        return selected.val;
    }
}
