num= int(input("정수를 입력하시오 : "))


one=num//1000
num -= one*1000
two=num//100
num -= two*100
three=num//10
num -= three*10

plus = one+two+three+num

print("자리 수의 합 : ",plus)


