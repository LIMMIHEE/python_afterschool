import random

for num in range(0,1):
    numbers=(random.randrange(0,10))
    print("A 주사위 숫자는", numbers)

for num in range(0,1):
    number=(random.randrange(0,10))
    print("B 주사위 숫자는", number)

if number==numbers:
    print("비걌습니다")
elif number> numbers :
    print("B가 이겼걌습니다")
else:
    print("A가 이겼걌습니다")
