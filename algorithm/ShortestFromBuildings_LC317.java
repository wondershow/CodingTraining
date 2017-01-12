/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 11, 2017
 */
package algorithm;
/**
 * see problem statement at 
 * https://leetcode.com/problems/shortest-distance-from-all-buildings/
 * 
 * 
 * **/
import java.util.Deque;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Set;

public class ShortestFromBuildings_LC317 {

	public static void main(String[] args) {

	}
	
	public int shortestDistance(int[][] grid) {
        if (grid == null || grid.length == 0 || grid[0].length == 0) {
            return -1;
        }
        
        int m = grid.length, n = grid[0].length;
        int[][] distance = new int[m][n];
        int[][] reach = new int[m][n];
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1 || grid[i][j] == 2) {
                    distance[i][j] = Integer.MAX_VALUE;
                }
            }
        }
        
        int totalBuildings = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    totalBuildings++;
                    bfs(i, j, grid, distance, reach);
                }
            }
        }
        
        int res = Integer.MAX_VALUE;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0 && reach[i][j] == totalBuildings) {
                    res = Math.min(res, distance[i][j]);
                }
                //System.out.print(distance[i][j] + " ");
            }
            //System.out.println();
        }
         
        return res == Integer.MAX_VALUE ? -1 : res;
    }
    
    Set<Integer> seen;
    int[][] directions = new int[][] {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    
    private void bfs(int a, int b, int[][] grid, int[][] distance, int[][] reach) {
        int m = grid.length, n = grid[0].length;
        Deque<Integer> que = new LinkedList();
        que.offer(a * n + b);
        int dist = 0;
        seen = new HashSet();
        seen.add(a * n + b);
        while (que.size() > 0) {
            int len = que.size();
            for (int i = 0; i < len; i++) {
                int tmp = que.poll();
                int x = tmp / n, y = tmp % n;
                for (int[] dir : directions) {
                    int r = x + dir[0];
                    int c = y + dir[1];
                    if (r < 0 || r >= m || c < 0 || c >= n) continue;
                    if (grid[r][c] == 0 && !seen.contains(r * n + c)) {
                        seen.add(r * n + c);
                        distance[r][c] += (dist + 1);
                        reach[r][c]++;
                        que.offer(r * n + c);
                    }
                }
            }
            dist++;
        }
    }
}
