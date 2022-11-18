# problem source: https://school.programmers.co.kr/learn/courses/30/lessons/120885

def solution(bin1, bin2):
    ans = ""
    n = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(n)
    bin2 = bin2.zfill(n)

    carry = 0
    for i in range(n - 1, -1, -1):
        tmp = ord(list(bin1)[i]) + ord(list(bin2)[i]) - ord('0') * 2
        tmp += carry
        carry = 0
        if tmp >= 2:
            carry += 1
            tmp -= 2
        ans += str(tmp)

    return (ans + str(carry))[::-1] if carry == 1 else ans[::-1]
