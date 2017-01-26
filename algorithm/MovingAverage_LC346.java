/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 26, 2017
 */
package algorithm;


/**
 * https://leetcode.com/problems/moving-average-from-data-stream/
 * 
 * **/
public class MovingAverage_LC346 {

	public static void main(String[] args) {

	}
	
	int[] cirArray;
    int cur, size, sum, total;
    /** Initialize your data structure here. */
    public MovingAverage_LC346(int size) {
        this.size = size;
        cur = 0;
        sum = 0;
        total = 0;
        cirArray = new int[size];
    }
    
    public double next(int val) {
        sum -= cirArray[cur];
        cirArray[cur] = val;
        sum += cirArray[cur];
        cur = (cur + 1) % size;
        
        total++;
        if (total <= size) {
            return (double) sum / (double) total;
        } else {
            return (double) sum / (double) size;
        }
    }

}
