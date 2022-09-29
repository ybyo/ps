import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    C = []
    cipher = []
    d = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7,
         '0110111': 8, '0001011': 9}

    for _ in range(N):
        s = str(input())
        C.append(s[::-1])

    for s in C:
        if len(set(s)) == 1:
            continue
        seg = ''
        for idx, c in enumerate((list(s))):
            if c == '1':
                seg = s[idx:idx + 56]
                break
            else:
                continue
        seg = seg[::-1]
        cipher = [seg[i:i + 7] for i in range(0, len(seg), 7)]
        break

    odd = even = 0
    for idx, c in enumerate(cipher):
        if idx % 2 == 0:
            odd += d[c]
        else:
            even += d[c]

    ans = 0
    if (odd * 3 + even) % 10 == 0:
        ans = odd + even

    print(f"#{test_case} {ans}")
