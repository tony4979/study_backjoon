import sys
x = sys.stdin.readline()
y = list(map(int,sys.stdin.readline().split()))
y = sorted(y)
print(y[0]*y[-1])