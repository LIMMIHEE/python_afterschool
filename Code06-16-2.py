i,k,line = 0,0,""

for i in range(9,2,-1):
    line=line + ("# %d단 #"%i)

print(line)

for i in range(9,1,-1):
    line=""
    for k in range(9,1,-1):
        line=line+("%3d * %3d = %3d   "%(k,i,k*i))

    print(line)
