# 서 : N <-> 동 :M
# 1 : 1 연결 시 가장 많이 지을 수 있는 경우의 수(겹치면 안됨)
# 서로 다른 조합을 선택한다 => 다이나믹 프로그래링

for i in range(int(input())):
    N, M = map(int, input().split())
    # 경우의 수를 구할 list를 만든다
    dp = [[0 for _ in range(M + 1)] for __ in range(N + 1)]
    # 서쪽 i번째 다리가 연결될 수 있는 경우의 수
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            # 첫 번째 i는 어디든 연결 할 수있음
            if i == 1:
                dp[i][j] = j
            # 같은 경우 해당 i가 연결될 수 있는것 부터 시작 
            elif i == j:
                dp[i][j] = 1
            else:
                # 작은건 그 전에 연결됨 제외
                # 크다면 연결 된 전에 연결 될수있는 경우 + 전 i가 연결에서 연결 안됐을 경우의수를 다 가질 수 있음
                if j > i:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
    print(dp[i][j])
