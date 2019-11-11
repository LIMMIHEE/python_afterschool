answer = 0
num1 = int(input("첫 번째 숫자 입력하세요 : " ))
num2 = int(input("두 번째 숫자 입력하세요 : " ))
num3 = int(input("더할  숫자 입력하세요 : " ))
for i in range(num1,num2+1,num3):
    answer = answer+i


print(num1,"+",(num1+num3),"...+",num2,"는 ",answer,"입니다")
