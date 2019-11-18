i=0;
number1,number2,number3,number4,number5,number6=0,0,0,0,0,0

while number1!=number2!=number3!=number4!=number5!=number6:
        i=i+1;
        number1=(random.randrange(0,5+1))+1
        number2=(random.randrange(0,5+1))+1
        number3=(random.randrange(0,5+1))+1
        number4=(random.randrange(0,5+1))+1
        number5=(random.randrange(0,5+1))+1
        number6=(random.randrange(0,5+1))+1
        if number1==number2==number3==number4==number5==number6:
            print(i,"회 돌았습니다")
            
        
