import sys
# 이분 탐색을 통해서 구현하지 않으면 시간 초과 결과를 가져온다.

k, n = map(int, sys.stdin.readline().split())
lan = []
for _ in range(k):
    lan.append(int(sys.stdin.readline()))

start = 1
end = max(lan)

while start <= end:
    mid = (start + end)//2
    result = 0
    for i in lan:
        result += int(i/mid)

    if result >= n:  #중간 값보가 큰 값일때
        start = mid + 1
    else:
        end = mid - 1 #중간 값보다 작은 값일때

print(end)