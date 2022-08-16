import sys
n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
B = list(map(int,sys.stdin.readline().split()))


#모든 수를 비교하기 때문에 시간이 오래걸리는 문재점이 있다.
# =============================================
# for i in B:
#     result = 0
#     for k in A:
#         if i == k:
#             result += 1
#     if result !=0:
#         print(1)
#     else:
#         print(0)


# 이를 해결하기 위해서 A 리스트를 정렬하고 인덱스를 구해 중간 값을 B 리스트 요소와 비교한다.
# 만약 B 요소가 A 요소 보다 크다면 해당하는 값이 중간 값보다 위쪽(오른쪽)에 있는 상황이기 때문에 start 값을 mid + 1로 지정하여 오른쪽으로 치우친 범위에서 값을 찾도록한다.
# 이를 반복하면 범위가 점점 작아지고 중간 값이 찾는 값과 같아질 확률이 높아진다.
# 중간 값과 B의 요소를 비교하여 로직이 돌아가도록 코드를 개편해야한다.

A.sort()

for i in B:
    start = 0
    end = n - 1
    result = False
    while start <= end:
        mid  = (start+end)//2
        if A[mid] == i:
            result = True
            print(1)
            break
        elif A[mid] < i:
            start = mid + 1
        else:
            end = mid - 1  
    if result == False:
        print(0)