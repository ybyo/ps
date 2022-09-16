"""
Return: Largest Rectangle
Category Assumption: Array, DP?
Real Category: Array, Stack, Monotonic Stack
​
Pseudo Code:
* Memo:
[2]: 2
[2, 1]: 2
[2, 1, 5]: 5
[2, 1, 5, 6]: 10
[2, 1, 5, 6, 2]: 10
​
* Variable:
lowest, highest
comparison: lowest * len(heights), highest(spread)
​
* 가장 큰 값을 기준으로 퍼져나가기?
* 발생할 수 있는 문제는 무엇일까?
* 좌우 선택 문제
* 항상 가장 큰 값을 기준으로 할 때, 최적의 답이 찾아지는가?
* 예시) [2, 1, 5, 5, 5, 5, 5, 1, 1, 1, 10, 9, 2, 3] 경우 늦게 찾아짐
* 위 예시에서 10 이후에 [5, 5, 5, 5]를 바로 찾는 방법은 무엇일까?
​
* Monotonic Stack:
* Example case 1: