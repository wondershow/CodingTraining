/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 11, 2017
 */
package algorithm;
/**
 * See problem statement at:
 * https://leetcode.com/problems/zigzag-iterator/
 * edge case missing: when the 1st list is an empty set
 * **/
import java.util.ArrayList;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;

public class ZigZagIterator_LC281 {

	public static void main(String[] args) {

	}

	LinkedList<Iterator> list;
    public ZigZagIterator_LC281(List<Integer> v1, List<Integer> v2) {
        list = new LinkedList<Iterator>();
        if (v1 != null && v1.size() > 0) list.add(v1.iterator());
        if (v2 != null && v2.size() > 0) list.add(v2.iterator());
    }

    public int next() {
        Iterator it = list.poll();
        Integer res = (Integer)it.next();
        if (it.hasNext()) list.add(it);
        return res; 
    }

    public boolean hasNext() {
        return list.size() > 0;
    }
}
