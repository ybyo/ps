class Solution:
    def checkRecord(self, s: str) -> bool:
        """
        Return: bool
        Condition:
          * 'A' fewer than 2
          * 'L' no 3 consecutive days
        Category:
          * String
        """
        
        cnt = 0
        if s.count('A') >= 2:
            return False
        if len(s) <= 1:
            return True
        
        if s.count('L') >= 3:
            prev = -100
            for idx, c in enumerate(s):
                if c == 'L':
                    if prev == -100:
                        cnt += 1
                    elif idx - prev == 1:
                        cnt += 1
                    else:
                        cnt = 1
                    prev = idx
                    if cnt == 3:
                        return False
        else:
            return True
        
        return cnt < 3
            