num = int(input("지쳬호 교환할 돈은 얼마? : "))


i=num/50000
num-=(i*50000)
print("50000원 짜리 ==>",i,"장\n");

i=num/10000
num-=(i*10000)
print("10000원 짜리 ==>",i,"장\n")

i=num/5000
num-=(i*5000)
print("5000원 짜리 ==>",i,"장\n")

i=num/5000
num-=(i*1000)
print("1000원 짜리 ==>",i,"장\n")

print("바꾸지 못한 돈 : ",num)
