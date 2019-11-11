import turtle as t


num=input("도형을 입력하시오(사각형 또는 원):")

if(num=="원"):
    z=int(input("원의 반지름 : "))
    t.circle(z);

elif(num=="사각형"):
    x=int(input("가로 : "))
    y=int(input("세로 : "))
    for i in range(4):
        if(i==0 or i==2):
             t.forward(x)
             t.right(90)
        else:
             t.forward(y)
             t.right(90)
else:
    print("잘못 입력 했어요");
