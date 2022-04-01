
# n번 피보나치 수를 구하기 위해서 풀어야 할 문제들 => 0 ~ N 까지
def fibo(n):
    if n < 2:
        return n
    if memo[n] != -1:
        return memo[n]
    memo[n] = fibo(n - 1) + fibo(n - 2)
    return memo[n]

def fibo_iter(n):
    dp = [0] * (N + 1)
    dp[0], dp[1] = 0, 1

    for i in range(2, n + 1): # i=> 문제 크기를 나타내는 값
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

N = 7
memo = [-1] * (N + 1) # 초기값은 아직 그 문제의 답을 구하지 못했다. 0부터 N까지의 크기를 구해야 하므로 N + 1
print(fibo(N))


n = int(input())

def fibo(n):
    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

print(fibo(n))