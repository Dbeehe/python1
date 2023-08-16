# 중첩 for문을 이용하여 구구단을 세로형, 가로형으로 각각 만들기,


for i in range(2, 10):
    print(i,"단")
    for j in range(1, 10):
        print(i, "X", j, "=", i*j)

for i in range(2, 10):
    print()
    print(i,"단")
    for j in range(1, 10):
        print(i, "X", j, "=", i*j,end="  ")

