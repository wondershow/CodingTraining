/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 14, 2017
 */
package algorithm;
/***
 * See problem statement at 
 * https://leetcode.com/problems/merge-intervals/
 * Nothing special
 * 
 * **/
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Interval {
	int start;
	int end;
	Interval() { start = 0; end = 0; }
	Interval(int s, int e) { start = s; end = e;}
}


public class MergeIntervals_LC56 {

	public static void main(String[] args) {
		
	}
	
	public List<Interval> merge(List<Interval> intervals) {
        List<Interval> res = new ArrayList<Interval>();
        if (intervals == null || intervals.size() == 0) {
            return res;
        }
        Collections.sort(intervals, new Comparator<Interval>() {
            public int compare(Interval a, Interval b) {
                if (a.start == b.start) {
                    return a.end - b.end;
                } else {
                    return a.start - b.start;
                }
            }
        });
        
        int low = intervals.get(0).start, hi = intervals.get(0).end;
        for (Interval in : intervals) {
            if (in.start > hi) {
                res.add(new Interval(low, hi));
                low = in.start;
                hi = in.end;
            } else {
                hi = Math.max(hi, in.end);
            }
        }
        
        res.add(new Interval(low, hi));
        
        return res;
    }
}
