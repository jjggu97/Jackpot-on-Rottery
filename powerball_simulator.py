import random

def generate_powerball_ticket():
    white_balls = random.sample(range(1, 70), 5)  # Select 5 different numbers from 1 to 69
    power_ball = random.randint(1, 26)            # Select a number from 1 to 26 for the Powerball
    return sorted(white_balls), power_ball

def simulate_powerball_tickets(num_tickets):
    winning_ticket = generate_powerball_ticket()
    num_winning_tickets = 0

    for _ in range(num_tickets):
        ticket = generate_powerball_ticket()
        if ticket == winning_ticket:
            num_winning_tickets += 1

    probability = num_winning_tickets / num_tickets
    return probability

def main():
    num_tickets = int(input("Enter the number of tickets to simulate: "))
    num_simulations = int(input("Enter the number of simulations to run: "))
    
    total_probability = 0
    for _ in range(num_simulations):
        total_probability += simulate_powerball_tickets(num_tickets)
    
    average_probability = total_probability / num_simulations
    print(f"After {num_simulations} simulations with {num_tickets} tickets each, the average probability of winning is: {average_probability:.15f}")

if __name__ == "__main__":
    main()
