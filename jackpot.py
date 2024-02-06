import random

list = []
white_ball = random.randint(1,69)

# select five numbers (white balls)
for _ in range(5):
    while white_ball in list:
        white_ball = random.randint(1,69)
    list.append(white_ball)

print(list[0])


