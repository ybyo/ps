# 2805

## Constraints

- 농장의 크기는 홀수다.
- 수확은 항상 정사각형의 마름모로 형태로 가능하다.
- 농장크기 N은 1 이상 49 이하의 홀수다.
- 농작물의 가치는 0~5 이다

## Idea

- Simulation
- 마름모 만들기, 세로 중심축으로 내려가면서 좌우 범위 확장 -> 중간 지점 지나면 감소

## Pseudo code

1. 값 받아 grid 생성
2. N // 2 -> 중간지점
3. r, c iteration: k = -1으로 시작
4. c가 N // 2 일때마다 가운데 좌표의 c-k:c+k 범위 값을 더해줌. k 증가
5. r이 N // 2를 지나면, k 1씩 감소

## Mistakes

- K 의 감소지점 판단 실수

```python
k = 0
for r in range(N):
    for c in range(N):
        if c == M:
            ans += sum(grid[r][c - k:c + k + 1])
    if r < M:  # 실수
        k += 1
    else:
        k -= 1
```