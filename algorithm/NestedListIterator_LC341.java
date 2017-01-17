/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 17, 2017
 */
package algorithm;
/**
 * https://leetcode.com/problems/flatten-nested-list-iterator/
 * some thoughts:
 * whenever there is a hierarchical structure, the first thing 
 * to think about is a stack. (Of course another use of
 * stack can be used to maintain some orders, increasing
 * decreasing in stack elements).
 * Errors made:
 * 1. forget to consider empty list situation
 * 2. some typos.
 * **/



public class NestedListIterator_LC341 {

	public static void main(String[] args) {

	}
	
	Stack<NestedInteger> path;
    
    public NestedIterator(List<NestedInteger> l) {
        path = new Stack();
        for (int i = l.size() - 1; i >= 0; i--) {
            path.push(l.get(i));
        }
        gotoNext();
    }
    
    private void gotoNext() {
        while (!path.isEmpty() && !path.peek().isInteger()) {
            NestedInteger ni = path.pop();
            List<NestedInteger> l = ni.getList();
            for (int i = l.size() - 1; i >= 0; i--) {
                path.push(l.get(i));
            }
        }
    }

    public Integer next() {
        Integer res = path.pop().getInteger();
        gotoNext();
        return res;
    }

    public boolean hasNext() {
        return !path.isEmpty();
    }
}
