import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # P: 가격 배열, S: 수영 계획
    P = list(map(int, input().split()))
    S = list(map(int, input().split()))
    # dp 배열 생성
    dp = [0] * 12

    # 3달권이 1달, 1일 짜리보다 더 저렴하지 않으리라는 제한 조건이 없으므로, 0번 배열부터 최솟값 계산
    dp[0] = min([S[0] * P[0], P[1], P[2]])

    # 우선 1일, 1달, 3달 가격권 비교
    # 현재 달(i)의 최솟값: 직전 달(i - 1)의 최솟값 + 현재달 최선의 가격
    # 다만, i가 3일 때부터 dp[i - 3]의 가격을 더해주어야함(dp는 누적된 최선의 가격이므로)
    for i in range(1, len(dp)):
        if i < 3:
            dp[i] = min([dp[i - 1] + S[i] * P[0], dp[i - 1] + P[1], P[2]])
        else:
            dp[i] = min([dp[i - 1] + S[i] * P[0], dp[i - 1] + P[1], dp[i - 3] + P[2]])

    # 1일, 1달, 3달의 최선 가격 배열 dp와 1년권을 비교
    print(f"#{test_case} {min(dp[-1], P[3])}")
