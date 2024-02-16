def powerball_probability():
    num_choices = 69
    powerball_choices = 26
    
    num_combinations = 1
    for i in range(5):
        num_combinations *= (num_choices - i)
    num_combinations //= (1 * 2 * 3 * 4 * 5)
    
    powerball_combinations = powerball_choices
    
    total_combinations = num_combinations * powerball_combinations
    
    probability = 1 / total_combinations
    
    return probability

print("Probability of winning Powerball: {:.10f}".format(powerball_probability()))
