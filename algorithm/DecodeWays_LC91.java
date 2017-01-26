/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 25, 2017
 */
package algorithm;
/**
 * https://leetcode.com/problems/decode-ways/
 * Very Nasty problem
 * 
 * edge case check
 * when len == 0 reutrn 1;
 * when len == 1; reutrn char(0) == 0 ? 0 : 1;
 * when len > 1; return 0 if char(0) = 0;
 * 
 * DP
 * 1. state definition
 * dp[i] = means how many times s(0...i) can be decoded;
 * 2. transistion 
 *    case 1. when s(i) == '0'
 *            if s(i-1) == '0' return 0;
 *            if Int(s(i-1,i)) > 26 return 0;
 * 			  dp[i] = dp[i - 2];
 * 	  case 2: when s(i) != '0'
 *            case 2.1: s(i - 1) == '0'
 *                      dp[i] = dp[i - 1];
 *            case 2.2: s(i - 1) == '0'
 *                      when int(s(i-1,i) > 26)
 *                      		dp[i] = dp[i - 1];
 *                      when int(s(i-1,i) <= 26)
 *                      		dp[i] = dp[i - 1] + dp[i - 2];
 *
 * dp[0] = 1;
 * init : if (s(1) == '0') {
 * 				if (int(s(0,1) > 26)) {
 * 					return 0;	
 * 				} else {
 * 					dp[1] = 1;
 * 				}
 * 			} else {
 * 				if (int(s(0,1) > 26)) {
 * 					dp[1] = 1;	
 * 				} else {
 * 					dp[1] = 2;
 * 				}
 * 
 * 
 * 			}
 * 
 * 
 * 
 * **/
public class DecodeWays_LC91 {

	public static void main(String[] args) {

	}
	
	public int numDecodings(String s) {
        if (s == null || s.length() == 0) return 0;
        if (s.length() == 1) return s.charAt(0) == '0' ? 0 : 1;
        if (s.charAt(0) == '0') return 0;
        
        int len = s.length();
        int[] dp = new int[len];
        
        dp[0] = 1;
        
        if (s.charAt(1) == '0') {
            if (Integer.parseInt(s.substring(0,2)) <= 26) {
                dp[1]  = 1;
            } else {
                return 0;
            }
        } else {
            if (Integer.parseInt(s.substring(0,2)) <= 26) {
                dp[1]  = 2;
            } else {
                dp[1]  = 1;   
            }
        }
        
        for (int i = 2; i < len; i++) {
            if (s.charAt(i) == '0') {
                if (s.charAt(i - 1) == '0' || Integer.parseInt(s.substring(i - 1, i + 1)) > 26) {
                    return 0;
                }
                dp[i] = dp[i - 2];
            } else {
                if (s.charAt(i - 1) == '0') {
                    dp[i] = dp[i - 1];
                } else {
                    if (Integer.parseInt(s.substring(i - 1, i + 1)) <= 26) {
                        dp[i] = dp[i - 1] + dp[i - 2];
                    } else {
                        dp[i] = dp[i - 1];
                    }
                }
            }
        }
        
        return dp[len - 1];
    }
}
