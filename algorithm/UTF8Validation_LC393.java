/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 12, 2017
 */
package algorithm;

public class UTF8Validation_LC393 {

	public static void main(String[] args) {

	}
	
	public boolean validUtf8(int[] data) {
        if (data == null || data.length == 0) {
            return false;
        }
        
        int tailings = 0;
        for (int i = 0; i < data.length; i++) {
            if (tailings == 0) {
                if (firstDigits(data[i], 1) != 0) {
                    if (firstDigits(data[i], 5) == 30) {
                        tailings = 3;
                    } else if (firstDigits(data[i], 4) == 14) {
                        tailings = 2;
                    } else if (firstDigits(data[i], 3) == 6) {
                        tailings = 1;
                    } else {
                        return false;
                    }
                }
            } else {
                if (firstDigits(data[i], 2) != 2) {
                    return false;
                }
                tailings--;
            }
        }
        
        return tailings == 0;    
    }
    
    /**
        get the most significant n digits and return as an int numbers
    **/
    private int firstDigits(int a, int n) {
        return a >>> (8 - n);
    }
}
