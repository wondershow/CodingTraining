/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 13, 2017
 */
package algorithm;
/**
 * See problem statement at 
 * https://leetcode.com/problems/number-of-islands-ii/
 * The key things in this problem:
 * 1. the 2d mapping from (i, j) to uf[x] needs to taken care of
 *    depends of uf.size is m*n or m*n + 1;
 * 
 * 
 * */
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class NumberOfIslands2_LC305 {

	public static void main(String[] args) {

	}
	
	int[] uf;
    int islands = 0, m, n;
    int[][] dirs = new int[][] {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
    
    public List<Integer> numIslands2(int m, int n, int[][] positions) {
        List<Integer> res = new ArrayList();
        this.m = m;
        this.n = n;
        uf = new int[m * n + 1];
        Arrays.fill(uf, -1);
        
        for (int[] pos : positions) {
            addLand(pos[0], pos[1]);
            res.add(islands);
        }
        
        return res;
    }
    
    private int root(int i) {
        if (uf[i] == 0) return i;
        uf[i] = root(uf[i]);
        return uf[i];
    }
    
    private void union(int i, int j) {
        int r1 = root(i);
        int r2 = root(j);
        if (r1 != r2) {
            uf[r1] = r2;
            islands--;
        }
    }

    private void addLand(int x, int y) {
        if (uf[remap(x, y)] == -1) {
            uf[remap(x, y)] = 0;
            islands++;
            for (int[] dir : dirs) {
                int i = x + dir[0];
                int j = y + dir[1];
                if (i >= 0 && i < m && j >= 0 && j < n && uf[remap(i, j)] != -1) {
                    union(remap(x, y), remap(i, j));
                }
            }
        }
    }
    
    private int remap(int x, int y) {
        return x * n + y + 1;
    }

}
