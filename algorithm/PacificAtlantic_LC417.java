/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 15, 2017
 */
package algorithm;
/**
 * See problem statement at
 * https://leetcode.com/problems/pacific-atlantic-water-flow/
 * errors made:
 * when pacific is computed,
 * the check should be done when polling the atlantic que,
 * can not do the check when offering atlantic que,
 * that may miss the points which are offered during the
 * atlantic initialization phase.
 * **/
import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;
import java.util.List;

public class PacificAtlantic_LC417 {

	public static void main(String[] args) {

	}
	
	int[][] directions = new int[][]{{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
    boolean[][] pacific;
    boolean[][] atlantic;
    public List<int[]> pacificAtlantic(int[][] matrix) {
        List<int[]> res = new ArrayList<int[]>();
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return res;
        }
        
        int m = matrix.length, n = matrix[0].length;
        Deque<int[]> que = new LinkedList();
        atlantic = new boolean[m][n];
        pacific = new boolean[m][n];
        
        for (int i = 0; i < n; i++) {
            que.offer(new int[] {0, i});
            atlantic[0][i] = true;
        }
        
        for (int i = 1; i < m; i++) {
            que.offer(new int[] {i, 0});
            atlantic[i][0] = true;
        }
        
        while (que.size() > 0) {
            int[] tmp = que.poll();
            for (int[] dir : directions) {
                int i = tmp[0] + dir[0];
                int j = tmp[1] + dir[1];
                if (i >= 0 && i < m && j >= 0 && j < n && matrix[tmp[0]][tmp[1]] <= matrix[i][j] && !atlantic[i][j]) {
                    que.offer(new int[] {i, j});
                    atlantic[i][j] = true;
                }
            }
        }
        
        //System.out.println(atlantic[0][4]);
        
        que = new LinkedList();
        
        for (int i = 0; i < n; i++) {
            que.offer(new int[] {m - 1, i});
            pacific[m - 1][i] = true;
        }
        
        for (int i = 0; i < m - 1; i++) {
            que.offer(new int[] {i,  n - 1});
            pacific[i][n - 1] = true;
        }
        
        
        while (que.size() > 0) {
            int[] tmp = que.poll();
            if (atlantic[tmp[0]][tmp[1]]) {
                res.add(new int[] {tmp[0], tmp[1]});
            };
            for (int[] dir : directions) {
                int i = tmp[0] + dir[0];
                int j = tmp[1] + dir[1];
                if (i >= 0 && i < m && j >= 0 && j < n && matrix[tmp[0]][tmp[1]] <= matrix[i][j] && !pacific[i][j]) {
                    que.offer(new int[] {i, j});
                    pacific[i][j] = true;
                }
            }
        }
        
        return res;
    }
}
