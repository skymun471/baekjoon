# 팰린드롬수
import sys

while True:
    # input()은 기본적으로 str로 받아온다.
    # sys.stdin.readline()으로 읽어 왔을떄 type은 str이었지만 조건문으로 인식이 되지 않았다.
    # 그 이유를 잘 모르겠다.
    data = input()
    
    if data == "0":
        break

    # python slicing: a[start:end:step]
    # 실제 인덱스 end -1 까지 표기된다.    
    if data[::-1] == data:
        print("Yes")
    else:
        print("No")


