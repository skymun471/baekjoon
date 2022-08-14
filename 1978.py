# 소수 : 인수가 자기 자신과 1뿐인 수 
import sys

n = int(input())
count = 0
result = 0
data = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    count = 0
    if data[i] > 1:
        for k in range(2,data[i]):
                if (data[i]%k == 0):
                    count+=1
        if count == 0:
            result += 1
        
print(result)


# 조건은 바로바로 그 구간에서 설정하고 걸러내야 오류가 발생 확률이 낮다.