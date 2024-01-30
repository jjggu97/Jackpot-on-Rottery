import random

def generate_powerball_ticket():
    white_balls = random.sample(range(1, 70), 5)  # 1부터 69 사이의 5개의 서로 다른 숫자 선택
    power_ball = random.randint(1, 26)            # 1부터 26 사이의 파워볼 번호 선택
    return sorted(white_balls), power_ball

def simulate_powerball_tickets(num_tickets):
    tickets = []
    for _ in range(num_tickets):
        ticket = generate_powerball_ticket()
        tickets.append(ticket)
    return tickets

def main():
    num_tickets = int(input("구매할 티켓 수를 입력하세요: "))
    tickets = simulate_powerball_tickets(num_tickets)
    print("\n구매한 티켓:")
    for idx, ticket in enumerate(tickets, start=1):
        white_balls, power_ball = ticket
        print(f"티켓 {idx}: {white_balls}, 파워볼: {power_ball}")

if __name__ == "__main__":
    main()
