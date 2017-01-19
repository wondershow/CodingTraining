/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 17, 2017
 */
package algorithm;

import java.util.ArrayList;
import java.util.List;
/**
 * 
 * https://leetcode.com/problems/binary-watch/
 * Mistakes made:
 * 1. the termination condition of the search process.
 *    wrong: when the position index is 0, that will miss the last digit
 *    correct: when the index = -1;
 * 2. 0:00 is correct while 12:00 is invalid
 *    so hour should be < 12s
 * 
 * **/
public class BinaryWatch_LC401 {

	public static void main(String[] args) {

	}
	
	public List<String> readBinaryWatch(int num) {
        List<String> res = new ArrayList<String>();
        helper(res, 0, 9, 0, num);
        return res;
    }
    
    private void helper(List<String> res, int time, int pos, int cnt, int num) {
        if (cnt == num) {
            String tmp = getTime(time);
            if (tmp != null) res.add(tmp);
            return;
        }
        if (pos <= -1) {
            return;
        }
        helper(res, time, pos - 1, cnt, num);
        helper(res, time | (1 << pos), pos - 1, cnt + 1, num);
    }
    
    private String getTime(int time) {
        int hour = time >> 6;
        int min = time & ((1 << 6) - 1);
        if (hour >= 12 || min >= 60) {
            return null;
        }
        
        return hour + ":" + (min <= 9 ? "0" : "") + min;
    }

}
