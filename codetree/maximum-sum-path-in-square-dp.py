# dp를 이용

# 오른쪽 / 밑 으로만 이동을 할 수 있다. (n, n )으로 간다.

n = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

dp = [[0]*n for _ in range(n)]

dys = [0, 1]
dxs = [1, 0]

def initialize():
    dp[0][0] = grid[0][0]

    # 1열의 행을 채우기
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    
    # 1행의 열 채우기
    for i in range(1, n):
        dp[0][i] = dp[0][i-1] + grid[0][i]


initialize()

# 양 방향의 값을 비교해서 넣기
for y in range(1, n):
    for x in range(1, n):
        dp[y][x] = max(dp[y][x-1], dp[y-1][x]) + grid[y][x]

print(dp[n-1][n-1])











