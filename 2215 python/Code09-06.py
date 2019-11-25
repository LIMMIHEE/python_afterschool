foods={'떡':'어묵','딸기':'잼','초콜릿':'누텔라'};

while(True):
    myFood= input(str(list(foods.keys()) + "를 좋아하는 음식은? ")
    if myFood in foods :
        print("<%s> 궁합음식은 <%s>입니다 " % (myFood, foods,get(myFood)))
    elif(myFood == "끝"):
        break;
    else:
        print("그런 음식이 없습니다, 확인해 보세요.")
