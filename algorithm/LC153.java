
public class LC153 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
	}
	
	public int findMin(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        int N = nums.length;
        if (nums[N - 1] > nums[0]) {
            return nums[0];
        }
        int lo = 0, hi = N - 1;
        while (lo + 1 < hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] > nums[lo]) {
                // at the upper part
                lo = mid;
            } else {
                // at the lower part
                hi = mid;                
            }
        }
        
        return nums[hi];
    }

}
