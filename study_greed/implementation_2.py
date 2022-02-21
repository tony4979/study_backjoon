n = int(input())
result = 0 # 3이 들어간 모든 경우의 수
count = 0 # 3 카운트

for h in range(0,n+1):
    for m in range(60):
        for s in range(60):
            if str(h).count('3')>0:
                count +=1
            elif str(m).count('3')>0:
                count +=1
            elif str(s).count('3')>0:
                count +=1
            if count > 0:
                result +=1
                count = 0

print(result)