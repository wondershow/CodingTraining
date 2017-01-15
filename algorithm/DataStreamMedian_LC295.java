/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 14, 2017
 */
package algorithm;

import java.util.Comparator;
import java.util.PriorityQueue;

/**
 * See problem statement at
 * https://leetcode.com/problems/find-median-from-data-stream/
 * 
 * errors happened:
 * 1. the max heap comparator declared as a min heap
 * 2. did not consider the relatio of incoming element and 
 *    maxheap/minheap head.
 * 
 * */
public class DataStreamMedian_LC295 {

	public static void main(String[] args) {

	}

	
	PriorityQueue<Integer> maxHeap = new PriorityQueue(new Comparator<Integer>(){
        public int compare(Integer a, Integer b) {
            return b - a;
        }
    });
    PriorityQueue<Integer> minHeap = new PriorityQueue();

    // Adds a number into the data structure.
    public void addNum(int num) {
        if (maxHeap.size() == 0) {
            maxHeap.offer(num);
        } else {
            if (num > maxHeap.peek()) {
                minHeap.offer(num);
            } else {
                maxHeap.offer(num);
            }
            
            if (maxHeap.size() < minHeap.size()) {
                maxHeap.offer(minHeap.poll());
            }
            
            if (maxHeap.size() > minHeap.size() + 1) {
                minHeap.offer(maxHeap.poll());
            }
        }
    }

    // Returns the median of current data stream
    public double findMedian() {
        if (maxHeap.size() == minHeap.size()) {
            return ((double) maxHeap.peek()  + (double) minHeap.peek()) / 2;
        } else {
            return (double) maxHeap.peek();
        }
    }
}
