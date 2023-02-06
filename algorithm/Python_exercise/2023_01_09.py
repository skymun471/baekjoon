# len() 개수 세기
a = len([1,2,3])
b = len('abc') # 글자의 개수는 ''안에 들어있는 글자 수 만큼의 리스트를 만든다.
print(a,b)

s = len('abcdefg')
print(s)

string = 'abcdef'
print(len(string))

list = [1,2,3]
print(len(list))

# 반복문 이용하여 반복하기
for i in range(len(list)):
    print(i)
# 배열은 인덱스로 접근하기 떄문에 0인덱스 부터 시작한다.
for i in range(0,3):
    print(i)
# 위 len(0)을 사용한것과 똑같은 역할을한다.
for idx in range(string):
    print(idx)
# 처음에는 실제 의미로 써주는 것이 좋다.
