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
