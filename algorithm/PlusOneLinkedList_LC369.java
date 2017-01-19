/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 19, 2017
 */
package algorithm;

/**
 * https://leetcode.com/problems/plus-one-linked-list/
 * The key thing is int the recursion function, no need
 * to return a linked node, instead, a carry flag should be 
 * returned. 
 * **/
public class PlusOneLinkedList_LC369 {

	public static void main(String[] args) {

	}
	
	public ListNode plusOne(ListNode head) {
        if (sol1(head) == 1) {
            ListNode p = new ListNode(1);
            p.next = head;
            return p;
        } else {
            return head;
        }
    }
    
    private int sol1(ListNode head) {
        if (head == null) {
            return 1;
        }
        int carry = sol1(head.next);
        int res = (head.val + carry) / 10;
        head.val = (head.val + carry) % 10;
        return res;
    }

}
