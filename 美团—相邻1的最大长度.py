# 作者：我要一桶浆糊
# 链接：https: // www.nowcoder.com / discuss / 104642
# 来源：牛客网

'''
10 2
1 0 0 1 0 1 0 1 0 1
'''
# 思路：确定填充每相邻K个0得到的总长度
N, K = [int(i) for i in input().strip().split()]
temp_list = [int(i) for i in input().strip().split()]
dp = [0]
for i in range(N):
    if temp_list[i] == 0:
        dp.append(i + 1)
dp.append(N + 1)

# 遍历得到最大长度
max_len = 0
for i in range(K + 1, len(dp)):
    max_len = max(max_len, dp[i] - dp[i - K - 1] - 1)

print(max_len)