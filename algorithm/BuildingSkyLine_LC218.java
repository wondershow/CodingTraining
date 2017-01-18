/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 18, 2017
 */
package algorithm;
/**
 * https://leetcode.com/problems/the-skyline-problem/
 * 
 * **/
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;

public class BuildingSkyLine_LC218 {

	public static void main(String[] args) {

	}
	class Wrapper {
        int h, x, end;
        Wrapper(int _h, int _x, int e) {
            this.h = _h;
            this.x = _x;
            this.end = e;
        }
    }
    /***
     * Solution 1. using a heap + sweep line algorithms
     * Key points here:
     * Use a maxheap to keep the tallest building height, 
     * but to handle the duplicated heights, we may need a
     * hashmap to remember the frequency of each height.
     * 
     * When sort the building vertical lines on the x axis,
     * be careful when the xs is equal, 
     * case 1. entering buildings should be before leaving building.
     * case 2. when both leaving, shorter buildings should come before taller buildings
     * case 3. when both entering, taller buildings should come before shorter buildings.
     * 
     * 
     * Possible Improvements:
     * The bottleneck of this solution is the maxheap.remove() operation, it's time
     * complexity is o(n), which is unberable. So we may use a hashheap to improve the
     * remove operations to o(lgn).
     * **/
    public List<int[]> getSkyline1(int[][] buildings) {
        List<int[]> res = new ArrayList<int[]>();
        if (buildings == null || buildings.length == 0) {
            return res;
        }
        
        Wrapper[] lines = sortVerticalLines(buildings);
        Map<Integer, Integer> freq = new HashMap();
        PriorityQueue<Integer> maxHeap = new PriorityQueue(new Comparator<Integer>() {
            public int compare(Integer a, Integer b) {
                return b - a;
            }
        });
        
        
        for (int i = 0; i < lines.length; i++) {
            //System.out.println(lines[i].x + " " + lines[i].end);
            int curHeight = maxHeap.size() == 0 ? 0 : maxHeap.peek();
            Wrapper w = lines[i];
            if (w.end == 1) { // enter
                if (w.h > curHeight) {
                    res.add(new int[] {w.x, w.h});
                }
                if (freq.containsKey(w.h)) {
                    freq.put(w.h, freq.get(w.h) + 1);
                } else {
                    freq.put(w.h, 1);
                    maxHeap.offer(w.h);
                }
            } else { // leave
                if (w.h == curHeight && freq.get(w.h) == 1) {
                    maxHeap.poll();
                    int nextHeight = maxHeap.size() == 0 ? 0 : maxHeap.peek();
                    res.add(new int[]{w.x, nextHeight});
                    freq.remove(w.h);
                } else {
                    if (freq.get(w.h) > 1) {
                        freq.put(w.h, freq.get(w.h) - 1);
                    } else {
                        freq.remove(w.h);
                        maxHeap.remove(w.h);
                    }
                }
            }
        }
        
        return res;
    }
    
    
    private Wrapper[] sortVerticalLines(int[][] buildings) {
        Wrapper[] wraps = new Wrapper[2 * buildings.length];
        for (int i = 0; i < buildings.length; i++) {
            wraps[2 * i] = new Wrapper(buildings[i][2], buildings[i][0], 1);
            wraps[2 * i + 1] = new Wrapper(buildings[i][2], buildings[i][1], -1);
        }
        
        Arrays.sort(wraps, new Comparator<Wrapper>() {
            public int compare(Wrapper a, Wrapper b) {
                if (a.x == b.x) {
                    if (a.end == b.end) {
                        if (a.end == 1) {
                            return b.h - a.h;
                        } else {
                            return a.h - b.h;
                        }
                    } else {
                        return b.end - a.end;
                    }
                } else {
                    return a.x - b.x;
                }
            }
        });
        return wraps;
    }
}
