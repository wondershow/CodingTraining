/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 25, 2017
 */
package algorithm;

import java.util.Stack;

/**
 * https://leetcode.com/problems/longest-absolute-file-path/
 * Mistakes made:
 * 1. the escape characters '\t' '\n' take only 1 space in the 
 *    input string, not two
 * 2. escape characters !!
 ****/
public class LongestFilePath_LC388 {

	public static void main(String[] args) {

	}

	public int lengthLongestPath(String input) {
        if (input == null || input.length() == 0) {
            return 0;
        }
        
        String[] tmp = input.split('\n' + "");
        System.out.println(tmp.length);
        Stack<String> path = new Stack();
        int res = 0, curLen = 0;
        for (String str : tmp) {
            int i = 0;
            int depth = 0;
            while (str.charAt(i) == '\n') {
                i++;
            }
            while (i < str.length() - 1 && str.charAt(i) == '\t') {
                depth++;
                i++;
            }
            
            while (path.size() > depth) {
                curLen -= path.pop().length();
            }
            
            String item = str.substring(i);
            if (isFile(item)) { // its a file
                res = Math.max(res, depth + item.length() + curLen); 
            } else {
                path.push(item);
                curLen += item.length();
            }
        }
        
        return res;
    }
    
    private boolean isFile(String fileName) {
        for (char ch : fileName.toCharArray()) {
            if (ch == '.') return true;
        }
        return false;
    }
}
