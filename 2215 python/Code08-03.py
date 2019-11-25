mlist =[]
i=0;
imax=0, imin=100


while(i<5):
    score=int(input("점수(0~100) : "))
    mlist.append(score)
    mix += score
    if(imax<score):
        imax=score
        mlist.remove(score)
    if(imin>score):
        imin=score
        mlist.remove(score)
    i+=1

a= mlist.length
mia=0
for j in range(0,a):
    mia+=mlist[j];
    
mia=(int)mia/3

print("평균 : %d, 최고점은 %d 최하점은 %d" %((int)mia/3, imax,imin))
    
    





