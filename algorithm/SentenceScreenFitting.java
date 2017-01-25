/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 25, 2017
 */
package algorithm;

/**
 * https://leetcode.com/problems/sentence-screen-fitting/
 * 
 * Very tough problem!
 * 
 * **/

public class SentenceScreenFitting {

	public static void main(String[] args) {

	}
	
	/**
	 *
	 * Try to fit one line with the whole sentences!
	 * Needs to be revisited later
	 * **/
	public int wordsTyping(String[] sentence, int rows, int cols) {
        String line = String.join(" ", sentence) + " ";
        int totalChars = 0, len = line.length();
        for (int i = 0; i < rows; i++) {
            totalChars += cols;
            if (line.charAt(totalChars % len) == ' ') {
                totalChars++;
            } else {
                while (totalChars > 0 && line.charAt((totalChars - 1) % len) != ' ') {
                    totalChars--;
                }
            }
        }
        
        //System.out.println(totalChars);
        return totalChars / len;      
    }

}
