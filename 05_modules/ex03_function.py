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