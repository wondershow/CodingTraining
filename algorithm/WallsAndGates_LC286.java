/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 13, 2017
 */
package algorithm;

import java.util.Deque;
import java.util.LinkedList;

/***
 * See problem statement at:
 * https://leetcode.com/problems/walls-and-gates/
 * 
 * The key is to do BFS with all "0" points
 * 
 **/
public class WallsAndGates_LC286 {

	public static void main(String[] args) {

	}
	
	int[][] directions = new int[][] {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    public void wallsAndGates(int[][] rooms) {
        if (rooms == null || rooms.length == 0 || rooms[0].length == 0) {
            return;
        }
        
        Deque<Integer> que = new LinkedList();
        
        for (int i = 0; i < rooms.length; i++) {
            for (int j = 0; j < rooms[0].length; j++) {
                if (rooms[i][j] == 0) {
                    que.offer(i * rooms[0].length + j);
                }
            }
        }
        
        int dist = 0;
        while (que.size() > 0) {
            int len = que.size();
            dist++;
            for (int k = 0; k < len; k++) {
                int tmp = que.poll();
                int x = tmp / rooms[0].length;
                int y = tmp % rooms[0].length;
                for (int[] dir : directions) {
                    int i = dir[0] + x;
                    int j = dir[1] + y;
                    int number = i * rooms[0].length + j; 
                    if (i >= 0 && i < rooms.length && j >= 0 && j < rooms[0].length 
                        && dist < rooms[i][j]) {
                        rooms[i][j] = dist;
                        que.offer(number);
                    }
                }
            }
        }
    }
	
}
