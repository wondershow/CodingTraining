/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 19, 2017
 */
package algorithm;

/**
 * https://leetcode.com/problems/add-strings/
 * 
 * **/
public class AddString_LC415 {

	public static void main(String[] args) {

	}
	
	public String addStrings(String num1, String num2) {
        StringBuilder sb = new StringBuilder("");
        int i = num1.length() - 1, j = num2.length() - 1;
        
        int carry = 0;
        while (i >= 0 || j >= 0) {
            int a1 = i >= 0 ? (num1.charAt(i) - '0') : 0;
            int a2 = j >= 0 ? (num2.charAt(j) - '0') : 0;
            sb.append((a1 + a2 + carry) % 10 + "");
            carry = (a1 + a2 + carry) / 10; 
            i--;
            j--;
        }
        
        if (carry == 1) {
            sb.append("1");
        }
        
        return sb.reverse().toString();
    }
}
