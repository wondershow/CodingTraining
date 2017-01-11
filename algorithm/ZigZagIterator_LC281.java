/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 11, 2017
 */
package algorithm;
/**
 * See problem statement at:
 * https://leetcode.com/problems/zigzag-iterator/
 * 
 * **/
import java.util.ArrayList;
import java.util.List;

public class ZigZagIterator_LC281 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

	int totalSize = 0, cur = 0, ptr = 0;
    int[] ptrs;
    List<List<Integer>> lists;
    public ZigZagIterator_LC281(List<Integer> v1, List<Integer> v2) {
        totalSize = v1.size() + v2.size();
        ptrs = new int[2];
        lists = new ArrayList();
        lists.add(v1);
        lists.add(v2);
    }

    public int next() {
        while (ptrs[ptr] >= lists.get(ptr).size()) {
            ptr = (ptr + 1) % lists.size();
        }
        int res = lists.get(ptr).get(ptrs[ptr]);
        ptrs[ptr]++;
        cur++;
        ptr = (ptr + 1) % lists.size(); 
        return res++; 
    }

    public boolean hasNext() {
        return cur < totalSize;
    }
}
