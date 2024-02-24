import random

def generate_powerball_numbers():
    powerball_numbers = random.sample(range(1, 70), 5)
    powerball_numbers.sort()
    powerball_numbers.append(random.randint(1, 26))
    return powerball_numbers

def get_user_numbers():
    print("Choose your 5 numbers (5 numbers from 1 ~ 69):")
    user_numbers = []
    while len(user_numbers) < 5:
        try:
            number = int(input(f"Enter your number [{len(user_numbers) + 1}]: "))
            if 1 <= number <= 69 and number not in user_numbers:
                user_numbers.append(number)
            else:
                print("Enter a valid number between 1 ~ 69.")
        except ValueError:
            print("Enter a valid number.")
    while True:
        try:
            powerball_number = int(input("Enter your bonus number (1 to 26): "))
            if 1 <= powerball_number <= 26:
                user_numbers.append(powerball_number)
                break
            else:
                print("Please enter a valid Powerball number between 1 and 26.")
        except ValueError:
            print("Please enter a valid number.")
    
    return user_numbers

# simulate powerball
def check_winner(user_numbers, powerball_numbers):
    match_count = len(set(user_numbers) & set(powerball_numbers[:5]))
    powerball_match = user_numbers[-1] == powerball_numbers[-1]
    if match_count == 5 and powerball_match:
        return "Jackpot! You matched ALL numbers!"
    elif match_count == 5:
        return "Congratulations! You matched all numbers! (except bonus ball.)"
    elif match_count == 4 and powerball_match:
        return "You matched 4 numbers and bonus number!"
    elif match_count == 4:
        return "You matched 4 numbers."
    elif match_count == 3 and powerball_match:
        return "You matched 3 numbers and bonus number!"
    elif match_count == 3:
        return "You matched 3 numbers."
    elif match_count == 2 and powerball_match:
        return "You matched 2 numbers and bonus number!"
    elif match_count == 1 and powerball_match:
        return "You matched 1 number and bonus number."
    elif powerball_match:
        return "You matched bonus number."
    else:
        return "Sorry, you didn't win this time."

def main():
    play_again = True
    attempts = 0
    while play_again:
        user_numbers = get_user_numbers()
        powerball_numbers = generate_powerball_numbers()
        print("Your numbers:", user_numbers[:-1], "Bonus number:", user_numbers[-1])
        print("Winning numbers:", powerball_numbers[:-1], "Bonus number:", powerball_numbers[-1])
        print(check_winner(user_numbers, powerball_numbers))
        attempts += 1
        play_again = input("Do you want to play again? (yes/no): ").lower() == 'yes'
    print("Total attempts:", attempts)

if __name__ == "__main__":
    main()
