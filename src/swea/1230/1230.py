import sys

sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    cipher = list(map(str, input().split()))
    K = int(input())
    key = list(map(str, input().split()))

    k = 0
    while k < len(key):
        if key[k] == 'I':
            correction = 0
            idx = int(key[k + 1])
            cnt = int(key[k + 2])
            for i in range(k + 3, k + 3 + cnt):
                cipher.insert(idx + correction, key[i])
                correction += 1
                k = i
        elif key[k] == 'D':
            idx = int(key[k + 1])
            cnt = int(key[k + 2])
            for i in range(cnt):
                del cipher[idx]
        elif key[k] == 'A':
            cnt = int(key[k + 1])
            for i in range(k + 2, k + 2 + cnt):
                cipher.append(key[i])
                k = i
        k += 1

    print(f"#{test_case} {' '.join(cipher[:10])}")
