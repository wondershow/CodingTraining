/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 20, 2017
 */
package algorithm;

import java.util.Arrays;
import java.util.Comparator;

/**
 * https://leetcode.com/problems/meeting-rooms/
 * Sweep line problem
 * */
public class MeetingRooms_LC252 {

	public static void main(String[] args) {

	}
	
	public boolean canAttendMeetings(Interval[] intervals) {
        Arrays.sort(intervals, new Comparator<Interval>() {
           public int compare(Interval a, Interval b) {
               return a.start - b.start;
           } 
        });
        
        int lastMeetingEnds = Integer.MIN_VALUE;
        for (int i = 0; i < intervals.length; i++) {
            if (intervals[i].start < lastMeetingEnds) {
                return false;
            }
            lastMeetingEnds = intervals[i].end;
        }
        
        return true;
    }
}
