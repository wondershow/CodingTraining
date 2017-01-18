/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 18, 2017
 */
package algorithm;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Random;

/**
 * https://leetcode.com/problems/insert-delete-getrandom-o1/
 * **/
public class InsertDeleteGetRandomO1_LC380 {

	public static void main(String[] args) {

	}
	HashMap<Integer, Integer> indexByVal;
    List<Integer> list;
    Random rand;
    /** Initialize your data structure here. */
    public InsertDeleteGetRandomO1_LC380() {
        indexByVal = new HashMap();
        list = new ArrayList();
        rand = new Random();
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    public boolean insert(int val) {
        if (!indexByVal.containsKey(val)) {
            indexByVal.put(val, list.size());
            list.add(val);
            return true;
        }
        return false;
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    public boolean remove(int val) {
        if (indexByVal.containsKey(val)) {
            if (indexByVal.get(val) != list.size() - 1) {
                int lastVal = list.get(list.size() - 1);
                int valIndex = indexByVal.get(val);
                list.set(valIndex, lastVal);
                indexByVal.put(lastVal, valIndex);
            }
            list.remove(list.size() - 1);
            indexByVal.remove(val);
            return true;
        }
        return false;
    }
    
    /** Get a random element from the set. */
    public int getRandom() {
        return list.get(rand.nextInt(list.size()));
    }
}
