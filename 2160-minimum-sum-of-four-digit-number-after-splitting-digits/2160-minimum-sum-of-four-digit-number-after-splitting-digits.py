class Solution:
    def minimumSum(self, num: int) -> int:
        std_num = sorted(str(num))
        return int(std_num[0] + std_num[2]) + int(std_num[1] + std_num[3])