/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Jan 15, 2017
 */
package algorithm;

/**
 * See problem statement at
 * https://leetcode.com/problems/evaluate-division/
 * The key steps is to develop a graph representaion
 * data structure used here is string->map<String, double>
 * very straighforward
 * **/

import java.util.Deque;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Map;
import java.util.Set;

public class EvaluationDivision_LC399 {

	public static void main(String[] args) {
	}
	
	public double[] calcEquation(String[][] equations, double[] values, String[][] queries) {
        if (equations == null) {
            return null;
        }
        
        if (equations.length == 0) {
            return new double[0];
        }
        
        Map<String, Map<String, Double>> neibors = new HashMap();
        
        for (int i = 0; i < equations.length; i++) {
            String from = equations[i][0];
            String to = equations[i][1];
            addEdge(from, to, values[i], neibors);
            addEdge(to, from, 1 / values[i], neibors);
        }
        
        double[] res = new double[queries.length];
        for (int i = 0; i < queries.length; i++) {
            res[i] = countEdgeWeghit(queries[i][0], queries[i][1], neibors);
        }
        
        return res;
    }
    
    private double countEdgeWeghit(String from, String to, Map<String, Map<String, Double>> neibors) {
        if (!neibors.containsKey(from) || !neibors.containsKey(to)) {
            return -1.0d;
        }
        
        Deque<String> que = new LinkedList();
        Deque<Double> valQue = new LinkedList();
        que.offer(from);
        valQue.offer(1.0d);
        Set<String> seen = new HashSet();
        seen.add(from);
        
        while (que.size() > 0) {
            String next = que.poll();
            double val = valQue.poll();
            if (next.equals(to)) {
                return val;
            }
            Map<String, Double> edges = neibors.get(next);
            for (String neibor : edges.keySet()) {
                if (!seen.contains(neibor)) {
                    seen.add(neibor);
                    que.offer(neibor);
                    valQue.offer(val * edges.get(neibor));
                }
            }
        }
        
        return -1.0d;
    }
    
    private void addEdge(String from, String to, double val, Map<String, Map<String, Double>> neibors) {
        if (!neibors.containsKey(from)) {
            neibors.put(from, new HashMap());
        }
        Map<String, Double> pointsTo = neibors.get(from);
        pointsTo.put(to, val);
    }

}
