/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 21, 2017
 */
package algorithm;
/**
 * https://leetcode.com/problems/insert-interval/
 * 
 * my solution is little bit boring.
 * 
 * there is a simpler solutions. 3 stpes.
 * 
 * 1.add all list that is before newInterval
 * 
 * 2.add all list that intersects with newInterval
 * 
 * 3.add all lists after newInterval. 
 * 
 * 
 * */
public class InsertInterval_LC57 {

	public static void main(String[] args) {

	}
	
	public List<Interval> insert(List<Interval> intervals, Interval newInterval) {
        List<Interval> res = new ArrayList<Interval>();
        
        boolean merged = false;
        Interval leftOver = newInterval;
        
        for(int i = 0; i < intervals.size(); i++) {
            Interval cur = intervals.get(i);
            if (leftOver != null && intersects(leftOver, cur)) {
                leftOver.start = Math.min(leftOver.start, cur.start);
                leftOver.end = Math.max(leftOver.end, cur.end);
            } else {
                if (leftOver != null && leftOver.end < cur.start) {
                    res.add(leftOver);
                    leftOver = null;
                }
                res.add(cur);
            }
        }
        
        if (leftOver != null) {
            res.add(leftOver);
            leftOver = null;
        }
        
        return res;
    }
    
    private boolean intersects(Interval a, Interval b) {
        return !(a.end < b.start || a.start > b.end);
    }
    
    /**
     * Solution 2
     * **/
    public List<Interval> insert2(List<Interval> intervals, Interval newInterval) {
        List<Interval> res = new ArrayList<Interval>();
        
        int i = 0;
        
        while (i < intervals.size() && intervals.get(i).end < newInterval.start) {
            res.add(intervals.get(i));
            i++;
        }
        
        while (i < intervals.size() && intervals.get(i).start <= newInterval.end) {
            newInterval.start = Math.min(intervals.get(i).start, newInterval.start);
            newInterval.end = Math.max(intervals.get(i).end, newInterval.end);
            i++;
        }
        
        res.add(newInterval);
        
        while (i < intervals.size()) {
            res.add(intervals.get(i++));
        }
        
        return res;
    }
}
