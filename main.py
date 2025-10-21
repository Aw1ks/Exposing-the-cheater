import random
import matplotlib.pyplot as plt
import webbrowser
import numpy as np


def repetitions_rolls(num_rolls):
    total = 0
    for _ in range(num_rolls):
        roll = random.randint(1, 6)
        total += roll
    average = total / num_rolls
    return average


def main():
    num_rolls = 10000
    num_repetitions = 2000

    averages = []
    for _ in range(num_repetitions):
        average = repetitions_rolls(num_rolls)
        averages.append(average)

    overall_average = sum(averages) / num_repetitions
    print(f'{overall_average}')

    std_dev = (np.var(averages))**0.5

    plt.figure(figsize=(10, 6))
    plt.hist(averages, color='blue')
    plt.xlabel('Итерации')
    plt.ylabel('Частота')
    plt.xlim(3.4, 3.6)
    plt.ylim(0, 600)
    plt.grid(True, alpha=0.2)
    plt.savefig('histogram.png', dpi=300, bbox_inches='tight')
    print('Открываем гистограмму в браузере')
    webbrowser.open('histogram.png')

if __name__ == '__main__':
    main()
