/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 13, 2017
 */
package algorithm;

import java.util.Arrays;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;
/**
 * See problem statement at 
 * https://leetcode.com/problems/queue-reconstruction-by-height/
 * greedy
 * **/
public class QueueReconstruction_LC406 {

	public static void main(String[] args) {

	}

	public int[][] reconstructQueue(int[][] people) {
        List<int[]> list = new LinkedList();
        if (people == null || people.length == 0) {
            return new int[0][2];
        }
        
        Arrays.sort(people, new Comparator<int[]>() {
            public int compare(int[] a, int[] b) {
                if (a[0] == b[0]) {
                    return a[1] - b[1];
                } else {
                    return b[0] - a[0];
                }
            }
        });
        
        
        for (int[] ppl : people) {
            list.add(ppl[1], ppl);
        }
    
        int[][] res = new int[list.size()][2];
        for (int i = 0; i < list.size(); i++) {
            res[i] = list.get(i);
        }
        
        return res;
    }
}
