N , K = map(int,input().split())
count = 0
while(N!=1):
  # 나누어 떨어질 때 나누기
  if N%K==0:
    N /= K
    count += 1
  # N에 1 빼주기
  else:
    N -= 1
    count += 1

print(count)
