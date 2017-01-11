/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 11, 2017
 */
package algorithm;
/**
 * See problem statement at 
 * https://leetcode.com/problems/license-key-formatting/
 * Very straightforward, scan from right to left and
 * do the formatting, two edge cases might be missing
 * 1. When there is only "-" in the string
 * 2. When there is a '-' at the beginning of the result, remove it
 * **/
public class LicenceFormating_LC482 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	public String licenseKeyFormatting(String S, int K) {
        
        StringBuilder sb = new StringBuilder();
        for (int i = S.length() - 1, j = 0; i >= 0; i--) {
            char ch = S.charAt(i);
            if (ch == '-' ) {
                continue;
            }
            sb.append(toUpperCase(ch));
            j++;
            if (j == K) {
                j = 0;
                sb.append("-");
            }
        }
        
        if (sb.length() > 0 && sb.charAt(sb.length() - 1) == '-') {
            sb.setLength(sb.length() - 1);
        }
        
        return sb.reverse().toString();
    }
    
    private char toUpperCase(char c) {
        if (c >= 97) {
            return (char) (c - 32);
        }
        return c;
    }

}
