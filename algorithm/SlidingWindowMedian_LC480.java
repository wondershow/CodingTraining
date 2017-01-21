/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 20, 2017
 */
package algorithm;
/**
 * https://leetcode.com/problems/sliding-window-median/
 * 
 * **/
public class SlidingWindowMedian_LC480 {

	public static void main(String[] args) {

	}
	
	class HashHeap {
        int[] heap;
        Map<Integer, Integer> freq;
        Map<Integer, Integer> posByVal;
        int cur, heapSize, max;
        boolean maxOrMinHeap;
        
        HashHeap(int capacity, boolean b) {
            cur = 1;
            max = capacity;
            heapSize = 0;
            heap = new int[capacity + 1];
            freq = new HashMap();
            posByVal = new HashMap();
            maxOrMinHeap = b;
        }
        
        private void sink(int i) {
            int kid = 2 * i;
            while (kid < cur) {
                if (maxOrMinHeap && kid < cur - 1 && heap[kid] < heap[kid + 1]) {
                    kid++;
                }
                if (!maxOrMinHeap && kid < cur - 1 && heap[kid] > heap[kid + 1]) {
                    kid++;
                }
                if (isHepified(i, kid)) {
                    break;
                }
                swap(i, kid);
                i = kid;
                kid = 2 * i;
            }
        }
        
        private void swim(int i) {
            while (i > 1) {
                if (isHepified(i / 2, i)) {
                    break;
                }
                swap(i, i / 2);
                i = i / 2;
            }
        }
        
        public void offer(int n) {
            if (freq.containsKey(n)) {
                freq.put(n, freq.get(n) + 1);
            } else {
                freq.put(n, 1);
                heap[cur] = n;
                posByVal.put(n, cur);
                swim(cur);
                cur++;
            }
            heapSize++;
        }
        
        private int poll() {
            int peekval = heap[1];
            //System.out.println(freq.size());
            if (freq.get(peekval) > 1) {
                freq.put(peekval, freq.get(peekval) - 1);
            } else {
                swap(1, cur - 1);
                cur--;
                //if (cur > 1) {
                sink(1);
                //}
                freq.remove(peekval);
            }
            heapSize--;
            return peekval;
        }
        
        private int peek() {
            return heap[1];
        }
        
        private void remove(int n) {
            //System.out.println("# of different values " + freq.size()) ;
            if (freq.get(n) > 1) {
                freq.put(n, freq.get(n) - 1);
            } else {
                int pos = posByVal.get(n);
                swap(pos, cur - 1);
                cur--;
                if (pos > 0) {
                    sink(pos);
                }
                swim(pos);
                freq.remove(n);
            }
            //System.out.println("# of different values after" + freq.size()) ;
            heapSize--;
        }
        
        private boolean isHepified(int parent, int kid) {
            if (maxOrMinHeap) {
                return heap[parent] > heap[kid];
            }
            return heap[parent] < heap[kid];
        }
        
        private void swap(int i, int j) {
            int tmp = heap[i];
            heap[i] = heap[j];
            heap[j] = tmp;
            posByVal.put(heap[i], i);
            posByVal.put(heap[j], j);
        }
        
        private int size() {
            return heapSize;
        }
    }
    
    /***
     * This solution makes use of HashHeap, which is a kinda 
     * very advanced data structure. The normal heap takes o(n)
     * time to delete one element(non-head) and it does
     * not allow duplicated elements. There is a way to 
     * improve the deletion performance by adding a hashmap
     * to remember the position of a heap element. Then the 
     * deletion can be improved to o(logn). However, you 
     * are supposed to implement this HashHeap by hand.
     * Mistakes I made:
     * 1. The heap array starts from index 1;
     * 2. ALl the following mistakes originated from error1.
     * 
     * **/
    public double[] medianSlidingWindow1(int[] nums, int k) {
        double[] res = new double[nums.length - k + 1];
        
        System.out.println(res.length);
        
        HashHeap maxHeap = new HashHeap(k, true);
        HashHeap minHeap = new HashHeap(k, false);
        
        
        for (int i = 0; i < nums.length; i++) {
            
            if (maxHeap.size() == 0 || nums[i] < maxHeap.peek()) {
                //System.out.println("total  max size before:" + (maxHeap.size()));
                maxHeap.offer(nums[i]);
                //System.out.println("total  max size after:" + (maxHeap.size()));
            }  else {
                minHeap.offer(nums[i]);
            }
            
            //System.out.println("total size before:" + (maxHeap.size() + minHeap.size()));
            balance(minHeap, maxHeap);
            //System.out.println("total size after:" + (maxHeap.size() + minHeap.size()));
            
            if (i >= k - 1) {
                res[i - (k - 1)] = k % 2 == 0 ? ((double)maxHeap.peek() + (double)minHeap.peek()) / 2  : (double)maxHeap.peek();
                int toremove = nums[i - (k - 1)];
                
                
                //System.out.println("toremove " + toremove);
                //System.out.println("maxHeap peak " + maxHeap.peek());
                //System.out.println("minHeap peak " + minHeap.peek());
                //toremove = 282475249;
                if (toremove <= maxHeap.peek()) {
                    maxHeap.remove(toremove);
                } else {
                    minHeap.remove(toremove);
                }
                balance(minHeap, maxHeap);
            }
        }
        
        return res;
    }
    
    //rebalace the two heaps, maxHeap may hold at most 1 more element or equal number of 
    //element as minHeap;
    private void balance(HashHeap minHeap, HashHeap maxHeap) {
        while (maxHeap.size() > minHeap.size() + 1) {
            int tmp = maxHeap.poll();
            //if (tmp == 282475249) {
            //    System.out.println("max to min");
            //}
            minHeap.offer(tmp);
        }
        while (minHeap.size() > maxHeap.size()) {
            int tmp = minHeap.poll();
            maxHeap.offer(tmp);
            //if (tmp == 282475249) {
            //    System.out.println("min to max");
            //    System.out.println(maxHeap.peek());
            //}
        }
    }

}
