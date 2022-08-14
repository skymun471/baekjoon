import sys
# data = list(map(str, sys.stdin.readline().split()))
n, m = map(int, sys.stdin.readline().split())
# print(n, m)
original = []
result_list = []

# 2차원 리스트 입력 받기
# board = [list(map(str, sys.stdin.readline().split())) for _ in range(n)]

# for _ in range(n):
#     original.append(sys.stdin.readline().split())

for _ in range(n):
    original.append(input())

for a in range(n-7):
    for b in range(m-7):
        BW = 0
        WB = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j)%2 == 0:
                    if original[i][j] != 'W':
                        BW += 1
                    if original[i][j] != 'B':
                        WB += 1
                        # 시작이 B 일때
                else:
                    if original[i][j] != 'B':
                        BW += 1
                    if original[i][j] != 'W':
                        WB += 1
        result = min(BW , WB)
        result_list.append(result)


print(min(result_list))