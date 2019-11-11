num= int(input("투입한 돈 : " ))
num2 = int(input("물건값 : "))

num3= num-num2

print("거스름 돈: ",num3)

num4 = num3//500
num3 -= num4*500
num5 = num3//100
num3 -= num5*100
num6 = num3//50
num3 -= num6*50
num7 = num3//10

for i in 



print("500원 ==>",num4)
print("100원 ==>",num5)
print("50원 ==>",num6)
print("10원 ==>",num7)

