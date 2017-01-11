/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 11, 2017
 */
package algorithm;
/**
 * See problem statement at 
 * https://leetcode.com/problems/word-squares/
 * A classical example of using Trie to reduce
 * search space and save time.
 * **/
import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;
import java.util.List;

public class WordSquares_LC425 {

	public static void main(String[] args) {

	}
	
	class TrieNode {
        boolean isWord;
        String word;
        TrieNode[] kids = new TrieNode[26];
    }
    
    TrieNode trieRoot = new TrieNode();
    public List<List<String>> wordSquares(String[] words) {
        List<List<String>> res = new ArrayList<List<String>>();
        if (words == null || words.length == 0) {
            return res;
        }
        for (String word : words) {
            buildTrie(word);
        }
        
        int size = words[0].length();
        
        List<String> path = new ArrayList<String>();
        for (String word : words) {
            path.add(word);
            helper(path, res, size);
            path.remove(word);
        }
        
        return res;
    }
    
    private void helper(List<String> path, List<List<String>> res, int size) {
        if (path.size() == size) {
            res.add(new ArrayList(path));
            return;
        }
        TrieNode p = trieRoot;
        int col = path.size();
        for (int i = 0; i < path.size(); i++) {
            char ch = path.get(i).charAt(col);
            if (p.kids[ch - 'a'] == null) {
                return;
            }
            p = p.kids[ch - 'a'];
        }
        
        Deque<TrieNode> que = new LinkedList();
        que.offer(p);
        while (que.size() > 0) {
            TrieNode q = que.poll();
            if (q.isWord) {
                path.add(q.word);
                helper(path, res, size);
                path.remove(path.size() - 1);
            } else {
                for (int i = 0; i < 26; i++) {
                    if (q.kids[i] != null) {
                        que.offer(q.kids[i]);
                    }
                }
            }
        }
    }
    
    
    private void buildTrie(String word) {
        TrieNode p = trieRoot;
        for (int i = 0; i < word.length(); i++) {
            char ch = word.charAt(i);
            if (p.kids[ch - 'a'] == null) {
                p.kids[ch - 'a'] = new TrieNode();
            }
            p = p.kids[ch - 'a'];
        }
        p.isWord = true;
        p.word = word;
    }
}
