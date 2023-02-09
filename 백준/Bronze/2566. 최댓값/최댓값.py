nums = [list(map(int, input().split())) for _ in range(9)]

max_num = -1

for i in range(9):
    for j in range(9):
        if nums[i][j] > max_num:
            max_num = nums[i][j]
            m_i = i + 1
            m_j = j + 1

print(max_num)
print(m_i, m_j)