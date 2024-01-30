import random

def generate_powerball_ticket():
    white_balls = random.sample(range(1, 70), 5)  
    power_ball = random.randint(1, 26)          
    return sorted(white_balls), power_ball

def simulate_powerball_tickets(num_tickets):
    tickets = []
    for _ in range(num_tickets):
        ticket = generate_powerball_ticket()
        tickets.append(ticket)
    return tickets

def main():
    num_tickets = int(input("Enter number of ticket : "))
    tickets = simulate_powerball_tickets(num_tickets)
    print("\nTicket Bought:")
    for idx, ticket in enumerate(tickets, start=1):
        white_balls, power_ball = ticket
        print(f"Ticket {idx}: {white_balls}, Power ball: {power_ball}")

if __name__ == "__main__":
    main()
