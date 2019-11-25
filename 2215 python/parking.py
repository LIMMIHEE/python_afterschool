import sys
parking = [ ]
top=0
carName="A"
outCar=""

while(1):
    i = int(input("<1>자동차 넣기 <2>자동차 빼기 <3>끝 : "))

    if(i==1):
        if(top>=5):
            print("주차장이 꽉 찼습니다")
        else:
            parking.append(carName)
            print("% 자동차가 들어감. 주차장 상태 ==> %" %parking[top],parking)
            top+=1
            carName = char(ord(carName)+1)
    elif(i==2):
        if(top<=0):
            print("주차장이 비었습니다")
        else:
            outCar = parking.pop()
            print("% 자동차가 나감. 주차장 상태 ==> %" %outCar,parking)
            top-=1
            carName = char(ord(carName)-1)

    elif(i==3):
         print("종료")
         break
    else:
        print("잘못입력함")
