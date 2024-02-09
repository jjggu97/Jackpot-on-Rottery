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

a = None

if bonus_ball == num:
    a = 1
else:
    a = 0

a = 1 (print("You won!"))
a = 0 (print("You lose.."))

