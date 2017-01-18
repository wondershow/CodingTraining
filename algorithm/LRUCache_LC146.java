/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 18, 2017
 */
package algorithm;

import java.util.HashMap;
import java.util.Map;

/**
 * https://leetcode.com/problems/lru-cache/
 * this solution uses hashmap + double linked list
 * but the performance is only better than 0.62%, 182 ms
 * need to revisit this problem
 * Mistakes made:
 *    1. forget to intialize the head and tail nodes to make them
 *       point to each other.
 * 
 * **/
public class LRUCache_LC146 {

	public static void main(String[] args) {

	}

	
	class DLinkedList {
        int val, key;
        DLinkedList prev, next;
        DLinkedList(int v, int k) {
            val = v;
            key = k;
            prev = next = null;
        }
    }
    
    DLinkedList head, tail;
    int max;
    Map<Integer, DLinkedList> nodeByKey;
    public LRUCache_LC146(int capacity) {
        head = new DLinkedList(-1, -1);
        tail = new DLinkedList(-1, -1);
        head.next = tail;
        tail.prev = head;
        max = capacity;
        nodeByKey = new HashMap();
    }
    
    public int get(int key) {
        if (!nodeByKey.containsKey(key)) {
            return -1;
        }
        DLinkedList dnode = nodeByKey.get(key);
        moveToLast(dnode);
        return dnode.val;
    }
    
    public void put(int key, int value) {
        if (nodeByKey.containsKey(key)) {
            DLinkedList dnode = nodeByKey.get(key);
            dnode.val = value;
            moveToLast(dnode);
        } else {
            DLinkedList dnode = new DLinkedList(value, key);
            if (nodeByKey.size() == max) {
                removeFirst();
            }
            addToLast(dnode);
            nodeByKey.put(key, dnode);
        }
    }
    
    private void moveToLast(DLinkedList dnode) {
        DLinkedList prev = dnode.prev;
        DLinkedList next = dnode.next;
        prev.next = next;
        next.prev = prev;
        
        addToLast(dnode);
    }
    
    private void removeFirst() {
        DLinkedList first = head.next;
        DLinkedList second = first.next;
        head.next = second;
        second.prev = head;
        nodeByKey.remove(first.key);
    }
    
    private void addToLast(DLinkedList dnode) {
        DLinkedList oldLast = tail.prev;
        oldLast.next = dnode;
        dnode.prev = oldLast;
        dnode.next = tail;
        tail.prev = dnode;
    }
}
