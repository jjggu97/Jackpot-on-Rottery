import matplotlib.pyplot as plt

# Probabilities for each winning rank (example)
winning_probabilities = {
    '5 + Powerball': 1.3e-8,
    '5': 1.4e-7,
    '4 + Powerball': 0.000018,
    '4': 0.00075,
    '3 + Powerball': 0.00085,
    '3': 0.038,
    '2 + Powerball': 0.052,
    '1 + Powerball': 0.91,
    'Powerball': 0.39
}

def visualize_powerball_probabilities(probabilities):
    plt.figure(figsize=(10, 6))
    plt.barh(list(probabilities.keys()), list(probabilities.values()), color='skyblue')
    plt.title('Powerball Winning Probabilities')
    plt.xlabel('Probability')
    plt.ylabel('Rank')
    plt.xscale('log')  # Use logarithmic scale
    plt.gca().invert_yaxis()  # Invert the y-axis to display ranks in descending order
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.show()

visualize_powerball_probabilities(winning_probabilities)
