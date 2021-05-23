class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowers, N = 0, len(flowerbed)
        for i, v in enumerate(flowerbed):
            if v != 0:
                continue
            if i > 0 and flowerbed[i - 1] == 1:
                continue
            if i < N - 1 and flowerbed[i + 1] == 1:
                continue
            flowers += 1
            flowerbed[i] = 1
        return flowers >= n
