class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        for i in range(0, len(flowerbed), 2):
            if flowerbed[i] == 0:
                left = (i == 0) or (flowerbed[i - 1] == 0)
                right = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                if left and right:
                    flowerbed[i] = 1
                    cnt += 1
                    if cnt >= n:
                        return True
        return cnt >= n


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        s = len(flowerbed)
        ans = 0
        bed = [0] + flowerbed + [0]
        for i in range(1, s + 1):
            if bed[i] == bed[i - 1] == bed[i + 1] == 0:
                bed[i] = 1
                ans += 1
            if ans == n:
                return True
        return False
