package algorithm;

public class SingleNumberLC136 {

	public static void main(String[] args) {

	}
	
	public int singleNumber(int[] nums) {
        int res = nums[0];
        for (int i = 1; i < nums.length; i++) {
            res ^= nums[i];
        }
        return res;
    }
}
