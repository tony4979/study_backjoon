# 하향식(탑다운) 다이나믹 프로그래밍 메모이제이션(Memoization)
# 캐싱(Cashing)이라고도 함
d = [0] * 100

def fibo(x):

    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))
