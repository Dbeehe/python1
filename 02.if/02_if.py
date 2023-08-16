# 자바의 scanner 처럼 실행후 콘솔에서 숫자를 입력받아
# 홀수, 짝수를 판변하여 출력하는 코드를 작성하시오.


num = int(input("입력하세요"))

if num%2==0:
    print("짝수")
else:
    print("홀수")