/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Feb 14, 2017
 */
package algorithm;
/**
 * http://www.lintcode.com/en/problem/4sum/
 * 
 * **/
public class FourSum_Lintcode58 {

	public ArrayList<ArrayList<Integer>> fourSum(int[] nums, int target) {
        /* your code */
        ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>>();
        if (nums == null || nums.length <= 3) return res;
        Arrays.sort(nums);
        
        int i, j, k, l;
        for (i = 0; i < nums.length - 3; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            for (j = i + 1; j < nums.length - 2; j++) {
                if (j > i + 1 && nums[j - 1] == nums[j])
                    continue;
                k = j + 1;
                l = nums.length - 1;
                while (k < l) {
                    int sum = nums[i] + nums[j] + nums[k] + nums[l];
                    if (sum == target) {
                        res.add(getList(nums[i], nums[j], nums[k], nums[l]));
                        k++;
                        l--;
                        while (k < l && nums[k] == nums[k - 1]) k++;
                        while (k < l && nums[l] == nums[l + 1]) l--;
                    } else if (sum > target) {
                        l--;
                    } else {
                        k++;
                    }
                }
            }
        }
        
        
        return res;
    }
    
    private ArrayList<Integer> getList(int a, int b, int c, int d) {
        ArrayList<Integer> res = new ArrayList<Integer>();
        res.add(a);
        res.add(b);
        res.add(c);
        res.add(d);
        return res;
    }

}
