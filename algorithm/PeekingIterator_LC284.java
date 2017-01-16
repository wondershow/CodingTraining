/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 15, 2017
 */
package algorithm;

import java.util.Iterator;

/**
 * See problem statement at 
 * https://leetcode.com/problems/peeking-iterator/
 * Errors made:
 * 1. i created another list to cache the whole elements in the iterator
 *    which is not acceptable
 * 2. Key thing is to hold the next element in the iterator in advance
 * 
 * 
 * **/
public class PeekingIterator_LC284 {

	public static void main(String[] args) {

	}
	
	Integer next;
    Iterator<Integer> it;
	public PeekingIterator_LC284(Iterator<Integer> it) {
	    next = it.next();
	    this.it = it;
	}

    // Returns the next element in the iteration without advancing the iterator.
	public Integer peek() {
	    return next;
	}

	// hasNext() and next() should behave the same as in the Iterator interface.
	// Override them if needed.
	public Integer next() {
	    Integer tmp = next;
	    if (it.hasNext())
	        next = it.next();
	    else
	        next = null;
	    return tmp;
	}

	public boolean hasNext() {
	    return next != null;
	}
}
