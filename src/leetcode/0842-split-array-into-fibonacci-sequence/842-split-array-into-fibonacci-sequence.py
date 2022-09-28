class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        def dfs(num, lt):
            if lt == len(num) and len(ans) >= 3:
                return True
            for rt in range(lt + 1, len(num) + 1):
                curr_val = int(num[lt:rt])
                curr_digit = rt - lt
                if curr_digit > 1 and num[lt:rt][0] == '0' or curr_val > 2**31 - 1:
                    return False
                elif len(ans) >= 2 and curr_val > ans[-2] + ans[-1]:
                    return False
                elif len(ans) <= 1 or ans[-2] + ans[-1] == curr_val:
                    ans.append(curr_val)
                    if dfs(num, lt + curr_digit):
                        return True
                    else:
                        ans.pop()
            return False

        ans = []
        dfs(num, 0)

        return ans
