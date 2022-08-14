#선택 정렬 : 여러 데이터 중에서 가장 작은 값을 뽑는 작동을 자동으로 반복하여 값을 정렬하는 방식이다.
import sys

# 최솟값을 찾는 함수   
# def findminidx(ary):
#     minidx = 0
#     for i in range(1, len(ary)):
#         if (ary[minidx] > ary[i]):
#             minidx = i
#     return minidx



# if __name__ == '__main__':

#     before_data_ary = list(map(int, sys.stdin.readline().split()))
#     after_data_ary = []

    
    ## 배열을 두개 사용하는 sort
    # ----------------------------------------------------------
    # for _ in range(len(before_data_ary)):
    #     minidx= findminidx(before_data_ary)
    #     after_data_ary.append(before_data_ary[minidx])
    #     del(before_data_ary[minidx])

    ## 배열을 한개만 사용하여 서로의 위치를 바꿔주는 sort 방식 
    # ----------------------------------------------------------
    # for i in range(len(before_data_ary)-1):
    #     minidx = i
    #     for k in range(i+1, len(before_data_ary)):
    #         if before_data_ary[minidx] > before_data_ary[k]:
    #             minidx = k
    #     temp = before_data_ary[i]
    #     before_data_ary[i] = before_data_ary[minidx]
    #     before_data_ary[minidx] = temp
            
        
    # print(before_data_ary)
    # print(after_data_ary)
    
# 삽입 정렬
# ====================================================================================================
# 삽입 정렬은 요소 하나 하나를 자신보다 작고 자신보다 큰 사람 사이에 세우면 된다.
# 알고리즘 원리: 빈 배열, 자신보다 큰 요소가 없는 경우 맨 뒤에 위치하면 된다.
# 자신보다 큰 원소가 있는 경우는 그 원소 앞애 세우면된다.

## 정렬에서 자신이 삽입될 위치를 찾는 함수

def findinsertidx (ary, data):
    findidx = -1
    for i in range(0,len(ary)):
        if ary[i] > data:
            findidx = i
            break
    if findidx == -1: # 자신 보다 큰 값이 없을 때나 빈 배열일 때
        return len(ary)
    else:
        return findidx 


if __name__ == '__main__':
    ary = list(map(int, sys.stdin.readline().split()))
    # data = int(input())
    # result = findinsertidx(ary, data)
    # print(result)
    
    result_ary = []
    for i in range(len(ary)):
        insertidx = findinsertidx(result_ary, ary[i])
        print(insertidx)
        result_ary.insert(insertidx, ary[i])

    print(result_ary)
