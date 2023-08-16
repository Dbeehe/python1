# 실행하면 콘솔에서 1또는2를 입력받고 1은 세로형구구단, 2는 가로형구구단을 각각 출력한다.
# 구구단은 각각 함수로 정의하도록 한다

def dan():
    for i in range(2, 10):
        print(i,"단")
        for j in range(1, 10):
            print(i, "X", j, "=", i*j)

def dan1():
    for i in range(2, 10):
        print()
        print(i,"단")
        for j in range(1, 10):
            print(i, "X", j, "=", i*j,end="  ")


count = int(input("입력"))

if count==1:
    dan()
elif count==2:
    dan1()
else:
    print("1 or 2만 입력")