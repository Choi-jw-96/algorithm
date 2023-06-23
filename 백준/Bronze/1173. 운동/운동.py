N, m, M, T, R = map(int, input().split())

cnt = t = 0
now = m
if m + T > M:
  pass
else:
   while t < N:
      if now + T <= M:
          now += T
          t += 1
      else:
          now = max(m, now - R)
      cnt += 1

if t == N:
    print(cnt)
else:
    print(-1)