n = int(input())
arr = list(map(int, input().split()))

dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i): # 현재 기준 i-1까지 확인
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))