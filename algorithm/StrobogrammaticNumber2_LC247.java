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
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

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
    
    
    /**
     * another solution based on combination
     * */
    public List<String> findStrobogrammatic2(int n) {
        Map<Character, Character> map = new HashMap();
        map.put('0', '0');
        map.put('1', '1');
        map.put('8', '8');
        map.put('6', '9');
        map.put('9', '6');
        char[] chars = new char[n];
        List<String> res = new LinkedList();
        if (n % 2 != 0) {
            chars[n / 2] = '0';
            helper(n / 2 - 1, chars, n, res, map);
            chars[n / 2] = '1';
            helper(n / 2 - 1, chars, n, res, map);
            chars[n / 2] = '8';
            helper(n / 2 - 1, chars, n, res, map);
        } else {
            helper(n / 2 - 1, chars, n, res, map);
        }
        
        return res;
    }
    
    private void helper(int pos, char[] chars, int n, List<String> res, Map<Character, Character> map) {
        if (pos <= 0) {
            if (pos == 0) {
                String tmp = "1896";
                for (int i = 0; i < tmp.length(); i++) {
                    chars[0] = tmp.charAt(i);
                    chars[n - 1] = map.get(tmp.charAt(i));
                    res.add(new String(chars));
                }
            } else {
                res.add(new String(chars));
            }
            return;
        }
        String tmp = "01896";
        for (int i = 0; i < tmp.length(); i++) {
            chars[pos] = tmp.charAt(i);
            chars[n - pos - 1] = map.get(tmp.charAt(i));
            helper(pos - 1, chars, n, res, map);
        }
    }
}
