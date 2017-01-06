/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 3, 2017
 */
package algorithm;

import java.util.HashMap;
import java.util.Map;
/**
 * See problem statement at
 * https://leetcode.com/problems/lru-cache/ * 
 * This is a pretty time-consuming coding question.
 * 
 * Hints of data structure.
 * 1. There should be a data structure where we can delete in the
 * middle while add in the end.
 * 2. We should be able to delete the first (oldest) item in the 
 * structure.
 * 
 * Given these two points, A "List" comes to our mind natural mind.
 * However, in order to delete a node in the middle of a list, 
 * we need to know both its previous node and next node. With 
 * a linked list, we are able to locate a node and delete
 * in o(n) time.
 * 
 * However if this deletion is pretty frequent(can be interpreted 
 * from this problem's statement), 
 * we may consider the cost of locating a node with o(n) to be too
 * high. In order to quickly find a thing, a Hash is a natural 
 * outcome. Given a quick way to locate a node in a list, how to 
 * delete it in o(1) time? We need to know its predecessor either
 * by 1) using a hash to remember each node's previous
 *    2) using a double-linked list.
 *    
 * Some tricky points of this problem.
 * 1. hash value needs to be updated whenever a key exists in a hash
 * 2. we need to use to dummy nodes as head and tail of a double
 *    linked list. this makes our coding much easier. 
 * 
 * **/
public class LRU_LC146 {

	public static void main(String[] args) {

	}
	
	class DLinkNode {
        DLinkNode next, prev;
        int key, val;
        DLinkNode(int k, int v) {
            key = k;
            val = v;
        }
    }
    
    int limit;
    Map<Integer, DLinkNode> nodeByKey;
    DLinkNode head, tail;
    
    public LRU_LC146(int capacity) {
        limit = capacity;
        nodeByKey = new HashMap();
        head = new DLinkNode(-1, -1);
        tail = new DLinkNode(-1, -1);
        head.next = tail;
        tail.prev = head;
    }

    public int get(int key) {
        if (!nodeByKey.containsKey(key)) {
            return -1;
        }
        DLinkNode n = nodeByKey.get(key);
        delete(n);
        appendNode(n);
        return n.val;
    }
    
    private void delete(DLinkNode n) {
        DLinkNode left = n.prev;
        DLinkNode right = n.next;
        left.next = right;
        right.prev = left;
    }
    
    private void appendNode(DLinkNode n) {
        DLinkNode last = tail.prev;
        last.next = n;
        n.next = tail;
        n.prev = last;
        tail.prev = n;
    }

    public void set(int key, int value) {
        if (!nodeByKey.containsKey(key)) {
            if (nodeByKey.size() == limit) {
                DLinkNode oldest = head.next;
                nodeByKey.remove(oldest.key);
                delete(oldest);
            }
            DLinkNode newnode = new DLinkNode(key, value);
            nodeByKey.put(key, newnode);
            appendNode(newnode);
        } else {
            DLinkNode n = nodeByKey.get(key);
            n.val = value;
            delete(n);
            appendNode(n);
        }
    }
}
