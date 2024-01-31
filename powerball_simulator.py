import itertools

def calculate_powerball_odds():
    white_balls_count = 5
    white_balls_pool = 69
    power_ball_pool = 26

    total_outcomes = (white_balls_pool * (white_balls_pool - 1) * (white_balls_pool - 2) * (white_balls_pool - 3) * (white_balls_pool - 4)) // (5 * 4 * 3 * 2 * 1) * power_ball_pool
    total_possible_combinations = (white_balls_pool ** white_balls_count) * power_ball_pool

    probability = total_outcomes / total_possible_combinations

    return probability

def main():
    probability = calculate_powerball_odds()
    print(f"The probability of winning the Powerball lottery: {probability:.15f}")

if __name__ == "__main__":
    main()
