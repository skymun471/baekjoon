import sys
x, y, w, h = map(int, sys.stdin.readline().split())
result = [x, h-y, w-x, y]
print(min(result))
