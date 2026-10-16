class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True
        count = 1                      # virtual empty plot on the left
        for plot in flowerbed:
            if plot == 0:
                count += 1
            else:
                count = 0
            if count == 3:
                n -= 1
                if n == 0:             # early exit
                    return True
                count = 1
        count += 1                     # virtual empty plot on the right
        if count == 3:
            n -= 1
        return n <= 0