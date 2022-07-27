class Solution:
    def maximum69Number(self, num: int) - > int:
        for i, n in enumerate(str(num)):
            if n == '6':
                return num + 3 * 10 ** (len(str(num))-i-1)
        return num


class Solution:
    def maximum69Number (self, num: int) -> int:
        str_num = str(num)
        if '6' in str_num:
            idx = str_num.index('6')
            return int(str_num[:idx] + '9' + str_num[idx+1:])
        return num
