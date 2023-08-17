# 구구단 함수를 ex03_function.py 에 각각 정의하고
# main에서 1,2 번 선택을 받아 세로형, 가로형을 각각
# 출력할 수 있도록 하시오

from ex03_function import *



run = True
while run:
    count = int(input("입력"))
    if count==1:
        dan()
    elif count==2:
        dan1()
        print()
    else:
        run= False