/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 19, 2017
 */
package algorithm;

/**
 * https://leetcode.com/problems/valid-parentheses/
 * 
 * The key thing is to put the right pair of the 
 * parenthesis into the stack, it saves a lot trouble
 * **/
import java.util.Stack;

public class ValidParenthesis_LC20 {

	public static void main(String[] args) {

	}
	
	public boolean isValid(String s) {
        if (s == null || s.length() == 0) {
            return true;
        }
        Stack<Character> stack = new Stack();
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (ch == '(') {
                stack.push(')');
            } else if (ch == '[') {
                stack.push(']');
            } else if (ch == '{') {
                stack.push('}');
            } else {
                if (stack.isEmpty() || stack.pop() != ch) {
                    return false;
                }
            }
        }
        
        return stack.size() == 0;
    }
}
