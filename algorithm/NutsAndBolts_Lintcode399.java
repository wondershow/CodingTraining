/**
 * Author: Lei Zhang
 * raymond.zhang.us@gmail.com
 * Feb 14, 2017
 */
package algorithm;

/**
 * http://www.lintcode.com/en/problem/nuts-bolts-problem/
 * 
 * Very tricky problem!
 * 
 * **/
public class NutsAndBolts_Lintcode399 {
	NBComparator compartor;
    public void sortNutsAndBolts(String[] nuts, String[] bolts, NBComparator compare) {
        // write your code here
        compartor = compare;
        qsort(nuts, bolts, 0, nuts.length - 1);
    }
    
    private void qsort(String[] nuts, String[] bolts, int lo, int hi) {
        if (lo >= hi) return;
        int mid = partition(nuts, lo, hi, bolts[lo]);
        
        partition(bolts, lo, hi, nuts[mid]);
        
        qsort(nuts, bolts, lo, mid - 1);
        qsort(nuts, bolts, mid + 1, hi);
    }
    
    
    private int partition(String[] items, int lo, int hi, String pivot) {
        if (lo == hi) return lo;
        
        int pos = lo;
        
        for (; pos <= hi; pos++) {
            if (cmp(items[pos], pivot) == 0 || cmp(pivot, items[pos]) == 0) {
                break;
            }
        }
        
        swap(items, lo, pos);
        
        int i = lo + 1, j = hi;
        while (i < j) {
            while (i < j && (cmp(items[i], pivot) == 1 || cmp(pivot, items[i]) == -1)) i++;
            while (i < j && (cmp(items[j], pivot) == -1 || cmp(pivot, items[j]) == 1)) j--;
            if (i < j) {
                swap(items, i, j);
            }
        }
        if (cmp(items[i], pivot) == -1 || cmp(pivot, items[i]) == 1) i--;
        swap(items, lo, i);
        return i;
    }
    
    private int cmp(String item1, String item2) {
        return compartor.cmp(item1, item2);
    }
    
    
    private void swap(String[] items, int i, int j) {
        String tmp = items[i];
        items[i] = items[j];
        items[j] = tmp;
    }
}
