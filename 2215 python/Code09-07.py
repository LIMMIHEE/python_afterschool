import operator

count = int(input("입력하는 학생수가 퐁 몇명인가요 :"))
print("학생의 이름과 시험 점수를 차례대로 입력하세요!")

scores = list()
num =1

while(num <= count):
    print(num,"번째 학생=====")
    name = input("이름 " )
    score = input("점수  " )
    pair = (name,score)
    scores.append(pair)

scores_dict = dict(scores)

flag = True
while flag :
    wanted = input("어떤 학생의 점수가 궁금하신가요? 이름을 입력하세요 : ")
