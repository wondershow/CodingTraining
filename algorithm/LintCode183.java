/***
 * Made 2 mistakes:
 * 1. hi count be 0 (k is too big)
 * 2. lo can not start from 0 (divided by 0)
 * **/
public class LintCode183 {

	/**
     * @param L: Given n pieces of wood with length L[i]
     * @param k: An integer
     * @return: The maximum length of the small pieces
     */
    public int woodCut(int[] L, int k) {
        // write your code here
        if (L == null || L.length == 0) {
            return 0;
        }
        
        long sum = 0;
        for (int i = 0; i < L.length; i++) {
            sum += (long) L[i];
        }
        
        int lo = 1, hi = (int) (sum / (long) k);
        
        if (hi == 0) {
            return 0;
        }
        
        while (lo + 1 < hi) {
            int mid = lo + (hi - lo) / 2;
            if (totalCut(L, mid) >= k) {
                lo = mid;
            } else {
                hi = mid;
            }
        }
        
        if (totalCut(L, hi) >= k) {
            return hi;
        }
        
        if (totalCut(L, lo) >= k) {
            return lo;
        }
        return 0;
    }
    
    int totalCut(int[] L, int size) {
        int res = 0;
        for (int i = 0; i < L.length; i++) {
            res += L[i] / size;
        }
        return res;
    }
}
