class Solution:
    def maximum69Number (self, num: int) -> int:
        st = str(num)
        if '6' in st:
            idx = st.index('6')
            return int(st[:idx]+'9'+st[idx+1:])
        return num
