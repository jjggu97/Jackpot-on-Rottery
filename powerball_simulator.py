import random

def powerball_simulation(num_tickets, num_simulations):
    winning_numbers = set(random.sample(range(1, 70), 5))
    winning_powerball = random.randint(1, 26)
    wins = 0

    for _ in range(num_simulations):
        for _ in range(num_tickets):
            ticket_numbers = set(random.sample(range(1, 70), 5))
            ticket_powerball = random.randint(1, 26)
            if ticket_numbers == winning_numbers and ticket_powerball == winning_powerball:
                wins += 1

    return wins

num_tickets = int(input("복권을 구매한 갯수를 입력하세요: "))
num_simulations = int(input("시뮬레이션 횟수를 입력하세요: "))

win_count = powerball_simulation(num_tickets, num_simulations)
print("실제로 당첨된 횟수:", win_count)
