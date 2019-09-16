package algorithm;

public class LC875 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	public int minEatingSpeed(int[] piles, int H) {
        int lo = 1, hi = -1;
        for (int i = 0; i < piles.length; i++) {
            hi = Math.max(hi, piles[i]);
        }
        
        while (lo + 1 < hi) {
            int mid = lo + (hi - lo) / 2;
            if (canFinish(piles, mid, H)) {
                hi = mid;
            } else {
                lo = mid;
            }
        }
        
        if (canFinish(piles, lo, H)) {
            return lo;
        }
        return hi;
    }
    
    private boolean canFinish(int[] piles, int speed, int H) {
        int hours = 0;
        for (int i = 0; i < piles.length; i++) {
            hours += (int) Math.ceil((double)piles[i] / (double)speed);            
        }
        return hours <= H;    
    }
}
