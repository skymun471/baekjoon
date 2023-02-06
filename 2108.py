#통계학
import sys

n = int(input())
result = []

for _ in range(n):
    result.append(int(sys.stdin.readline()))


# print("======")
# 정렬
result.sort()
# round를 활용하면 소수 표현 자리수를 표기 할 수 있다.
# round의 두번째 인자를 비워두면 소수 첫번째 자리에서 반올림하여 정수로 나타낸다.
print(round(sum(result)/n))
print(result[n//2])

result_1 = list(set(result))
result_1.sort()
p_idx = []


for i in result_1:  # 0~4
    cnt = 0
    for k in range(n):
        if  i == result[k]:
            cnt += 1
    if cnt >= 2:
        p_idx.append(i)    

if  len(p_idx) == 0:
    if len(result_1) == 1:
        print(result[0])
    else:
        print(result[1])
else:
    print(p_idx[1])

print(max(result)-min(result))

