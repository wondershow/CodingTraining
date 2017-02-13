/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Feb 13, 2017
 */
package algorithm;
/**
 * See problem statement at :
 * http://www.lintcode.com/en/problem/heapify/
 * **/
public class Heapify_LintCode130 {
	public void heapify(int[] A) {
        // write your code here
        if (A == null || A.length <= 1) return;
        
        for (int i = A.length - 1; i >= 0; i--) {
            sink(A, i);
        }
    }
    
    private void sink(int[] A, int i) {
        int k = 2 * i + 1;
        while (k < A.length) {
            if (k < A.length - 1 && A[k] > A[k + 1]) k++;
            if (A[i] <= A[k]) break;
            swap(A, i, k);
            i = k;
            k = 2 * i + 1;
        }
    }
    
    private void swap(int[] A, int i, int j) {
        int tmp = A[i];
        A[i] = A[j];
        A[j] = tmp;
    }
}
