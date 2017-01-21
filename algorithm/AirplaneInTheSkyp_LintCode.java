/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 20, 2017
 */
package algorithm;

/***
 * http://www.lintcode.com/en/problem/number-of-airplanes-in-the-sky/#
 * 
 * One sweepline problem
 * 
 * */
public class AirplaneInTheSkyp_LintCode {

	public static void main(String[] args) {

	}
	
	class Event implements Comparable<Event> {
        int time;
        boolean isLanding;
        Event(int t, boolean b) {
            time = t;
            isLanding = b;
        }
        
        public int compareTo(Event that) {
            if (this.time == that.time) {
                if (this.isLanding) {
                    return -1;
                } else {
                    return  1;
                }
            } else {
                return this.time - that.time;
            }
        }
    } 
     
    public int countOfAirplanes(List<Interval> airplanes) { 
        // write your code here
        if (airplanes == null || airplanes.size() == 0) {
            return 0;
        }
        
        Event[] events = new Event[airplanes.size() * 2];
        
        for (int i = 0; i < airplanes.size(); i++) {
            Interval intval = airplanes.get(i);
            events[2 * i] = new Event(intval.start, false);
            events[2 * i + 1] = new Event(intval.end, true);
        }
        
        Arrays.sort(events);
        
        int res = 0, cnt = 0;
        for (int i = 0; i < events.length; i++) {
            if (events[i].isLanding) {
                cnt--;
            } else {
                cnt++;
            }
            res = Math.max(res, cnt);
        }
        
        return res;
    }
}
