/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 20, 2017
 */
package algorithm;

import java.util.Arrays;
import java.util.Comparator;

/**
 * https://leetcode.com/problems/meeting-rooms-ii/
 * Sweepline problem
 * */
public class MeetingRooms2_LC253 {

	public static void main(String[] args) {

	}
	
	class Wrapper{
        int time;
        boolean isStart;
        Wrapper(int t, boolean b) {
            time = t;
            isStart = b;
        }
    }
    
    public int minMeetingRooms(Interval[] intervals) {
        if (intervals == null || intervals.length == 0) {
            return 0;
        }
        int len = intervals.length;
        Wrapper[] wraps = new Wrapper[2 * len];
        for (int i = 0; i < intervals.length; i++) {
            wraps[2 * i] = new Wrapper(intervals[i].start, true);
            wraps[2 * i + 1] = new Wrapper(intervals[i].end, false);
        }
        
        Arrays.sort(wraps, new Comparator<Wrapper>(){
            public int compare(Wrapper a, Wrapper b) {
                if (a.time == b.time) {
                    if (a.isStart) {
                        return 1;
                    } else {
                        return -1;
                    }
                } else {
                    return a.time - b.time;
                }
            }
        });
        
        int res = 0, cnt = 0;
        for (int i = 0; i < wraps.length; i++) {
            if (wraps[i].isStart) {
                cnt++;
            } else {
                cnt--;
            }
            res = Math.max(res, cnt);
        }
        
        return res;
    }
}
