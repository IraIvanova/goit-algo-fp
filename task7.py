import random
import matplotlib.pyplot as plt

def monte_carlo_simulation(num_experiments):
    sum_counter = [0] * 13
    
    for _ in range(num_experiments):
        throw1 = random.randint(1, 6)
        throw2 = random.randint(1, 6)
        throw_sum = throw1 + throw2

        sum_counter[throw_sum] += 1

    return sum_counter


if __name__ == '__main__':
    experiments_num = 10_000_000
    data = monte_carlo_simulation(experiments_num)

    sums = range(2, 13)
    probabilities = [data[sum_value] * 100 / experiments_num for sum_value in sums]

    fig, ax = plt.subplots()
    bar_container = ax.bar(sums, probabilities)
    ax.bar_label(bar_container, fmt='{:,.2f}%')

    plt.xticks(sums)
    plt.xlabel('Сума на кубиках')
    plt.ylabel('Ймовірність (%)')
    plt.title('Ймовірність сум при киданні двох кубиків')
    plt.show()