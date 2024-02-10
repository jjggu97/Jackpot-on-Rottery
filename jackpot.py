import random

def run_powerball(num_trials):
    win_count = 0
    
    for _ in range(num_trials):
        white_balls = set()
        while len(white_balls) < 6:
            white_ball = random.randint(1, 69)
            white_balls.add(white_ball)

        bonus_ball = random.randint(1, 26)

        chosen_bonus = int(input('Enter your chosen bonus number (1-26): '))

        if chosen_bonus == bonus_ball:
            win_count += 1

    return win_count

def main():
    num_trials = int(input("Enter the number of Powerball trials: "))
    num_wins = run_powerball(num_trials)

    print(f"Out of {num_trials} trials, you won {num_wins} times.")
    print(f"The probability of winning was {num_wins / num_trials * 100:.2f}%.")

if __name__ == "__main__":
    main()
