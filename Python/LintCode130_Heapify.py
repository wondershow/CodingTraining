class Solution:
    """
    @param a: Given an integer array
    @return: nothing
    """
    def heapify(self, a: List[int]):
        # write your code here
        def sift_down(i):
            N = len(a)
            while i < N:
                l_child = 2 * i + 1
                r_child = 2 * i + 2
                min_index = i
                if l_child < N and a[l_child] < a[min_index]:
                    min_index = l_child
                if r_child < N and a[r_child] < a[min_index]:
                    min_index = r_child
                if min_index == i:
                    break
                a[i], a[min_index] = a[min_index], a[i]
                i = min_index
        N = len(a)

        for i in range(N // 2, -1, -1):
            sift_down(i)
        

