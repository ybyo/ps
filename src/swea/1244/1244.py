import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(str, input().split())
    K = int(K)
    n = list(N)

    max_val = sorted(list(map(str, n)), reverse=True)
    mdx = 0
    last = -1
    H = 0

    while K and mdx < len(max_val):
        if max_val[mdx] == n[mdx]:
            mdx += 1
        else:
            cdx = len(n) - 1
            while cdx >= 0:
                if max_val[mdx] == n[cdx]:
                    n[cdx], n[mdx] = n[mdx], n[cdx]
                    if last == max_val[mdx]:
                        H += 1
                    last = max_val[mdx]
                    mdx += 1
                    K -= 1
                    break
                else:
                    cdx -= 1
    while K:
        if len(set(n)) == len(n):
            n[-1], n[-2] = n[-2], n[-1]
            K -= 1
        else:
            K = 0

    for i in range(len(n) - 1, 0, -1):
        if H == 0:
            break
        if n[i] > n[i - 1]:
            n[i - 1], n[i] = n[i], n[i - 1]
            H -= 1

    print(f"#{test_case} {''.join(n)}")
