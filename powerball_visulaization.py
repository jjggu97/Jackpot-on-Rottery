import random
import matplotlib.pyplot as plt

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
                print("Please enter a valid number between 1 and 26.")
        except ValueError:
            print("Please enter a valid number.")
    
    return user_numbers

# simulate powerball
def check_winner(user_numbers, powerball_numbers):
    return user_numbers[:-1] == powerball_numbers[:5]

def count_matching_numbers(user_numbers, powerball_numbers):
    matching_numbers = sum(num in powerball_numbers[:5] for num in user_numbers[:-1])
    bonus_match = 1 if user_numbers[-1] == powerball_numbers[-1] else 0
    return matching_numbers + bonus_match

def simulate_and_visualize(max_attempts=10000):
    matching_numbers_count = []
    
    user_numbers = get_user_numbers()
    print("Your numbers:", user_numbers[:-1], "Bonus number:", user_numbers[-1])
    
    for _ in range(max_attempts):
        powerball_numbers = generate_powerball_numbers()
        matching_numbers = count_matching_numbers(user_numbers, powerball_numbers)
        matching_numbers_count.append(matching_numbers)
    
    # Visualizing
    plt.hist(matching_numbers_count, bins=range(8), align='left', rwidth=0.5)
    plt.xlabel('Number of Matching Numbers')
    plt.ylabel('Frequency')
    plt.title('Matching Numbers in Powerball Simulation')
    plt.xticks(range(8))
    plt.grid(axis='y', alpha=0.75)
    plt.show()

if __name__ == "__main__":
    simulate_and_visualize()
