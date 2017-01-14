/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 14, 2017
 */
package algorithm;
/**
 * See problem statement at:
 * https://leetcode.com/problems/trapping-rain-water-ii/
 * 
 * **/
public class TrappingRainWater2_LC407 {

	public static void main(String[] args) {

	}
	
	class Cell {
        int x, y, h;
        Cell (int x, int y, int h) {
            this.x = x;
            this.y = y;
            this.h = h;
        }
    }
    
    int[][] directions = new int[][] {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    
    /***
     * Solution 1:
     * According to the Bucket argument, for a cell, 
     * the final water it holds is decided by the shortest
     * cell in four corners of it. So we start from the outmost
     * rectangle, add all cells into to a priority queue, each time
     * we poll a shortest cell from the heap, visit its neighbors,
     * when the neighbor is shorter than the current cell, that means
     * the neighbor can hold water up to the height of the current cell.
     * then we need to add the neighbor to the heap, NOTE that its not
     * the actual height of the neighbor cell should be added, instead
     * it is the neighbor's "final height", the larger of water height 
     * and neighbor cell height. 
     * **/
    public int trapRainWater(int[][] heightMap) {
        if (heightMap == null || heightMap.length <= 2 || heightMap[0].length <= 2) {
            return 0;
        }
        
        BitSet visited = new BitSet();
        PriorityQueue<Cell> heap = new PriorityQueue(new Comparator<Cell>() {
            public int compare(Cell a, Cell b) {
                return a.h - b.h;
            }
        });
        
        int m = heightMap.length, n = heightMap[0].length;
        for (int i = 0; i < m; i++) {
            heap.offer(new Cell(i, 0, heightMap[i][0]));
            heap.offer(new Cell(i, n - 1, heightMap[i][n - 1]));
            visited.set(i * n);
            visited.set(i * n + n - 1);
        }
        
        for (int j = 1; j < n - 1; j++) {
            heap.offer(new Cell(0, j, heightMap[0][j]));
            heap.offer(new Cell(m - 1, j, heightMap[m - 1][j]));
            visited.set(j);
            visited.set((m - 1) * n + j);
        }
        
        int res = 0;
        while (heap.size() > 0) {
            Cell c = heap.poll();
            for (int[] dir : directions) {
                int i = c.x + dir[0];
                int j = c.y + dir[1];
                if (i >= 0 && j >= 0 && i < m && j < n && !visited.get(i * n + j)) {
                    visited.set(i * n + j);
                    res += Math.max(0, c.h - heightMap[i][j]);
                    heap.offer(new Cell(i, j, Math.max(heightMap[i][j], c.h)));
                }
            }
        }
        
        return res;
    }
}
