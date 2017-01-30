/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 30, 2017
 */
package algorithm;
/**
 * https://leetcode.com/problems/encode-and-decode-strings/
 * **/
public class Codec_LC271 {

	public static void main(String[] args) {

	}
	
	// Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder("");
        for (String str : strs) {
            sb.append(str.length() + "#" + str);
        }
        return sb.toString();
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
        List<String> res = new ArrayList<String>();
        for (int i = 0; i < s.length(); ) {
            int j = i;
            while (s.charAt(j) != '#') {
                j++;
            }
            int len = Integer.parseInt(s.substring(i, j));
            res.add(s.substring(j + 1, j + 1 + len));
            i = j + 1 + len;
        }
        return res;
    }

}
