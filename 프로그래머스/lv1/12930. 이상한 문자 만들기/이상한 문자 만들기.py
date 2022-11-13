def solution(s):
    ans = ""
    cnt = -1

    for i in range(len(s)):
        if s[i] == " ":
            cnt = -1
            ans += s[i]
        else:
            cnt += 1
            if cnt & 1 == 0:
                ans += s[i].upper()
            else:
                ans += s[i].lower()

    return ans
