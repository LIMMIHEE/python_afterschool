ch=""
a,b=0,0

while True:
    a= int(input("계산할 첫 수를 입력하시오 : "))
    b= int(input("계산할 두 번째수를 입력하시오 : "))
    ch= input("계산할 연산자를 입력하시오 : ")

    if ch=="+" :
        print(a+b)
    elif(ch=="-"):
        print(a-b)
    elif(ch=="*"):
        print(a*b)
    elif(ch=="/"):
        print(a/b)
    else:
        print("사칙연산만 가능합니다")
    
