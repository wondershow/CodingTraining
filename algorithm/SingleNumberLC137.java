package algorithm;

public class SingleNumberLC137 {

	public static void main(String[] args) {
		
	}
	
	/**
    5:   1 0 1
    6:   1 1 0    
    5:   1 0 1
    5:   1 0 1
    -----------------    
	bitCount:   4 1 3          
	bitCount%3:   1 1 0    
	***/
	public int singleNumber(int[] nums) {
		if (nums.length == 1) {
		    return nums[0];
		}
		
		int res = 0;
		for (int i = 0; i <= 31; i++) {
		    int bitCount = 0;
		    for (int num : nums) {
		        bitCount += (num >> i) & 1;
		    }
		    bitCount %= 3;
		    res |= (bitCount << i);
		}
		return res;
	}
}
