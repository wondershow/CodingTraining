/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 15, 2017
 */
package algorithm;
/**
 * See problem statement at
 * https://leetcode.com/problems/strobogrammatic-number-ii/
 * errors made:
 *  Dont know when to wrap "0" to a given string, 
 *  solution, in the parameters of recursion function, 
 *  use a parameter to indicate the outer most recursion
 *  recursion depth, when reach that depth, we dont wrap
 *  strings with "0".
 * **/
import java.util.ArrayList;
import java.util.List;

public class StrobogrammaticNumber2_LC247 {

	public static void main(String[] args) {

	}

	public List<String> findStrobogrammatic(int n) {
        return helper(n, n);
    }
    
    private List<String> helper(int n, int m){
        List<String> res = new ArrayList<String>();
        if (n <= 0) {
            res.add("");
            return res;
        }
        if (n == 1) {
            res.add("0");
            res.add("1");
            res.add("8");
            return res;
        }
        List<String> smaller = helper(n - 2, m);
        for (String str : smaller) {
            if (m != n) {
                res.add("0" + str + "0");
            }
            res.add("1" + str + "1");
            res.add("8" + str + "8");
            res.add("9" + str + "6");
            res.add("6" + str + "9");
        }
        return res;
    }
}
