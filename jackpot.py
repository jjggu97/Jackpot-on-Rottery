import random

def generate_powerball_numbers():
    # Select 5 numbers from 1 to 69 for the Powerball drawing
    # Select 1 number from 1 to 26 for the Powerball itself
    powerball_numbers = random.sample(range(1, 70), 5)
    powerball_numbers.sort()
    powerball_numbers.append(random.randint(1, 26))
    return powerball_numbers

def get_user_numbers():
    # Prompt the user to select 5 numbers from 1 to 69
    # Also, prompt to select 1 Powerball number from 1 to 26
    print("Choose your Powerball numbers (5 numbers from 1 to 69):")
    user_numbers = []
    while len(user_numbers) < 5:
        try:
            number = int(input(f"Enter {len(user_numbers) + 1}nd number: "))
            if 1 <= number <= 69 and number not in user_numbers:
                user_numbers.append(number)
            else:
                print("Please enter a valid number between 1 and 69.")
        except ValueError:
            print("Please enter a valid number.")
    
    while True:
        try:
            powerball_number = int(input("Enter your Powerball number (1 to 26): "))
            if 1 <= powerball_number <= 26:
                user_numbers.append(powerball_number)
                break
            else:
                print("Please enter a valid Powerball number between 1 and 26.")
        except ValueError:
            print("Please enter a valid number.")
    
    return user_numbers
