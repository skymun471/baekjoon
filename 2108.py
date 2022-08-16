#통계학
import sys

n = int(input())
result = []

for _ in range(n):
    result.append(int(sys.stdin.readline()))


print("======")
# 정렬
result.sort()
# round를 활용하면 소수 표현 자리수를 표기 할 수 있다.
# round의 두번째 인자를 비워두면 소수 첫번째 자리에서 반올림하여 정수로 나타낸다.
print(round(sum(result)/n))
print(n//2)

result_1 = list(set(result))
result_1.sort()
# print(type(result_1))
p = []
p_idx = []
for i in result_1:  # 0~4
    cnt = 0
    for k in range(n):
        if  i == result[k]:
            cnt += 1
    p.append(cnt)
    p_idx.append(i)    

max_idx = p.index(max(p))



if max_idx == 0:
    print(result_1[1])
else:
    print(result_1[max_idx])


print(max(result)-min(result))

