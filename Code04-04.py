str=input("16진수 한 글자 입력 : ")

if((str>='0' and str <= '9') or (str>='a' and str<='f') or(str>='A' and str<='F')):
    print("10진수 ==>",int(str,16))
else :
    print("16진수가 아님")




#str=input("2진수 한 글자 입력 : ")

#if(str):
 #   print(int(str,10))

#else :
#    print("2진수가 아님")

