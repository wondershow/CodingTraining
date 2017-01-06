/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 6, 2017
 */
package algorithm;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Set;


/**
 * See problem statement at 
 * https://leetcode.com/problems/word-ladder-ii/
 * 
 * This is a tricky and hard problem. 
 * 1. bfs to find the shortest distance from start to end
 * 2. from the end word, do a dfs towards start.
 * **/
public class WordLadder2_LC126 {

	public static void main(String[] args) {

	}
	
	public List<List<String>> findLadders(String beginWord, String endWord, Set<String> wordList) {
	    List<List<String>> res = new ArrayList<List<String>>();
	    
	    if (wordList == null || wordList.size() == 0 || beginWord == null || endWord == null) {
	        return res;
	    }
	    
	    Map<String, Integer> distMap = bfsDistance(beginWord, endWord, wordList);
	    
	    List<String> path = new LinkedList();
	    path.add(endWord);
	    dfs(endWord, beginWord, path, res, distMap);
	    
	    return res;
	    }


	    private void dfs(String word, String start, List<String> path, List<List<String>> res, Map<String, Integer> distMap) {
	        if (word.equals(start)) {
	            List tmp = new LinkedList(path);
	            Collections.reverse(tmp);
	            res.add(tmp);
	            return;
	        }
	        char[] chars = word.toCharArray();
	        int distance = distMap.get(word);
	        for (int i = 0; i < chars.length; i++) {
	            char ch = chars[i];
	            for (char c = 'a'; c <= 'z'; c++) {
	                if (c == ch) continue;
	                chars[i] = c;
	                String neibor = new String(chars);
	                if (distMap.containsKey(neibor) && distMap.get(neibor) == distance - 1) {
	                    path.add(neibor);
	                    dfs(neibor, start, path, res, distMap);
	                    path.remove(path.size() - 1);
	                }
	            }
	            chars[i] = ch;
	        }
	    }
	    
	    
	    private Map<String, Integer> bfsDistance(String beginWord, String endWord, Set<String> wordList) {
	        Map<String, Integer> res = new HashMap();
	        Queue<String> que = new LinkedList();
	    
	        que.offer(beginWord);
	        res.put(beginWord, 0);
	    
	        while (!que.isEmpty()) {
	            String word = que.poll();
	            if (word.equals(endWord)) {
	                break;
	            }
	            
	            int dist = res.get(word);
	            
	            char[] chars = word.toCharArray();
	            for (int i = 0; i < chars.length; i++) {
	                char ch = chars[i];
	                for (char c = 'a'; c <= 'z'; c++) {
	                    if (ch == c) continue;
	                    chars[i] = c;
	                    String neibor = new String(chars);
	                    if ((wordList.contains(neibor) ||  neibor.equals(endWord)) && !res.containsKey(neibor)) {
	                        res.put(neibor, dist + 1);
	                        que.offer(neibor);
	                    }
	                }
	                chars[i] = ch;
	            }
	        }
	    
	        return res;
	    }
}
