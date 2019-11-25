import operator

trainDic, traintList= {},[]

trainDic = {'Thomas ': '토마스','edward':'에드워드','henry' : '헨리','Gothan':'고든',
            'james' : '제임스' }
trainList = sorted(trainDic.items(),key = operator.itemgetter(0))


print(trainList)
