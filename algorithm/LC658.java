
public class LC658 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	public List<Integer> findClosestElements(int[] arr, int k, int x) {
        List<Integer> res = new ArrayList();
        int pos = binarySeach(arr, x);
        
        //Start searching from k elements left of pos to k elements right of pos.
        int lo = Math.max(0, pos - k), hi = Math.min(arr.length - 1, pos + k);
        
        //create the first list of k
        for (int i = lo; i < lo + k; i++) {
            res.add(arr[i]);            
        }
        
        /* start scanning from (lo + k) element, try to add that element while
        // poping out the 1st elemnt in the list, see adding and removing which one
        // brings more difference (abs value minus x), if adding introduces more or equal 
        // abs error, stop. */
        for (int j = lo + k; j <= hi; j++) {
            if ( Math.abs(arr[j] - x) >= Math.abs(arr[j - k] - x)) {
                break;
            }
            res.remove(0);
            res.add(arr[j]);
        }
        
        return res;
    }
    
    
    /***
        Find a proper insert location in arr to put x.
    */
    private int binarySeach(int[] arr, int x) {
        int lo = 0, hi = arr.length - 1;
        while (lo + 1 < hi) {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] > x) {
                hi = mid;
            } else {
                lo = mid;
            }
        }
        
        if (x > arr[hi]) {
            return hi + 1;
        } else if (x > arr[lo]) {
            return hi;
        } else {
            return lo;
        }
    }
}
