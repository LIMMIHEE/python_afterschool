
i,k =0,0

while i < 9 :
    if i<5:
        k=0
        while k < k-i:
            print(' ',end='')
            k=k+1;
        k=0
        while k< i+2+1:
            print('\u2605',end='')
            k = k+1;
    else:
        while k< i-4:
            print(' ',end='')
            k = k+1
        k=0
        while k < (9-i)*2-1:
            print('\u2605',end='')
            k = k+1

    print()
    i +=1;
