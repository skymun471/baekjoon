# 벌집 구조를 이해하여 몇번만에 해당 숫자에 해당하는 벌집에 도달할 수 있는지를 구하는 문제

n = int(input())

beehome = 1
i = 1
while n > beehome:
    beehome += 6*i
    i += 1
print(i)

