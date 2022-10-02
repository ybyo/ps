# 2806

## Constraints

- 1 <= N <= 10

## Idea

- Simulation
- Recursion(불가능 조건(대각선, 가로, 세로)을 확인해 기존에 놓은 자리에 없다면 두고 진입)

## Pseudo code

1. c iteration: r은 N - n과 동일. check과정(놓으려는 위치의 대각선 상에 기존 좌표가 들어있는 지 확인, boolean을 통해 세로 좌표 확인)
2. check 과정을 통과하면, n을 줄이고 recursion 진입
3. n이 0이되면 해당 접근이 맞는 것(ans += 1), 아니면 그냥 return

## Mistakes
