n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data:
    count +=1 # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i: # 현재 그룹에 해당 모험가를 포함시키기
        result += 1 # 총 그룹의 수 증가시키기
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화

print(result)
