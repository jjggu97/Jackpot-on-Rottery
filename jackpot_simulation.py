import random
import matplotlib.pyplot as plt

def generate_powerball_numbers():
    # Generate Powerball numbers
    powerball_numbers = random.sample(range(1, 70), 5)
    powerball_numbers.sort()
    powerball_numbers.append(random.randint(1, 26))
    return powerball_numbers

# Function to calculate winning counts through simulation
def simulate_draws(num_draws):
    results = {
        "Jackpot": 0,
        "5 Numbers": 0,
        "4 Numbers + Powerball": 0,
        "4 Numbers": 0,
        "3 Numbers + Powerball": 0,
        "3 Numbers": 0,
        "2 Numbers + Powerball": 0,
        "1 Number + Powerball": 0,
        "Powerball": 0,
        "None": 0
    }

    for _ in range(num_draws):
        user_numbers = generate_powerball_numbers()
        powerball_numbers = generate_powerball_numbers()
        result = check_winner(user_numbers, powerball_numbers)

        results[result] += 1

    return results

# Function to plot winning probabilities
def plot_results(results):
    labels = list(results.keys())
    values = list(results.values())

    plt.figure(figsize=(10, 6))
    plt.barh(labels, values, color='skyblue')
    plt.xlabel('Frequency')
    plt.ylabel('Winning Category')
    plt.title('Powerball Winning Probability')
    plt.gca().invert_yaxis()  # Invert the axis to have the most frequent category on top
    plt.show()

def main():
    num_draws = 100000  # Number of draws for simulation
    results = simulate_draws(num_draws)
    plot_results(results)

if __name__ == "__main__":
    main()
