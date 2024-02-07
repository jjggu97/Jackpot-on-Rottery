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

num = int(input('Enter the number : '))

if bonus_ball == num:
    print(f"you select right number, the number is {bonus_ball}")
else:
    print(f"you select wrong number, the number is {bonus_ball}")
