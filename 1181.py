import sys

n = int(input())
data = []
result_ary = []

# data = [list(map(str, sys.stdin.readline().split())) for _ in range(n)]

for i in range(n):
    data.append(sys.stdin.readline().strip())
# strip()은 앞뒤 공백을 제거 해준다.
data = list(set(data))
data.sort() # 아무런 조건 없는 sort는 리스트 내부가 문자열 일때 알파벳순으로 자동 정렬 해준다.
data.sort(key = len)

for i in data:
    print(i)