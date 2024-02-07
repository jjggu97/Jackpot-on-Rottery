import random

list = []
white_ball = random.randint(1,69)

# select five numbers (white balls)
for a in range(5):
    while white_ball in list:
        white_ball = random.randint(1,69)
    list.append(white_ball)

# select bonus ball

bonus_ball = random.randint(1,26)


print(list,bonus_ball)
