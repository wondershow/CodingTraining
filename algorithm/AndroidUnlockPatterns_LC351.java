/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 18, 2017
 */
package algorithm;
/**
 * 
 * https://leetcode.com/problems/android-unlock-patterns/
 * The key is to build that skip array. 
 * 
 * **/
import java.util.BitSet;

public class AndroidUnlockPatterns_LC351 {

	public static void main(String[] args) {

	}
	
	public int numberOfPatterns(int m, int n) {
        if (m > n || m < 1 || n > 9) {
            return 0;
        }
        
        int[][] skip = new int[10][10];
        skip[1][3] = skip[3][1] = 2;
        skip[1][7] = skip[7][1] = 4;
        skip[3][9] = skip[9][3] = 6;
        skip[7][9] = skip[9][7] = 8;
        skip[1][9] = skip[9][1] = skip[3][7] = skip[7][3] = skip[4][6] = skip[6][4] = skip[2][8] = skip[8][2] = 5;
        
        BitSet used = new BitSet(10);
        int[] res = new int[1];
        for (int i = 1; i <= 9; i++) {
            used.set(i);
            helper(i, used, res, 1, m, n, skip);
            used.clear(i);
        }
        return res[0];
    }
    
    
    private void helper(int number, BitSet used, int[] res, int len, int m, int n, int[][] skip) {
        if (len >= m) {
            res[0]++;
            if (len == n) {
                return;
            }
        }
        for (int i = 1; i <= 9; i++) {
            if (used.get(i)) {
                continue;
            }
            if (skip[number][i] == 0 || skip[number][i] != 0 && used.get(skip[number][i])) {
                used.set(i);
                helper(i, used, res, len + 1, m, n, skip);
                used.clear(i);
            }
        }
    }
}
