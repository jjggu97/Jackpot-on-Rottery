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
    return user_numbers[:-1] == powerball_numbers[:5]

def count_matching_numbers(user_numbers, powerball_numbers):
    return sum(num in powerball_numbers[:5] for num in user_numbers[:-1])

def main():
    user_numbers = get_user_numbers()
    print("Your numbers:", user_numbers[:-1], "Bonus number:", user_numbers[-1])
    
    attempts = 0
    max_attempts = 10000
    max_matching_numbers = 0
    
    while attempts < max_attempts:
        attempts += 1
        powerball_numbers = generate_powerball_numbers()
        print("Winning numbers:", powerball_numbers[:-1], "Bonus number:", powerball_numbers[-1])
        
        matching_numbers = count_matching_numbers(user_numbers, powerball_numbers)
        
        if matching_numbers > max_matching_numbers:
            max_matching_numbers = matching_numbers
        
        if check_winner(user_numbers, powerball_numbers):
            print(f"Congratulations! You won after {attempts} attempts!")
            break
        else:
            print(f"Sorry, you didn't win this time. Matching numbers: {matching_numbers}. Trying again...")
    else:
        print(f"Maximum attempts reached ({max_attempts}).")
        print(f"Maximum matching numbers in a single attempt: {max_matching_numbers}. Exiting the game.")

if __name__ == "__main__":
    main()
