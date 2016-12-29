package algorithm;

import java.util.ArrayList;
import java.util.List;

public class SingleNumberLC260 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	public int[] singleNumber(int[] nums) {
        if (nums == null || nums.length == 0) return nums;
        
        int xor = nums[0];
        for (int i = 1; i < nums.length; i++) {
            xor ^= nums[i];
        }
        
        /**
                    xor:  100010010110000
                xor - 1:  100010010101111
          xor & xor - 1:  100010010100000
          bitOfOne:       000000000010000
        **/
        int bitOfOne = xor - (xor & (xor - 1));
        
        List<Integer> group1 = new ArrayList<Integer>();
        List<Integer> group2 = new ArrayList<Integer>();
        
        for (int num : nums) {
            if ((num & bitOfOne) == 0) {
                group1.add(num);
            } else {
                group2.add(num);
            }
        }
        
        int[] res = new int[2];
        for (int i = 1; i < group1.size(); i++) {
            group1.set(0, group1.get(0) ^  group1.get(i));
        }
        
        for (int i = 1; i < group2.size(); i++) {
            group2.set(0, group2.get(0) ^  group2.get(i));
        }
        
        res[0] = group1.get(0);
        res[1] = group2.get(0);
        
        return res;
    }
}
