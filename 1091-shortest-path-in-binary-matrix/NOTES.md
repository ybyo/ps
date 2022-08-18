* return: total move count(int)
* special condition
1. [0][0] == [n-1][n-1] == 0 or return -1
* category
1. bfs
* variable
ans = 0, 8 direction dir, queue
* algorithm
1. check [0][0], [n-1][n-1] == 0
2. check 8direction, but check first right below conrner
2.1 if okay, move corner, ans +=