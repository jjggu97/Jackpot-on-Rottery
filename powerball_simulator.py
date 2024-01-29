import random

def generate_powerball_ticket():
    white_balls = random.simple(range(1,70),5)
    power_ball = random.randint(1,26)
    return sorted(white_balls),power_ball

def simulate_powerball_tickets(num_tickets):
    tickets = []
    