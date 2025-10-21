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


def add_sigma_lines(plt, dispersion, sigma, level, color, label=None):
    left = dispersion - level * sigma
    right = dispersion + level * sigma
    plt.axvline(
        left, 
        color=color, 
        linestyle='--', 
        linewidth=3, 
        label=label
    )
    plt.axvline(
        right, 
        color=color, 
        linestyle='--', 
        linewidth=3
    )


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

    plt.axvline(
        overall_average, 
        color='red', 
        linestyle='--', 
        linewidth=3, 
        label=f'Среднее значение {overall_average}'
    )

    add_sigma_lines(plt, overall_average, std_dev, 1, 'black', f'1 сигма {overall_average}')
    add_sigma_lines(plt, overall_average, std_dev, 2, 'green', f'2 сигма {overall_average}')

    plt.legend()

    plt.savefig('histogram.png', dpi=300, bbox_inches='tight')
    print('Открываем гистограмму в браузере')
    webbrowser.open('histogram.png')

if __name__ == '__main__':
    main()