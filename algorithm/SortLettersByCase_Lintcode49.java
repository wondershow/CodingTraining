/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Feb 14, 2017
 */
package algorithm;

public class SortLettersByCase_Lintcode49 {
	public void sortLetters(char[] chars) {
        //write your code here
        
        if (chars == null || chars.length <= 1) return;
        
        int i = 0, j = chars.length - 1;
        while (i < j) {
            while (i < j && Character.isLowerCase(chars[i])) i++;
            while (i < j && Character.isUpperCase(chars[j])) j--;
            if (i < j) {
                swap(chars, i, j);
            }
        }
    }
    
    private void swap(char[] chars, int i, int j) {
        char ch = chars[i];
        chars[i] = chars[j];
        chars[j] = ch;
    }
}
