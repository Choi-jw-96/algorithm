import sys
input = sys.stdin.readline

def m_sort(a):
    if len(a) == 1:
        return a

    mid = (len(a) + 1) // 2
    
    # a_1이 하나 남을때까지 쪼개줘
    a_1 = m_sort(a[ : mid])
    # a_1을 제외하고 하나 남을때까지 쪼개줘
    a_2 = m_sort(a[mid : ])

    i, j = 0, 0
    li_2 = []
    while i < len(a_1) and j < len(a_2):
        if a_1[i] < a_2[j]:
            a_li.append(a_1[i])
            li_2.append(a_1[i])
            i += 1
        else:
            a_li.append(a_2[j])
            li_2.append(a_2[j])
            j += 1
    
    while i < len(a_1):
        a_li.append(a_1[i])
        li_2.append(a_1[i])
        i += 1
    
    while j < len(a_2):
        a_li.append(a_2[j])
        li_2.append(a_2[j])
        j += 1

    # a_1으로 리턴
    return li_2

N, K = map(int, input().split())
A = list(map(int, input().split()))

a_li = []
m_sort(A)

if len(a_li) >= K:
    print(a_li[K - 1])
else:
    print(-1)