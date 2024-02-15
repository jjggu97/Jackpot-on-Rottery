import random

def generate_powerball_numbers():
    powerball_numbers = random.sample(range(1, 70), 5)
    powerball_numbers.sort()
    powerball_numbers.append(random.randint(1, 26))
    return powerball_numbers

def get_user_numbers():
    print("Choose your Powerball numbers (5 numbers from 1 ~ 69):")
    user_numbers = []
    while len(user_numbers) < 5:
        try:
            number = int(input(f"Enter {len(user_numbers) + 1}nd number: "))
            if 1 <= number <= 69 and number not in user_numbers:
                user_numbers.append(number)
            else:
                print("Enter a valid number between 1 ~ 69.")
        except ValueError:
            print("Enter a valid number.")
    
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

# simulate powerball
def check_winner(user_numbers, powerball_numbers):
    match_count = len(set(user_numbers) & set(powerball_numbers[:5]))
    powerball_match = user_numbers[-1] == powerball_numbers[-1]
    if match_count == 5 and powerball_match:
        return "Jackpot! You won!"
    elif match_count == 5:
        return "Congratulations! You matched all 5 numbers but not the Powerball."
    elif match_count == 4 and powerball_match:
        return "You matched 4 numbers plus the Powerball! Well done!"
    elif match_count == 4:
        return "You matched 4 numbers. Good job!"
    elif match_count == 3 and powerball_match:
        return "You matched 3 numbers plus the Powerball!"
    elif match_count == 3:
        return "You matched 3 numbers."
    elif match_count == 2 and powerball_match:
        return "You matched 2 numbers plus the Powerball."
    elif match_count == 1 and powerball_match:
        return "You matched 1 number plus the Powerball."
    elif powerball_match:
        return "You matched the Powerball only."
    else:
        return "Sorry, you didn't win this time."

def simulate_lottery(purchase_count):
    wins = {
        "Jackpot": 0,
        "5 numbers (no Powerball)": 0,
        "4 numbers + Powerball": 0,
        "4 numbers": 0,
        "3 numbers + Powerball": 0,
        "3 numbers": 0,
        "2 numbers + Powerball": 0,
        "1 number + Powerball": 0,
        "Powerball only": 0,
        "No win": 0
    }
    
    for _ in range(purchase_count):
        user_numbers = get_user_numbers()
        powerball_numbers = generate_powerball_numbers()
        match_result = check_winner(user_numbers, powerball_numbers)
        
        if "Jackpot" in match_result:
            wins["Jackpot"] += 1
        elif "5 numbers" in match_result:
            wins["5 numbers (no Powerball)"] += 1
        elif "4 numbers + Powerball" in match_result:
            wins["4 numbers + Powerball"] += 1
        elif "4 numbers" in match_result:
            wins["4 numbers"] += 1
        elif "3 numbers + Powerball" in match_result:
            wins["3 numbers + Powerball"] += 1
        elif "3 numbers" in match_result:
            wins["3 numbers"] += 1
        elif "2 numbers + Powerball" in match_result:
            wins["2 numbers + Powerball"] += 1
        elif "1 number + Powerball" in match_result:
            wins["1 number + Powerball"] += 1
        elif "Powerball only" in match_result:
            wins["Powerball only"] += 1
        else:
            wins["No win"] += 1
    
    return wins

def main():
    purchase_count = int(input("Enter the number of Powerball tickets you want to purchase: "))
    results = simulate_lottery(purchase_count)
    
    print("\nResults after simulating", purchase_count, "Powerball tickets:")
    for outcome, count in results.items():
        print(f"{outcome}: {count} times")
    
if __name__ == "__main__":
    main()
